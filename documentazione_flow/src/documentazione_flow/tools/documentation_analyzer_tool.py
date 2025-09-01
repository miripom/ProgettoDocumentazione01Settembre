from crewai.tools import tool
from typing import Dict, List, Any
import json

@tool
def analyze_template_sections() -> str:
    """
    Restituisce la struttura dettagliata del template di documentazione EU AI Act
    con le informazioni specifiche richieste per ogni sezione.
    """
    template_structure = {
        "Application Documentation Template": {
            "required_fields": [
                "Application Owner (Name, Email, Phone, Department)",
                "Document Version (Version, Last Updated, Change Log)",
                "Reviewers (Technical, Legal, Security, Business)"
            ],
            "rag_search_queries": [
                "Who is the application owner? Contact information?",
                "What is the current version of the application?",
                "Who are the reviewers for this application?"
            ]
        },
        "Key Links": {
            "required_fields": [
                "Code Repository (GitHub URL, Branch, Access)",
                "Deployment Pipeline (CI/CD Platform, Pipeline URL, Environment)",
                "API Documentation (Swagger Docs, API Version, Authentication)",
                "Cloud Account (Provider, Subscription, Resource Group, Region)",
                "Project Management Board (Platform, Board URL, Epic)",
                "Application Architecture (Diagram, Technology Stack, Deployment Model)"
            ],
            "rag_search_queries": [
                "What is the GitHub repository URL?",
                "What CI/CD platform is used?",
                "Where is the API documentation located?",
                "What cloud provider and services are used?",
                "What project management tools are used?",
                "What is the application architecture and technology stack?"
            ]
        },
        "Purpose and Intended Use": {
            "required_fields": [
                "AI System Purpose Description",
                "Problem the AI Application Aims to Solve",
                "Target Users and Stakeholders",
                "Measurable Goals and KPIs",
                "Ethical Considerations and Regulatory Constraints",
                "Clear Statement on Prohibited Uses",
                "Operational Environment"
            ],
            "rag_search_queries": [
                "What is the purpose of this AI system?",
                "What problem does the application solve?",
                "Who are the target users?",
                "What are the success metrics and KPIs?",
                "What are the ethical considerations?",
                "What are the prohibited uses?",
                "What is the operational environment?"
            ]
        },
        "EU AI Act Risk Classification": {
            "required_fields": [
                "Risk classification (High/Limited/Minimal) with justification",
                "Required compliance measures",
                "Excluded high-risk categories"
            ],
            "rag_search_queries": [
                "What is the EU AI Act risk classification?",
                "What compliance measures are implemented?",
                "What high-risk categories are excluded?"
            ]
        },
        "Application Functionality": {
            "required_fields": [
                "Model Capabilities (what it can do)",
                "Model Limitations (what it cannot do)",
                "Input Data Requirements and Examples",
                "Output Explanation and Interpretation",
                "System Architecture Overview"
            ],
            "rag_search_queries": [
                "What are the model capabilities and limitations?",
                "What input data formats are supported?",
                "How should outputs be interpreted?",
                "What is the detailed system architecture?"
            ]
        },
        "Models and Datasets": {
            "required_fields": [
                "Complete model documentation table with links",
                "Dataset documentation table with usage descriptions",
                "Links to Single Source of Truth for each model/dataset"
            ],
            "rag_search_queries": [
                "What AI models are used in the system?",
                "What datasets are used for training and evaluation?",
                "Where is the model and dataset documentation located?"
            ]
        },
        "Deployment": {
            "required_fields": [
                "Infrastructure and Environment Details",
                "Cloud Setup (Provider, Regions, Services)",
                "Integration with External Systems",
                "API Endpoints and Authentication",
                "Deployment Plan and Rollback Strategies"
            ],
            "rag_search_queries": [
                "What is the deployment infrastructure?",
                "What cloud services and regions are used?",
                "What external systems are integrated?",
                "What are the API endpoints and authentication methods?",
                "What is the deployment and rollback strategy?"
            ]
        },
        "Lifecycle Management": {
            "required_fields": [
                "Monitoring Procedures and Real-time Metrics",
                "Performance KPIs and Thresholds",
                "Versioning and Change Management",
                "Update and Maintenance Procedures"
            ],
            "rag_search_queries": [
                "What monitoring procedures are in place?",
                "What performance metrics are tracked?",
                "How is versioning and change management handled?",
                "What are the update and maintenance procedures?"
            ]
        },
        "Risk Management System": {
            "required_fields": [
                "Risk Assessment Methodology",
                "Identified Risks (likelihood and severity)",
                "Risk Mitigation Measures",
                "Preventive and Protective Measures"
            ],
            "rag_search_queries": [
                "What risk assessment methodology is used?",
                "What specific risks have been identified?",
                "What risk mitigation measures are implemented?",
                "What preventive and protective measures exist?"
            ]
        },
        "Testing and Validation": {
            "required_fields": [
                "Accuracy Testing (metrics, validation results)",
                "Data Quality and Management procedures",
                "Robustness Measures (adversarial testing, stress testing)",
                "Cybersecurity (data security, access control, incident response)"
            ],
            "rag_search_queries": [
                "What accuracy testing has been performed?",
                "What data quality procedures are in place?",
                "What robustness testing has been conducted?",
                "What cybersecurity measures are implemented?"
            ]
        },
        "Human Oversight": {
            "required_fields": [
                "Human-in-the-Loop Mechanisms",
                "Override and Intervention Procedures",
                "User Instructions and Training",
                "System Limitations and Constraints"
            ],
            "rag_search_queries": [
                "What human oversight mechanisms exist?",
                "What override and intervention procedures are available?",
                "What user training and instructions are provided?",
                "What are the system limitations and constraints?"
            ]
        },
        "Incident Management": {
            "required_fields": [
                "Common Issues and Solutions",
                "Troubleshooting Procedures",
                "Support Contact Information",
                "Escalation Procedures"
            ],
            "rag_search_queries": [
                "What common issues have been identified?",
                "What troubleshooting procedures exist?",
                "What support contacts are available?",
                "What are the escalation procedures?"
            ]
        }
    }
    
    return json.dumps(template_structure, indent=2)

@tool
def generate_targeted_questions(section_name: str, rag_findings: str) -> str:
    """
    Genera domande specifiche e mirate per una sezione della documentazione
    basandosi sui risultati della ricerca RAG e sulle informazioni mancanti.
    
    Args:
        section_name: Nome della sezione della documentazione
        rag_findings: Risultati della ricerca RAG per quella sezione
    
    Returns:
        Lista di domande specifiche per raccogliere le informazioni mancanti
    """
    
    section_questions = {
        "Application Documentation Template": [
            "Qual è il nome completo, email, telefono e dipartimento del proprietario dell'applicazione?",
            "Qual è la versione corrente del documento e la data dell'ultimo aggiornamento?",
            "Chi sono i revisori tecnici, legali, di sicurezza e business di questa applicazione?"
        ],
        "Key Links": [
            "Qual è l'URL esatto del repository GitHub e il branch principale?",
            "Qual è la piattaforma CI/CD utilizzata e l'URL della pipeline?",
            "Dove si trova la documentazione API (URL Swagger) e qual è la versione API?",
            "Qual è il provider cloud, l'ID subscription, il resource group e la regione?",
            "Qual è la piattaforma di project management e l'URL del board?",
            "Dove si trova il diagramma dell'architettura applicativa?"
        ],
        "Purpose and Intended Use": [
            "Qual è lo scopo specifico di questo sistema di intelligenza artificiale?",
            "Quale problema specifico risolve questa applicazione AI?",
            "Chi sono gli utenti target primari e secondari?",
            "Quali sono i KPI misurabili e gli obiettivi di successo specifici?",
            "Quali considerazioni etiche specifiche sono state identificate?",
            "Quali sono gli utilizzi espressamente proibiti di questo sistema?",
            "In quale ambiente operativo specifico viene utilizzato il sistema?"
        ],
        "EU AI Act Risk Classification": [
            "Qual è la classificazione di rischio secondo l'EU AI Act (Alto/Limitato/Minimo)?",
            "Quali misure di compliance specifiche sono state implementate?",
            "Quali categorie ad alto rischio sono state escluse e perché?"
        ],
        "Application Functionality": [
            "Cosa può fare specificamente questo modello AI? Elencare le capacità dettagliate.",
            "Cosa NON può fare questo modello? Elencare le limitazioni specifiche.",
            "Quali formati di dati di input sono supportati? Fornire esempi specifici.",
            "Come devono essere interpretati gli output del sistema?",
            "Qual è l'architettura dettagliata del sistema con componenti specifici?"
        ],
        "Models and Datasets": [
            "Quali modelli AI specifici sono utilizzati (nomi, versioni, provider)?",
            "Quali dataset sono utilizzati per training e valutazione?",
            "Dove si trova la documentazione completa per ogni modello?",
            "Dove si trova la documentazione completa per ogni dataset?"
        ],
        "Deployment": [
            "Qual è l'infrastruttura di deployment specifica (VM, container, etc.)?",
            "Quali servizi cloud specifici sono utilizzati?",
            "Quali sistemi esterni sono integrati e come?",
            "Quali sono gli endpoint API specifici e i metodi di autenticazione?",
            "Qual è la strategia di deployment e rollback dettagliata?"
        ],
        "Lifecycle Management": [
            "Quali procedure di monitoraggio in tempo reale sono implementate?",
            "Quali metriche di performance specifiche sono tracciate e con che soglie?",
            "Come è gestito il versioning e il change management?",
            "Quali sono le procedure specifiche di update e manutenzione?"
        ],
        "Risk Management System": [
            "Quale metodologia di risk assessment è utilizzata (ISO 31000, etc.)?",
            "Quali rischi specifici sono stati identificati con likelihood e severity?",
            "Quali misure di mitigazione specifiche sono implementate?",
            "Quali misure preventive e protettive sono in atto?"
        ],
        "Testing and Validation": [
            "Quali test di accuratezza sono stati eseguiti con risultati specifici?",
            "Quali procedure di data quality sono implementate?",
            "Quali test di robustezza (adversarial, stress) sono stati condotti?",
            "Quali misure di cybersecurity specifiche sono implementate?"
        ],
        "Human Oversight": [
            "Quali meccanismi human-in-the-loop sono implementati?",
            "Quali procedure di override e intervento sono disponibili?",
            "Quali istruzioni e training per gli utenti sono forniti?",
            "Quali sono le limitazioni e constraints specifici del sistema?"
        ],
        "Incident Management": [
            "Quali problemi comuni sono stati identificati con relative soluzioni?",
            "Quali procedure di troubleshooting sono documentate?",
            "Quali sono i contatti di supporto specifici?",
            "Quali sono le procedure di escalation definite?"
        ]
    }
    
    base_questions = section_questions.get(section_name, [
        f"Quali informazioni specifiche sono richieste per la sezione '{section_name}'?",
        f"Quali dettagli tecnici sono necessari per completare la sezione '{section_name}'?",
        f"Quali informazioni di compliance sono richieste per la sezione '{section_name}'?"
    ])
    
    # Analizza i risultati RAG per identificare cosa manca
    missing_info_analysis = f"""
    SEZIONE: {section_name}
    
    RISULTATI RAG DISPONIBILI:
    {rag_findings}
    
    DOMANDE SPECIFICHE PER INFORMAZIONI MANCANTI:
    """
    
    for i, question in enumerate(base_questions, 1):
        missing_info_analysis += f"{i}. {question}\n"
    
    missing_info_analysis += f"""
    
    ISTRUZIONI PER L'UTENTE:
    - Rispondi in modo specifico e dettagliato a ogni domanda
    - Se non hai l'informazione, indica chiaramente "Non disponibile" 
    - Fornisci esempi concreti quando possibile
    - Include riferimenti a documentazione esistente se applicabile
    """
    
    return missing_info_analysis

@tool
def validate_documentation_completeness(documentation_content: str) -> str:
    """
    Valida la completezza della documentazione generata confrontandola
    con i requisiti del template EU AI Act.
    
    Args:
        documentation_content: Contenuto della documentazione generata
    
    Returns:
        Report di validazione con sezioni mancanti o incomplete
    """
    required_sections = [
        "Application Documentation Template",
        "Key Links", 
        "Purpose and Intended Use",
        "EU AI Act Risk Classification",
        "Application Functionality",
        "Models and Datasets",
        "Deployment",
        "Lifecycle Management", 
        "Risk Management System",
        "Testing and Validation",
        "Human Oversight",
        "Incident Management",
        "EU Declaration of Conformity"
    ]
    
    validation_report = "# DOCUMENTATION COMPLETENESS VALIDATION REPORT\n\n"
    
    missing_sections = []
    incomplete_sections = []
    complete_sections = []
    
    for section in required_sections:
        if section not in documentation_content:
            missing_sections.append(section)
        elif "[INFORMATION NEEDED" in documentation_content or "[NON FORNITO]" in documentation_content:
            # Controlla se questa sezione specifica ha placeholder
            section_start = documentation_content.find(section)
            if section_start != -1:
                # Trova la fine della sezione (prossima sezione o fine documento)
                next_section_start = len(documentation_content)
                for other_section in required_sections:
                    if other_section != section:
                        other_start = documentation_content.find(other_section, section_start + 1)
                        if other_start != -1 and other_start < next_section_start:
                            next_section_start = other_start
                
                section_content = documentation_content[section_start:next_section_start]
                if "[INFORMATION NEEDED" in section_content or "[NON FORNITO]" in section_content:
                    incomplete_sections.append(section)
                else:
                    complete_sections.append(section)
            else:
                incomplete_sections.append(section)
        else:
            complete_sections.append(section)
    
    validation_report += f"## ✅ COMPLETE SECTIONS ({len(complete_sections)}):\n"
    for section in complete_sections:
        validation_report += f"- {section}\n"
    
    validation_report += f"\n## ⚠️ INCOMPLETE SECTIONS ({len(incomplete_sections)}):\n"
    for section in incomplete_sections:
        validation_report += f"- {section} (contains placeholders or missing information)\n"
    
    validation_report += f"\n## ❌ MISSING SECTIONS ({len(missing_sections)}):\n"
    for section in missing_sections:
        validation_report += f"- {section}\n"
    
    completeness_percentage = (len(complete_sections) / len(required_sections)) * 100
    validation_report += f"\n## OVERALL COMPLETENESS: {completeness_percentage:.1f}%\n"
    
    if completeness_percentage == 100:
        validation_report += "\n🎉 **DOCUMENTATION IS COMPLETE AND READY FOR REVIEW!**"
    elif completeness_percentage >= 80:
        validation_report += "\n👍 **DOCUMENTATION IS MOSTLY COMPLETE - MINOR ADDITIONS NEEDED**"
    elif completeness_percentage >= 60:
        validation_report += "\n⚠️ **DOCUMENTATION NEEDS SIGNIFICANT ADDITIONS**"
    else:
        validation_report += "\n❌ **DOCUMENTATION IS SIGNIFICANTLY INCOMPLETE**"
    
    return validation_report
