from crewai.tools import tool
from typing import Dict, Any, Union
import json
import sys
import os

# Global dictionary to track asked questions and prevent loops
_asked_questions = {}
_session_responses = {}

@tool
def request_user_input(question: str, section: str) -> str:
    """
    Richiede input dall'utente per informazioni mancanti nella documentazione.
    Previene loop evitando di fare la stessa domanda più volte.
    
    Args:
        question: La domanda specifica da porre all'utente
        section: La sezione della documentazione a cui si riferisce la domanda
    
    Returns:
        La risposta dell'utente
    """
    global _asked_questions, _session_responses
    
    # Create a unique key for this question
    question_key = f"{section}::{question.strip()}"
    
    # Check if we've already asked this question
    if question_key in _asked_questions:
        print(f"⚠️  Domanda già posta per '{section}': {question}")
        stored_response = _asked_questions[question_key]
        print(f"📋 Risposta precedente: {stored_response}")
        return stored_response
    
    print(f"\n{'='*80}")
    print(f"🔍 INFORMAZIONE RICHIESTA per '{section}'")
    print(f"{'='*80}")
    print(f"❓ {question}")
    print(f"{'-'*80}")
    print("💡 Suggerimenti:")
    print("   • Fornisci informazioni specifiche e dettagliate")
    print("   • Se non hai l'informazione, scrivi 'Non disponibile'")
    print("   • Includi esempi concreti quando possibile")
    print("   • Scrivi 'skip' per saltare questa domanda")
    print(f"{'-'*80}")
    
    try:
        user_response = input("📝 La tua risposta: ").strip()
    except (EOFError, KeyboardInterrupt):
        # Handle non-interactive environment or user interruption
        response = f"[INFORMAZIONE RICHIESTA] - Sezione '{section}': {question}"
        _asked_questions[question_key] = response
        return response
    
    # Process the response
    if user_response.lower() in ['skip', 'salta', '']:
        response = f"[INFORMAZIONE NON FORNITA] - Sezione '{section}': {question}"
    elif user_response.lower() in ['non disponibile', 'n/a', 'na', 'non lo so']:
        response = f"[INFORMAZIONE NON DISPONIBILE] - Sezione '{section}': {question}"
    elif user_response:
        response = user_response
        print("✅ Risposta salvata!")
    else:
        response = f"[RISPOSTA VUOTA] - Sezione '{section}': {question}"
    
    # Store the response to prevent asking again
    _asked_questions[question_key] = response
    _session_responses[section] = _session_responses.get(section, {})
    _session_responses[section][question] = response
    
    return response

@tool 
def collect_missing_information(questions_json: Union[str, dict]) -> str:
    """
    Raccoglie tutte le informazioni mancanti dall'utente in una sessione interattiva strutturata.
    Previene loop e domande duplicate.
    
    Args:
        questions_json: JSON string o dizionario contenente le domande organizzate per sezione
    
    Returns:
        JSON string con tutte le risposte dell'utente organizzate per sezione
    """
    global _asked_questions, _session_responses
    
    print("\n" + "="*100)
    print("🚀 RACCOLTA INFORMAZIONI MANCANTI PER LA DOCUMENTAZIONE EU AI ACT")
    print("="*100)
    print("📋 Le seguenti informazioni sono necessarie per completare la documentazione.")
    print("💬 Rispondi a ciascuna domanda nel modo più dettagliato possibile.")
    print("⏭️  Puoi digitare 'skip' per saltare una domanda o 'Non disponibile' se non hai l'informazione.")
    print("🔄 Le domande già risposte non verranno richieste nuovamente.")
    print("="*100)
    
    try:
        # Prova a parsare il JSON delle domande
        if isinstance(questions_json, str):
            questions_data = json.loads(questions_json)
        elif isinstance(questions_json, dict):
            questions_data = questions_json
        else:
            questions_data = {"Informazioni Generali": [str(questions_json)]}
    except (json.JSONDecodeError, TypeError):
        questions_data = {"Informazioni Generali": [str(questions_json)]}
    
    responses = {}
    total_questions = 0
    answered_questions = 0
    skipped_questions = 0
    
    # Conta il totale delle domande e filtra quelle già riposte
    for section, questions in questions_data.items():
        if isinstance(questions, list):
            for question in questions:
                question_key = f"{section}::{question.strip()}"
                if question_key not in _asked_questions:
                    total_questions += 1
        else:
            question_key = f"{section}::{questions.strip()}"
            if question_key not in _asked_questions:
                total_questions += 1
    
    if total_questions == 0:
        print("✅ Tutte le domande sono già state risposte in questa sessione!")
        return json.dumps(_session_responses, indent=2, ensure_ascii=False)
    
    current_question = 0
    
    for section, questions in questions_data.items():
        print(f"\n📂 SEZIONE: {section}")
        print(f"{'─'*60}")
        
        section_responses = _session_responses.get(section, {})
        
        if isinstance(questions, list):
            for question in questions:
                question_key = f"{section}::{question.strip()}"
                
                # Skip if already asked
                if question_key in _asked_questions:
                    print(f"⏭️  Saltata (già risposta): {question[:50]}...")
                    section_responses[question] = _asked_questions[question_key]
                    continue
                    
                current_question += 1
                print(f"\n[{current_question}/{total_questions}] 🔍 {section}")
                print(f"❓ {question}")
                print(f"{'─'*40}")
                
                try:
                    user_response = input("📝 Risposta: ").strip()
                except (EOFError, KeyboardInterrupt):
                    user_response = ""
                    response = f"[INFORMAZIONE RICHIESTA: {question}]"
                    _asked_questions[question_key] = response
                    section_responses[question] = response
                    print("ℹ️  Ambiente non interattivo - marcato come richiesto")
                    continue
                
                if user_response.lower() in ['skip', 'salta']:
                    response = "[SALTATO]"
                    skipped_questions += 1
                    print("⏭️  Domanda saltata")
                elif user_response.lower() in ['non disponibile', 'n/a', 'na', 'non lo so']:
                    response = "[NON DISPONIBILE]"
                    print("ℹ️  Marcato come non disponibile")
                elif user_response:
                    response = user_response
                    answered_questions += 1
                    print("✅ Risposta salvata!")
                else:
                    response = "[VUOTO]"
                    print("⚠️  Risposta vuota")
                
                _asked_questions[question_key] = response
                section_responses[question] = response
        else:
            # Singola domanda
            question_key = f"{section}::{questions.strip()}"
            
            if question_key in _asked_questions:
                print(f"⏭️  Saltata (già risposta): {questions[:50]}...")
                section_responses[questions] = _asked_questions[question_key]
            else:
                current_question += 1
                print(f"\n[{current_question}/{total_questions}] ❓ {questions}")
                print(f"{'─'*40}")
                
                try:
                    user_response = input("📝 Risposta: ").strip()
                except (EOFError, KeyboardInterrupt):
                    user_response = ""
                    response = f"[INFORMAZIONE RICHIESTA: {questions}]"
                    _asked_questions[question_key] = response
                    section_responses[questions] = response
                    continue
                
                if user_response.lower() in ['skip', 'salta']:
                    response = "[SALTATO]"
                    skipped_questions += 1
                elif user_response.lower() in ['non disponibile', 'n/a', 'na', 'non lo so']:
                    response = "[NON DISPONIBILE]"
                elif user_response:
                    response = user_response
                    answered_questions += 1
                else:
                    response = "[VUOTO]"
                
                _asked_questions[question_key] = response
                section_responses[questions] = response
        
        responses[section] = section_responses
        _session_responses[section] = section_responses
    
    print(f"\n{'='*100}")
    print(f"✅ RACCOLTA COMPLETATA!")
    print(f"📊 Statistiche: {answered_questions}/{total_questions} domande completate")
    print(f"⏭️  {skipped_questions} domande saltate")
    print(f"📈 Completamento: {answered_questions/total_questions*100:.1f}%" if total_questions > 0 else "📈 Completamento: 100%")
    print(f"{'='*100}")
    
    return json.dumps(responses, indent=2, ensure_ascii=False)

@tool
def collect_section_information(section_name: str, questions: str) -> str:
    """
    Raccoglie informazioni specifiche per una singola sezione della documentazione.
    Previene loop e domande duplicate.
    
    Args:
        section_name: Nome della sezione della documentazione
        questions: Lista di domande per quella sezione (una per riga)
    
    Returns:
        Informazioni raccolte per quella sezione
    """
    global _asked_questions, _session_responses
    
    print(f"\n{'='*80}")
    print(f"📂 RACCOLTA INFORMAZIONI PER: {section_name}")
    print(f"{'='*80}")
    
    questions_list = [q.strip() for q in questions.split('\n') if q.strip()]
    responses = {}
    new_questions = []
    
    # Filter out already asked questions
    for question in questions_list:
        question_key = f"{section_name}::{question.strip()}"
        if question_key in _asked_questions:
            print(f"⏭️  Già risposta: {question[:50]}...")
            responses[question] = _asked_questions[question_key]
        else:
            new_questions.append(question)
    
    if not new_questions:
        print("✅ Tutte le domande per questa sezione sono già state risposte!")
        # Return existing responses
        return json.dumps({section_name: responses}, indent=2, ensure_ascii=False)
    
    for i, question in enumerate(new_questions, 1):
        question_key = f"{section_name}::{question.strip()}"
        
        print(f"\n[{i}/{len(new_questions)}] ❓ {question}")
        print(f"{'─'*60}")
        
        try:
            user_response = input("📝 Risposta: ").strip()
        except (EOFError, KeyboardInterrupt):
            user_response = ""
            response = f"[INFORMAZIONE RICHIESTA: {question}]"
            _asked_questions[question_key] = response
            responses[question] = response
            print("ℹ️  Ambiente non interattivo - marcato come richiesto")
            continue
        
        if user_response.lower() in ['skip', 'salta']:
            response = "[SALTATO]"
            print("⏭️  Domanda saltata")
        elif user_response.lower() in ['non disponibile', 'n/a', 'na', 'non lo so']:
            response = "[NON DISPONIBILE]"
            print("ℹ️  Marcato come non disponibile")
        elif user_response:
            response = user_response
            print("✅ Risposta salvata!")
        else:
            response = "[VUOTO]"
            print("⚠️  Risposta vuota")
        
        _asked_questions[question_key] = response
        responses[question] = response
    
    print(f"\n✅ Sezione '{section_name}' completata!")
    
    # Update session responses
    _session_responses[section_name] = responses
    
    # Formatta le risposte per l'uso nella documentazione
    formatted_responses = f"## Informazioni raccolte per {section_name}:\n\n"
    for question, response in responses.items():
        formatted_responses += f"**{question}**\n{response}\n\n"
    
    return formatted_responses

@tool
def reset_user_input_session() -> str:
    """
    Resetta la sessione di input utente, cancellando tutte le domande già poste.
    Utile per iniziare una nuova sessione di raccolta informazioni.
    
    Returns:
        Messaggio di conferma del reset
    """
    global _asked_questions, _session_responses
    
    previous_count = len(_asked_questions)
    _asked_questions.clear()
    _session_responses.clear()
    
    return f"✅ Sessione di input utente resettata. {previous_count} domande precedenti cancellate."

@tool
def get_session_summary() -> str:
    """
    Restituisce un riassunto della sessione corrente con tutte le risposte raccolte.
    
    Returns:
        Riassunto della sessione in formato JSON
    """
    global _session_responses
    
    if not _session_responses:
        return "📭 Nessuna informazione raccolta in questa sessione."
    
    summary = {
        "total_sections": len(_session_responses),
        "total_questions": sum(len(section) for section in _session_responses.values()),
        "responses": _session_responses
    }
    
    return json.dumps(summary, indent=2, ensure_ascii=False)
