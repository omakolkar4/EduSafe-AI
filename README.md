
# EduSafe AI – Domain-Specific Educational Assistant with Safety Controls

EduSafe AI is a local AI-powered educational assistant designed to help students with academic questions while applying multiple safety controls to protect privacy and prevent malicious instructions.

The application uses the Qwen 2.5 3B language model through Ollama and provides an interactive web interface built with Streamlit.

## Features

- **Educational Assistance:** Explains academic concepts in simple language.
- **Prompt Injection Protection:** Detects and blocks suspicious instructions.
- **Privacy Protection:** Blocks requests for sensitive student information.
- **Study Material Validation:** Checks supplied study material for malicious instructions.
- **Output Safety:** Detects basic email and phone-number-like patterns in generated responses.
- **Activity Logging:** Records security events without storing student questions.
- **Local AI Processing:** Uses a locally hosted Ollama model.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| User Interface | Streamlit |
| Language Model | Qwen 2.5 3B |
| Model Runtime | Ollama |
| AI Integration | LangChain |
| Safety Controls | Python Regex |
| Logging | Python Logging |

## Project Architecture

```text
EduSafe AI
    |
    v
Streamlit User Interface
    |
    v
Educational AI Agent
    |
    +--> Input Guard
    |
    +--> Privacy Guard
    |
    +--> Study Content Guard
    |
    +--> Local Qwen 2.5 3B Model
    |
    +--> Output Guard
    |
    v
Safe Educational Response
    |
    v
Activity Logging
```

## Project Structure

```text
EduSafe_AI/
|
|-- app.py
|-- agent.py
|-- requirements.txt
|-- README.md
|
|-- safety/
|   |-- input_guard.py
|   |-- privacy_guard.py
|   |-- content_guard.py
|   |-- output_guard.py
|
|-- data/
|   |-- sample_students.json
|
|-- logs/
|   |-- activity.log
|
|-- .gitignore
```

## Safety Mechanisms

### 1. Input Guard
Detects suspicious user instructions, including attempts to override previous instructions or reveal system prompts.

### 2. Privacy Guard
Blocks requests that attempt to access sensitive student information.

### 3. Content Guard
Checks supplied study material for malicious instructions before sending it to the AI model.

### 4. Output Guard
Checks generated responses for basic email-like and 10-digit phone-number-like patterns.

### 5. Activity Logging
Records successful processing and security events without logging the actual student questions.

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Ollama
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/EduSafe-AI.git
cd EduSafe-AI
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download the AI Model

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running before launching the application.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Testing

The following safety scenarios have been tested:

| Test Scenario | Expected Result | Status |
|---|---|---|
| Normal academic question | Educational response generated | Passed |
| Prompt injection attempt | Request blocked | Passed |
| Private student data request | Request blocked | Passed |
| Malicious study material | Content blocked | Passed |
| Output safety unit test | Email/phone-like data detected | Passed |

Note: The output guard result above was verified through a direct unit test, not yet through an end-to-end generated response.

## Limitations

- Safety checks use basic regular-expression patterns and are not comprehensive security guarantees.
- Output checking covers simple email-like and 10-digit phone-number-like patterns.
- The local model may occasionally generate inaccurate information.
- The application requires Ollama and the downloaded model to be available locally.

## Privacy Note

EduSafe AI uses a locally hosted Ollama model. Prompts are sent to the local Ollama service. This does not guarantee that every component of the overall computer environment is isolated from external services.

The sample student dataset is intended for synthetic demonstration data only. Do not use real student personal information.

## Future Enhancements

- Improved prompt injection detection.
- More advanced privacy detection.
- User authentication and role-based access.
- Academic document upload and processing.
- Enhanced security testing and evaluation.

## Author

**Om Akolkar**

B.Tech – Computer Science and Engineering  
Specialization: Artificial Intelligence and Analytics

MIT ADT University, Pune

---

*EduSafe AI – Making AI-powered educational assistance safer and more responsible.*
