# Template di Documentazione per Applicazioni AI

Questo documento descrive come utilizzare il sistema di generazione automatica della documentazione basato su RAG (Retrieval-Augmented Generation).

## Come Funziona

Il sistema è composto da due agenti CrewAI:

### 1. Documentation Researcher
- **Ruolo**: Ricerca informazioni esistenti usando il RAG tool
- **Compiti**: 
  - Estrae informazioni dai file HTML nella cartella `docs/`
  - Identifica le informazioni mancanti per ogni sezione del template
  - Prepara domande specifiche per l'utente

### 2. Documentation Generator  
- **Ruolo**: Genera la documentazione finale
- **Compiti**:
  - Combina le informazioni trovate dal RAG
  - Richiede input dall'utente per informazioni mancanti
  - Genera documentazione strutturata seguendo il template TechOps

## Sezioni della Documentazione Generata

Il template seguisce la struttura del [TechOps Application Documentation Template](https://aloosley.github.io/techops/template-application-documentation/) e include:

1. **Key Links** - Repository, pipeline, API, cloud account
2. **General Information** - Scopo, utenti target, KPI, compliance EU AI Act
3. **Risk Classification** - Classificazione del rischio secondo EU AI Act
4. **Application Functionality** - Capacità del modello, limitazioni, architettura
5. **Models and Datasets** - Modelli e dataset integrati
6. **Deployment** - Infrastruttura, ambiente, integrazioni
7. **Lifecycle Management** - Monitoraggio, versioning, gestione rischi
8. **Testing and Validation** - Accuratezza, robustezza, cybersecurity
9. **Human Oversight** - Meccanismi di supervisione umana
10. **Incident Management** - Troubleshooting, supporto

## Utilizzo

### Avvio del Sistema

```bash
python src/documentazione_flow/main.py
```

Seleziona l'opzione "2" per la generazione documentazione.

### Flusso di Lavoro

1. **Input Nome Applicazione**: Inserisci il nome dell'applicazione da documentare
2. **Ricerca Automatica**: Il sistema cerca informazioni nei file HTML della cartella `docs/`
3. **Interazione Utente**: Per informazioni mancanti, il sistema chiederà input specifici
4. **Generazione**: Viene creato un documento Markdown completo
5. **Salvataggio**: Il documento viene salvato come `{nome_app}_documentation.md`

### Esempio di Interazione Utente

Quando mancano informazioni, il sistema presenta domande come:

```
🔍 INFORMAZIONE RICHIESTA per la sezione 'General Information':
❓ Qual è lo scopo principale dell'applicazione AI?
Inserisci la tua risposta (o 'skip' per saltare): 
```

## Struttura dei File

```
documentazione_flow/
├── src/documentazione_flow/
│   ├── tools/
│   │   ├── rag_tool.py          # Tool per ricerca RAG
│   │   └── user_input_tool.py   # Tool per input utente
│   ├── crews/rag_crew/
│   │   ├── rag_crew.py          # Definizione crew
│   │   └── config/
│   │       ├── agents.yaml      # Configurazione agenti
│   │       └── tasks.yaml       # Configurazione task
│   ├── docs/                    # File HTML per RAG
│   └── main.py                  # Punto di ingresso
```

## Requisiti

- Azure OpenAI configurato (variabili ambiente nel file `.env`)
- File HTML nella cartella `docs/` per la ricerca RAG
- Dipendenze Python: crewai, langchain, faiss, beautifulsoup4

## Personalizzazione

Per personalizzare il template o aggiungere nuove sezioni:

1. Modifica i file in `crews/rag_crew/config/`
2. Aggiorna i tool se necessario
3. Modifica il template nel task `generate_documentation_task`

## Compliance EU AI Act

Il template generato include automaticamente i riferimenti agli articoli rilevanti dell'EU AI Act per garantire la compliance normativa.
