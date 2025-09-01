from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from documentazione_flow.crews.rag_crew.rag_crew import RagCrew


class DocumentationState(BaseModel):
    application_name: str = ""
    documentation: str = ""


class DocumentationFlow(Flow[DocumentationState]):
    
    @start()
    def setup_application_name(self):
        print("📝 GENERAZIONE DOCUMENTAZIONE APPLICAZIONE")
        print("=" * 50)
        application_name = input("Inserisci il nome dell'applicazione da documentare: ")
        self.state.application_name = application_name or "MiaApplicazioneAI"
        print(f"🎯 Generazione documentazione per: {self.state.application_name}")

    @listen(setup_application_name)
    def generate_documentation(self):
        print(f"🚀 Avvio generazione documentazione per {self.state.application_name}")
        
        result = (
            RagCrew()
            .crew()
            .kickoff(inputs={"application_name": self.state.application_name})
        )

        print("✅ Documentazione generata!")
        self.state.documentation = result.raw

    @listen(generate_documentation)
    def save_documentation(self):
        print("💾 Salvataggio documentazione...")
        filename = f"{self.state.application_name.lower().replace(' ', '_')}_documentation.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.state.documentation)
        print(f"📄 Documentazione salvata in: {filename}")


def kickoff_documentation():
    """Avvia il flow per la generazione della documentazione"""
    doc_flow = DocumentationFlow()
    doc_flow.kickoff()


def plot_documentation():
    """Mostra il diagramma del flow di documentazione"""
    doc_flow = DocumentationFlow()
    doc_flow.plot()


if __name__ == "__main__":
    print("📝 SISTEMA DI GENERAZIONE DOCUMENTAZIONE AI")
    print("=" * 50)
    kickoff_documentation()
