from crewai.tools import tool
from pathlib import Path
from typing import List
import os
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import BSHTMLLoader


load_dotenv()

class RAGSystem:
    def __init__(self):
        self.persist_dir = "faiss_index_medical"
        self.k = 4
        
        self.embeddings = self._get_embeddings()
        self.llm = self._get_llm()
        self.vector_store = None
        self.chain = None
        
        self._initialize_rag()
    
    def _get_embeddings(self):
        """Inizializza embedding Azure OpenAI"""
        api_key = os.getenv("AZURE_API_KEY")
        return AzureOpenAIEmbeddings(
            model="text-embedding-ada-002",
            azure_endpoint=os.getenv("AZURE_API_BASE"),
            api_key=api_key
        )
    
    def _get_llm(self):
        """Inizializza LLM Azure OpenAI"""
        api_key = os.getenv("AZURE_API_KEY")
        endpoint = os.getenv("AZURE_API_BASE")
        deployment = os.getenv("MODEL")

        return AzureChatOpenAI(
            deployment_name=deployment,
            openai_api_version="2024-02-15-preview",
            azure_endpoint=endpoint,
            openai_api_key=api_key,
            temperature=0.1
        )
    
    def _create_documents(self) -> List[Document]:
        """Crea documenti HTML dalla cartella docs"""
        documents = []
        
        # Percorso della cartella docs
        docs_path = Path(__file__).parent.parent / "docs"
        
        if not docs_path.exists():
            print(f"⚠️ Cartella docs non trovata in: {docs_path}")
            return documents
        
        # Configura il text splitter per dividere documenti lunghi
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Carica tutti i file HTML
        html_files = list(docs_path.glob("*.html"))
        
        if not html_files:
            print(f"⚠️ Nessun file HTML trovato in: {docs_path}")
            return documents
        
        for html_file in html_files:
            try:
                # Usa BSHTMLLoader per caricare e parsare l'HTML
                loader = BSHTMLLoader(str(html_file))
                loaded_docs = loader.load()
                
                # Aggiungi metadata personalizzati
                for doc in loaded_docs:
                    doc.metadata.update({
                        "source": html_file.name,
                        "file_type": "html",
                        "category": "documentation"
                    })
                
                # Dividi i documenti in chunk più piccoli
                split_docs = text_splitter.split_documents(loaded_docs)
                documents.extend(split_docs)
                
                print(f"✅ Caricato: {html_file.name} ({len(split_docs)} chunks)")
                
            except Exception as e:
                print(f"❌ Errore nel caricamento di {html_file.name}: {str(e)}")
                continue
        
        print(f"📚 Totale documenti caricati: {len(documents)} chunks da {len(html_files)} file HTML")
        return documents
    
    def _initialize_rag(self):
        """Inizializza o carica il sistema RAG"""
        if Path(self.persist_dir).exists():
            # Carica indice esistente
            self.vector_store = FAISS.load_local(
                self.persist_dir,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            print("✅ Indice FAISS caricato da disco")
        else:
            # Crea nuovo indice
            documents = self._create_documents()
            self.vector_store = FAISS.from_documents(
                documents,
                self.embeddings
            )
            # Salva su disco
            self.vector_store.save_local(self.persist_dir)
            print("✅ Nuovo indice FAISS creato e salvato")
        
        # Costruisci la chain RAG
        self._build_rag_chain()
    
    def _format_docs(self, docs: List[Document]) -> str:
        """Formatta i documenti recuperati"""
        return "\n\n---\n\n".join(doc.page_content for doc in docs)
    
    def _build_rag_chain(self):
        """Costruisce la chain RAG con LangChain"""
        # Template del prompt
        template = """Sei un assistente esperto. Usa le seguenti informazioni dalla documentazione per rispondere alla domanda.
        Se le informazioni non sono sufficienti, indicalo chiaramente.
        
        Contesto dalla documentazione:
        {context}
        
        Domanda: {question}
        
        Fornisci una risposta dettagliata e precisa basata sulla documentazione disponibile:"""
        
        prompt = ChatPromptTemplate.from_template(template)
        
        # Crea il retriever
        retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": self.k}
        )
        
        # Costruisci la chain
        self.chain = (
            {"context": retriever | self._format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def search(self, question: str) -> str:
        """Esegue una ricerca RAG"""
        if not self.chain:
            return "❌ Sistema RAG non inizializzato correttamente"
        
        try:
            result = self.chain.invoke(question)
            return result
            
        except Exception as e:
            return f"❌ Errore nella ricerca RAG: {str(e)}"

# Istanza globale del sistema RAG
_rag_system = None

def get_rag_system():
    """Restituisce l'istanza singleton del sistema RAG"""
    global _rag_system
    if _rag_system is None:
        _rag_system = RAGSystem()
    return _rag_system

@tool
def search_rag(question: str) -> str:
    """
    Effettua una ricerca nella documentazione HTML utilizzando RAG.
    Restituisce informazioni basate sui file HTML nella cartella docs.
    """
    try:
        rag_system = get_rag_system()
        result = rag_system.search(question)
        return f"Risultato della ricerca nella documentazione per '{question}':\n\n{result}"
    except Exception as e:
        return f"Errore nella ricerca RAG: {str(e)}"