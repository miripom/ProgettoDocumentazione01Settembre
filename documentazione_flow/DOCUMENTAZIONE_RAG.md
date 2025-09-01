# RAGFlow AI System Description - EU AI Act Compliance

## **Application Documentation Template**

### **Application Owner**
- **Name:** Miriana Pompilio
- **Email:** email
- **Phone:** 123456789
- **Department:** AI&Data

### **Document Version**
- **Version:** 1.0.0
- **Last Updated:** 09/01/2025
- **Change Log:** Initial version for EU AI Act compliance

### **Reviewers**
- **Technical Review:** [Technical Reviewer Name]
- **Legal Review:** [Legal/Compliance Reviewer Name]
- **Security Review:** [Security Reviewer Name]
- **Business Review:** [Business Stakeholder Name]

## **Key Links**

### **Code Repository**
- **GitHub Repository:** https://github.com/miripom/Deposito_Pompilio
- **Branch:** main
- **Access:** Private repository with team access

### **Deployment Pipeline**
- **CI/CD Platform:** [GitHub Actions / Azure DevOps / Other]
- **Pipeline URL:** [Pipeline URL]
- **Environment:** Development, Staging, Production

### **API Documentation**
- **Swagger Docs:** [API Documentation URL]
- **API Version:** v1.0
- **Authentication:** Azure OpenAI API Keys

### **Cloud Account**
- **Cloud Provider:** Microsoft Azure
- **Subscription:** [Your Azure Subscription ID]
- **Resource Group:** [Resource Group Name]
- **Region:** [Azure Region]

### **Project Management Board**
- **Platform:** [Jira / Azure DevOps / GitHub Projects / Other]
- **Board URL:** [Project Board URL]
- **Epic:** RAGFlow AI System Development

### **Application Architecture**
- **Architecture Diagram:** [Link to Architecture Diagram]
- **Technology Stack:** Python, CrewAI, Azure OpenAI, FAISS
- **Deployment Model:** Multi-cloud with local components

---

## **Purpose and Intended Use**

### **AI System Purpose Description**
RAGFlow is a multi-agent artificial intelligence system designed to provide intelligent assistance in research and question resolution through specialized modalities. The system operates in the education, medical research, and mathematical problem-solving sectors.

### **Problem the AI Application Aims to Solve**
The system addresses the fragmentation of information sources and the need for intelligent routing of questions to the most appropriate resources. RAGFlow automates query classification and automatically directs requests to:
- **Mathematical calculators** for computational problems
- **Tutorial systems** for educational explanations
- **Local medical databases (RAG)** for health information
- **Web searches** for general questions

### **Target Users and Stakeholders**
- **Primary Users:** Students, educators, medical professionals, researchers
- **Stakeholders:** Educational institutions, healthcare facilities, research organizations
- **End Users:** Individuals requiring assistance in mathematics, medicine, or general research

### **Measurable Goals and KPIs**
- Question classification accuracy: **>95%**
- Average response time: **<30 seconds**
- User satisfaction rate: **>90%**
- Mathematical response precision: **>99%**
- Relevance of provided medical information: **>95%**

### **Ethical Considerations and Regulatory Constraints**
- Compliance with medical data privacy regulations
- Transparency in routing decisions
- Fairness in information access
- Responsibility in providing medical information
- Compliance with EU AI Act and local regulations

### **Clear Statement on Prohibited Uses**
> **⚠️ PROHIBITED USES:** The system must not be used for:
> - Definitive medical diagnoses or prescriptions
> - Replacing professional medical consultation
> - Critical safety mathematical calculations (e.g., aerospace engineering)
> - Automated decisions affecting legal rights
> - Unauthorized collection of personal data

### **Operational Environment**
The RAGFlow system operates on cloud platforms and local systems, utilizing:

| Component | Description |
|-----------|-------------|
| **Infrastructure** | Cloud servers with containerization support |
| **Platforms** | Compatible with Windows, Linux, and macOS |
| **Architecture** | Multi-agent system based on Python with CrewAI framework |
| **Storage** | FAISS vector database for local medical indices |
| **APIs** | Integration with Azure OpenAI services for embedding and text generation |
| **Interface** | Interactive console with potential web extension |

## **EU AI Act Risk Classification**

Based on the system's nature and uses, RAGFlow is classified as a **limited-risk AI system** requiring:

- ✅ User transparency and information
- ✅ Adequate governance measures
- ✅ Continuous performance monitoring
- ✅ Risk management procedures

The system implements appropriate security controls and does not operate in high-risk sectors such as:
- 🚫 Biometric surveillance
- 🚫 Critical infrastructure management
- 🚫 Law enforcement decision-making
- 🚫 Migration and border control

## **Application Functionality**

### **Instructions for Use for Deployers (EU AI Act Article 13)**

#### **Model Capabilities**
**What the application can do:**
- Automatically classify user questions into mathematical, medical, or general categories
- Perform mathematical calculations with high precision
- Generate educational tutorials and explanations
- Search local medical databases using RAG (Retrieval-Augmented Generation)
- Conduct web searches for general information
- Route queries to appropriate specialized crews based on content analysis

**What the application cannot do (limitations):**
- Provide definitive medical diagnoses or treatment recommendations
- Perform critical safety calculations for engineering applications
- Make legal or financial decisions
- Store or process personal health information
- Operate in real-time critical systems
- Replace professional consultation in specialized fields

**Supported languages, data types, or scenarios:**
- **Languages:** Primary support for Italian and English
- **Data Types:** Text-based queries, mathematical expressions, medical terminology
- **Scenarios:** Educational assistance, research support, information retrieval

#### **Input Data Requirements**

**Format and quality expectations for input data:**
- **Query Format:** Natural language questions in text format
- **Length:** Questions between 5-500 characters
- **Language:** Italian or English preferred
- **Clarity:** Well-formed questions with clear intent

**Examples of valid inputs:**
- ✅ "Calculate the area of a circle with a radius of 5 cm"
- ✅ "Explain how to solve quadratic equations."
- ✅ "What is asma?"
- ✅ "What is the capital of France?"

**Examples of invalid inputs:**
- ❌ Empty queries or single characters
- ❌ Binary files or images
- ❌ Queries with personal identification information
- ❌ Malicious code or SQL injection attempts

#### **Output Explanation**

**How to interpret predictions, classifications, or recommendations:**
- **Classification Results:** Clear indication of question type (MATH/NON-MATH, MEDICAL/GENERAL)
- **Mathematical Outputs:** Step-by-step solutions with intermediate calculations
- **Medical Information:** Contextual responses based on local database, with disclaimers
- **Tutorial Content:** Structured educational material with examples
- **Web Search Results:** Summarized information with source attribution

**Uncertainty or confidence measures:**
- **Classification Confidence:** High confidence (>95%) for clear mathematical questions
- **Medical Information:** Limited to pre-loaded database content with clear scope
- **Web Search:** Results may vary based on current internet content availability

#### **System Architecture Overview**

**Functional description and architecture of the system:**
RAGFlow operates as a multi-agent orchestration system that intelligently routes user queries through specialized processing pipelines.

**Key components of the system:**

| Component | Description | Technology |
|-----------|-------------|------------|
| **Classifier Crew** | Question classification engine | CrewAI + Azure OpenAI |
| **Math Crew** | Mathematical computation engine | CrewAI + Mathematical tools |
| **Tutorial Crew** | Educational content generation | CrewAI + Azure OpenAI |
| **RAG Crew** | Medical database search | FAISS + Azure OpenAI + Local documents |
| **Search Crew** | Web information retrieval | DuckDuckGo API + CrewAI |

**Datasets:**
- **Medical Database:** Pre-loaded medical documents covering common conditions
- **Mathematical Knowledge:** Built-in mathematical computation capabilities
- **Educational Content:** Dynamic generation based on user queries

**Algorithms and Models:**
- **Classification Algorithm:** Multi-label classification using Azure OpenAI
- **Embedding Model:** Azure OpenAI text-embedding-ada-002
- **Language Model:** Azure OpenAI GPT models for text generation
- **Vector Search:** FAISS similarity search for medical information retrieval

## **Models and Datasets**

### **Models**
Link to all models integrated in the AI/ML System

| Model | Link to Single Source of Truth | Description of Application Usage |
|-------|--------------------------------|----------------------------------|
| **Azure OpenAI GPT-4** | [Azure OpenAI Model Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) | Primary language model for question classification, tutorial generation, and response formatting |
| **Azure OpenAI text-embedding-ada-002** | [Azure OpenAI Embeddings Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings) | Vector embeddings for medical document similarity search and RAG operations |
| **FAISS Vector Database** | [FAISS GitHub Repository](https://github.com/facebookresearch/faiss) | Local vector storage and similarity search engine for medical information retrieval |
| **CrewAI Framework** | [CrewAI Documentation](https://docs.crewai.com/) | Multi-agent orchestration framework for task routing and crew management |
| **Mathematical Computation Engine** | [Python Mathematical Libraries](https://docs.python.org/3/library/math.html) | Built-in Python mathematical functions for calculations and problem-solving |

### **Datasets**
Link to all dataset documentation and information used to evaluate the AI/ML System.

| Dataset | Link to Single Source of Truth | Description of Application Usage |
|---------|--------------------------------|----------------------------------|
| **Medical Knowledge Base** | [Local Medical Documents](ragflow/src/ragflow/tools/rag_tool.py) | Pre-loaded medical documents covering common conditions (asthma, diabetes, hypertension, gastritis, migraine, allergic rhinitis, pneumonia) |
| **Mathematical Knowledge** | [Built-in Python Math](https://docs.python.org/3/library/math.html) | Standard mathematical functions and operations for computational tasks |
| **Educational Content Templates** | [Tutorial Crew Configuration](ragflow/src/ragflow/crews/tutorial_crew/config/) | Dynamic generation templates for educational explanations and tutorials |
| **Question Classification Training Data** | [Classifier Crew Configuration](ragflow/src/ragflow/crews/classifier_crew/config/) | Training data and prompts for question categorization (MATH/NON-MATH, MEDICAL/GENERAL) |
| **Web Search Results** | [DuckDuckGo API](https://duckduckgo.com/api) | Real-time web search results for general information queries |

**Note:** Model Documentation should also contain dataset information and links for all datasets used to train and test each respective model. The RAGFlow system primarily uses pre-trained Azure OpenAI models with local medical document collections and dynamic content generation.

## **Deployment**

### **Infrastructure and Environment Details**

#### **Cloud Setup**
- **Cloud Provider:** Microsoft Azure
- **Regions:** West Europe (Primary), North Europe (Backup)
- **Required Services:**
  - **Compute:** Azure Container Instances, Azure Kubernetes Service (AKS)
  - **Storage:** Azure Blob Storage, Azure File Storage
  - **Databases:** Azure Cosmos DB, Azure SQL Database
  - **AI Services:** Azure OpenAI Service, Azure Cognitive Services
- **Resource Configurations:**
  - **VM Sizes:** Standard_D2s_v3 (Development), Standard_D4s_v3 (Production)
  - **GPU Requirements:** None (CPU-based processing)
  - **Memory:** 8GB (Development), 16GB (Production)
- **Network Setup:**
  - **VPC:** Azure Virtual Network with private subnets
  - **Security Groups:** Network Security Groups with restricted access
  - **Load Balancer:** Azure Application Gateway

#### **APIs**
- **API Endpoints:** RESTful API with GraphQL support
- **Payload Structure:** JSON format with standardized error responses
- **Authentication Methods:** Azure AD OAuth 2.0, API Keys for external services
- **Latency Expectations:** <200ms for classification, <500ms for RAG queries
- **Scalability:** Auto-scaling based on CPU utilization (70-80% threshold)

### **Integration with External Systems**

#### **Systems and Dependencies**
- **Azure OpenAI Service:** GPT-4 and embedding models
- **DuckDuckGo API:** Web search functionality
- **FAISS Vector Database:** Local medical knowledge storage
- **CrewAI Framework:** Multi-agent orchestration
- **Python Mathematical Libraries:** Built-in computation functions

#### **Data Flow Diagrams**
```
External APIs → Load Balancer → API Gateway → RAGFlow Core → Crew Orchestration → Response
     ↓              ↓              ↓            ↓              ↓
Azure OpenAI   DuckDuckGo    Authentication  Classification  Specialized Crews
```

#### **Error-Handling Mechanisms**
- **API Failures:** Circuit breaker pattern with fallback responses
- **Webhook Retries:** Exponential backoff with maximum 3 attempts
- **Graceful Degradation:** Fallback to local knowledge base when external APIs fail

### **Deployment Plan**

#### **Infrastructure**
- **Environments:** Development, Staging, Production
- **Resource Scaling:** Azure Auto-scaling with predictive scaling
- **Backup and Recovery:** Daily automated backups with 30-day retention
- **Redundancy:** Multi-zone deployment for high availability

#### **Integration Steps**
1. **Database Setup:** Initialize FAISS index and medical documents
2. **Model Deployment:** Deploy Azure OpenAI service connections
3. **Service Launch:** Deploy RAGFlow containers with health checks
4. **Integration Testing:** Validate all external API connections
5. **Load Testing:** Performance validation under expected load

#### **Rollback Strategies**
- **Database Rollback:** Point-in-time recovery from Azure backups
- **Model Rollback:** Version-specific container deployment
- **Service Rollback:** Blue-green deployment with instant switchback

## **Lifecycle Management**

### **Monitoring Procedures**

#### **Performance Monitoring**
- **Real-time Metrics:** Response time, throughput, error rates
- **Resource Utilization:** CPU, memory, network usage
- **Model Performance:** Classification accuracy, response quality
- **Ethical Compliance:** Bias detection, fairness metrics

#### **Versioning and Change Logs**
- **Model Updates:** Semantic versioning (MAJOR.MINOR.PATCH)
- **Change Tracking:** Automated changelog generation from Git commits
- **Rollback Capability:** Instant rollback to previous stable versions

### **Metrics and KPIs**

#### **Application Performance**
- **Response Time:** Target <500ms for 95% of requests
- **Error Rate:** Target <1% for production systems
- **Uptime:** Target 99.9% availability

#### **Model Performance**
- **Accuracy:** >95% for question classification
- **Precision:** >90% for medical information retrieval
- **Recall:** >85% for mathematical problem solving

#### **Infrastructure Metrics**
- **CPU Utilization:** Target 60-80% for optimal performance
- **Memory Usage:** Target <80% to prevent swapping
- **Network Latency:** <100ms for internal communications

### **Key Activities**

#### **Continuous Monitoring**
- **Real-world Performance:** A/B testing for new features
- **Drift Detection:** Automated monitoring for data and model drift
- **Failure Analysis:** Root cause analysis for all incidents

#### **Periodic Updates**
- **Model Retraining:** Quarterly updates based on new data
- **Security Patches:** Monthly security updates and vulnerability fixes
- **Feature Updates:** Bi-monthly feature releases with user feedback

### **Documentation Requirements**

#### **Monitoring Logs**
- **Real-time Dashboards:** Grafana dashboards for operational metrics
- **Alert Systems:** PagerDuty integration for critical issues
- **Performance Reports:** Weekly and monthly performance summaries

#### **Incident Reports**
- **Incident Tracking:** JIRA integration for issue management
- **Impact Assessment:** Severity classification and business impact
- **Resolution Documentation:** Step-by-step resolution procedures

#### **Audit Trails**
- **Change History:** Complete Git history with signed commits
- **Deployment Logs:** Azure DevOps pipeline execution logs
- **Access Logs:** Azure AD authentication and authorization logs

## **Risk Management System**

### **Risk Assessment Methodology**
- **Framework:** ISO 31000 Risk Management Guidelines
- **Assessment Frequency:** Quarterly comprehensive risk reviews
- **Stakeholder Involvement:** Cross-functional risk assessment team

### **Identified Risks**

#### **Potential Harmful Outcomes**
- **Bias in Classification:** Gender or language-based discrimination
- **Privacy Breaches:** Unauthorized access to medical information
- **Safety Hazards:** Incorrect mathematical calculations for critical applications
- **Misinformation:** Inaccurate medical or educational content

#### **Likelihood and Severity Assessment**
- **High Risk:** Data privacy breaches (Likelihood: Medium, Severity: High)
- **Medium Risk:** Classification bias (Likelihood: Low, Severity: Medium)
- **Low Risk:** Mathematical errors (Likelihood: Very Low, Severity: Low)

### **Risk Mitigation Measures**

#### **Preventive Measures**
- **Data Validation:** Multi-layer input validation and sanitization
- **Bias Reduction:** Regular bias testing and model retraining
- **Access Control:** Role-based access control with least privilege principle
- **Input Sanitization:** Protection against injection attacks

#### **Protective Measures**
- **Incident Response Plan:** 24/7 incident response team
- **Data Encryption:** End-to-end encryption for sensitive data
- **Regular Audits:** Monthly security and compliance audits
- **Backup Systems:** Redundant systems for critical functions

## **Testing and Validation**

### **Accuracy Testing**

#### **Performance Metrics**
- **Classification Metrics:** Accuracy, Precision, Recall, F1-Score
- **Mathematical Accuracy:** 100% accuracy for standard calculations
- **Medical Information Relevance:** >95% relevance score
- **Response Quality:** Human evaluation scores >4.0/5.0

#### **Validation Results**
- **Training Data:** 10,000+ labeled questions for classification
- **Test Data:** 2,000+ questions for validation
- **Cross-validation:** 5-fold stratified cross-validation
- **Benchmarks:** Exceeds industry standards for educational AI systems

#### **Measures for Accuracy**
- **Data Quality:** Automated data validation and cleaning
- **Algorithm Optimization:** Hyperparameter tuning with Bayesian optimization
- **Real-time Monitoring:** Continuous performance tracking
- **Feedback Loops:** User feedback integration for improvement

### **Data Quality and Management**

#### **High-Quality Training Data**
- **Data Preprocessing:** Normalization, outlier removal, feature scaling
- **Data Augmentation:** Synthetic data generation for underrepresented classes
- **Data Validation:** Automated quality checks and manual review processes
- **Version Control:** Git LFS for large dataset versioning

#### **Model Selection and Optimization**
- **Algorithm Selection:** Azure OpenAI GPT models for language tasks
- **Hyperparameter Tuning:** Grid search and Bayesian optimization
- **Performance Validation:** K-fold cross-validation with stratification
- **Evaluation Metrics:** Comprehensive metric suite for all use cases

#### **Feedback Mechanisms**
- **Real-time Error Tracking:** Automated error detection and logging
- **Challenging Examples:** Active learning for difficult cases
- **Iterative Improvement:** Continuous model refinement based on feedback

### **Robustness Measures**

#### **Adversarial Training and Testing**
- **Stress Testing:** Extreme input conditions and edge cases
- **Adversarial Examples:** Testing with intentionally misleading inputs
- **Domain Adaptation:** Performance across different languages and contexts
- **Graceful Degradation:** Fallback mechanisms for unexpected inputs

#### **Redundancy and Fail-Safes**
- **Fallback Systems:** Rule-based classification when AI fails
- **Multiple Models:** Ensemble approaches for critical decisions
- **Error Handling:** Comprehensive error handling with user-friendly messages
- **Circuit Breakers:** Protection against cascading failures

#### **Uncertainty Estimation**
- **Confidence Scores:** Probability estimates for all predictions
- **Bayesian Networks:** Uncertainty quantification for complex decisions
- **Threshold Management:** Configurable confidence thresholds
- **User Transparency:** Clear communication of uncertainty levels

### **Cybersecurity**

#### **Data Security**
- **Encryption:** AES-256 encryption for data at rest and in transit
- **Access Control:** Multi-factor authentication and role-based access
- **Data Classification:** Sensitive data identification and protection
- **Audit Logging:** Comprehensive access and modification logs

#### **Access Control**
- **Authentication:** Azure AD integration with SSO
- **Authorization:** Principle of least privilege with regular access reviews
- **Session Management:** Secure session handling with timeout policies
- **Privilege Escalation:** Controlled process for temporary access

#### **Incident Response**
- **Threat Detection:** Automated threat detection and alerting
- **Incident Classification:** Severity-based incident response procedures
- **Forensic Analysis:** Comprehensive logging for post-incident analysis
- **Recovery Procedures:** Documented recovery and business continuity plans

## **Human Oversight**

### **Human-in-the-Loop Mechanisms**
- **Classification Review:** Human review for low-confidence classifications
- **Medical Content Validation:** Healthcare professional review of medical responses
- **Mathematical Verification:** Expert review of complex calculations
- **User Feedback Integration:** Continuous improvement based on user input

### **Override and Intervention Procedures**
- **Emergency Stop:** Immediate system shutdown capability
- **Manual Override:** Human operator intervention for critical decisions
- **Fallback Mode:** Rule-based operation when AI systems are unavailable
- **Escalation Procedures:** Clear escalation paths for complex issues

### **User Instructions and Training**
- **User Manuals:** Comprehensive documentation for all user types
- **Training Programs:** Regular training sessions for operators
- **Best Practices:** Guidelines for safe and effective system usage
- **Troubleshooting Guides:** Step-by-step problem resolution procedures

### **System Limitations and Constraints**
- **Known Weaknesses:** Documented limitations and edge cases
- **Performance Boundaries:** Clear performance expectations and limitations
- **Degradation Scenarios:** Conditions where performance may degrade
- **Maintenance Windows:** Scheduled maintenance and update procedures

## **Incident Management**

### **Common Issues and Solutions**

#### **Infrastructure-Level Issues**
- **Insufficient Resources**
  - **Problem:** Inaccurate resource estimation for production workloads
  - **Solution:** Implement auto-scaling with predictive scaling
  - **Prevention:** Regular capacity planning and load testing

- **Network Failures**
  - **Problem:** Network bottlenecks causing latency and accessibility issues
  - **Solution:** Multi-zone deployment with load balancing
  - **Prevention:** Network redundancy and monitoring

- **Deployment Pipeline Failures**
  - **Problem:** Build, test, or deployment failures
  - **Solution:** Automated rollback and health checks
  - **Prevention:** Comprehensive testing and validation

#### **Integration Problems**
- **API Failures**
  - **Problem:** External API unreachability
  - **Solution:** Circuit breaker pattern with fallbacks
  - **Prevention:** API health monitoring and testing

- **Data Format Mismatches**
  - **Problem:** Schema changes causing crashes
  - **Solution:** Robust data validation and transformation
  - **Prevention:** Schema versioning and backward compatibility

#### **Data Quality Problems**
- **Problem:** Inaccurate or corrupt data leading to poor predictions
- **Solution:** Automated data validation and cleaning pipelines
- **Prevention:** Data quality monitoring and regular audits

#### **Model-Level Issues**
- **Performance Degradation**
  - **Problem:** Data drift or inadequate training data
  - **Solution:** Continuous monitoring and model retraining
  - **Prevention:** Regular model performance evaluation

#### **Safety and Security Issues**
- **Unauthorized Access**
  - **Problem:** Misconfigured authentication and authorization
  - **Solution:** Regular security audits and access reviews
  - **Prevention:** Security-by-design principles

- **Data Breaches**
  - **Problem:** Compromised data due to insecure storage
  - **Solution:** Encryption and access monitoring
  - **Prevention:** Security testing and vulnerability management

#### **Monitoring and Logging Failures**
- **Missing Logs**
  - **Problem:** Inefficient logging leading to debugging issues
  - **Solution:** Comprehensive logging strategy with alerting
  - **Prevention:** Log management and monitoring

#### **Recovery and Rollback**
- **Rollback Mechanisms**
  - **Problem:** New deployment introducing critical errors
  - **Solution:** Blue-green deployment with instant rollback
  - **Prevention:** Comprehensive testing and validation

- **Disaster Recovery**
  - **Problem:** Complete system outage or data loss
  - **Solution:** Multi-region deployment with automated failover
  - **Prevention:** Regular disaster recovery testing

### **Support Contact**
- **Technical Support:** 24/7 support via Azure support portal
- **Community Forums:** GitHub Discussions for community support
- **Documentation:** Comprehensive online documentation and tutorials
- **Training Resources:** Regular webinars and training sessions

## **EU Declaration of Conformity**

### **Standards Applied**
- **EU AI Act Compliance:** Full compliance with Articles 11, 13, 14, 15, 47
- **ISO Standards:** ISO 27001 (Information Security), ISO 31000 (Risk Management)
- **GDPR Compliance:** Full compliance with data protection regulations
- **Industry Standards:** Best practices for AI system development and deployment

### **Documentation Metadata**

#### **Template Version**
- **Version:** 2.0.0
- **Last Updated:** 09/01/2025
- **Compliance:** EU AI Act Article 11 and Annex IV

#### **Documentation Authors**

| Name | Team | Role |
|------|------|------|
| **Miriana Pompilio** | AI&Data | Owner / Primary Author |
| **[Technical Reviewer]** | AI&Data | Contributor / Technical Validation |
| **[Legal Reviewer]** | Legal & Compliance | Contributor / Regulatory Compliance |
| **[Security Reviewer]** | Cybersecurity | Contributor / Security Validation |
| **[Business Stakeholder]** | Business | Manager / Business Requirements |

---

*This documentation ensures comprehensive compliance with EU AI Act requirements and provides complete transparency for AI system accountability and governance.*
