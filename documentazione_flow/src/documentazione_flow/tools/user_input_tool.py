from crewai.tools import tool
from typing import Dict, Any

@tool
def request_user_input(question: str, section: str) -> str:
    """
    Richiede input dall'utente per informazioni mancanti nella documentazione.
    
    Args:
        question: La domanda specifica da porre all'utente
        section: La sezione della documentazione a cui si riferisce la domanda
    
    Returns:
        La risposta dell'utente
    """
    print(f"\n🔍 INFORMAZIONE RICHIESTA per la sezione '{section}':")
    print(f"❓ {question}")
    print("---")
    
    user_response = input("Inserisci la tua risposta (o 'skip' per saltare): ")
    
    if user_response.lower() == 'skip':
        return f"[INFORMAZIONE NON FORNITA] - L'utente ha scelto di saltare questa domanda per la sezione '{section}'"
    
    return user_response

@tool
def collect_missing_information(missing_info_list: str) -> str:
    """
    Raccoglie tutte le informazioni mancanti dall'utente in una sessione interattiva.
    
    Args:
        missing_info_list: Lista delle informazioni mancanti in formato stringa
    
    Returns:
        Dizionario con tutte le risposte dell'utente
    """
    print("\n" + "="*60)
    print("🚀 RACCOLTA INFORMAZIONI MANCANTI PER LA DOCUMENTAZIONE")
    print("="*60)
    print("Le seguenti informazioni non sono state trovate nella documentazione esistente.")
    print("Per favore, fornisci le informazioni richieste:\n")
    
    # Simula il parsing della lista di informazioni mancanti
    # In un'implementazione reale, questa dovrebbe essere strutturata meglio
    responses = {}
    
    sections = missing_info_list.split('\n')
    for section_info in sections:
        if section_info.strip() and '|' in section_info:
            try:
                section, question = section_info.split('|', 1)
                section = section.strip()
                question = question.strip()
                
                print(f"\n📋 SEZIONE: {section}")
                print(f"❓ {question}")
                user_response = input("Risposta: ")
                
                if user_response.strip():
                    responses[section] = user_response
                else:
                    responses[section] = "[NON FORNITO]"
                    
            except ValueError:
                continue
    
    print("\n✅ Raccolta informazioni completata!")
    print("="*60)
    
    # Formatta le risposte per l'uso nella documentazione
    formatted_responses = ""
    for section, response in responses.items():
        formatted_responses += f"**{section}**: {response}\n\n"
    
    return formatted_responses
