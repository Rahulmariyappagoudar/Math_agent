# AI Math Mentor

AI Math Mentor is a multi-agent system that helps students solve
mathematics problems from JEE-style exams. The system accepts **text,
image, or audio input**, processes the question through specialized AI
agents, retrieves relevant mathematical knowledge using **RAG**,
verifies the solution, and produces a clear step-by-step explanation.

------------------------------------------------------------------------

# Features

• Solve math problems from **text input**\
• Solve math problems from **images using OCR**\
• Solve math problems from **audio using speech-to-text**\
• Multi-agent reasoning pipeline\
• Retrieval-Augmented Generation (RAG) for mathematical knowledge\
• Verification using symbolic math and LLM critic\
• Student-friendly explanations\
• Feedback system for continuous learning

------------------------------------------------------------------------

# System Architecture

The system follows a **multi-agent architecture**.

User Input │ ├── Text ├── Image (OCR) └── Audio (Speech-to-Text) │ ▼
Parser Agent │ ▼ Intent Router Agent │ ▼ Retriever (RAG) │ ▼ Solver
Agent │ ▼ Verifier / Critic Agent │ ▼ Explainer / Tutor Agent │ ▼
Human-in-the-Loop (HITL) │ ▼ Final Answer + Explanation

------------------------------------------------------------------------

# Agents

## Parser Agent

Converts raw user input into a structured problem.

Example output:

{ "problem_text": "Find derivative of x\^2 + 3x", "topic": "calculus",
"variables": \["x"\], "constraints": \[\] }

------------------------------------------------------------------------

## Intent Router Agent

Identifies the math topic and routes the problem to the correct solver
strategy.

Examples:

• calculus_solver\
• algebra_solver\
• trigonometry_solver

------------------------------------------------------------------------

## Solver Agent

Solves the problem using:

• Retrieved mathematical rules\
• LLM reasoning\
• Optional mathematical tools

------------------------------------------------------------------------

## Verifier / Critic Agent

Checks:

• mathematical correctness\
• domain constraints\
• edge cases\
• symbolic verification using **SymPy**

If uncertain → triggers **Human-in-the-Loop (HITL)**.

------------------------------------------------------------------------

## Explainer / Tutor Agent

Produces a **clear step-by-step explanation** suitable for students.

------------------------------------------------------------------------

# RAG Pipeline

The system uses Retrieval-Augmented Generation.

### Knowledge Base

A curated collection of math documents including:

• derivative rules\
• integration rules\
• algebra identities\
• trigonometric identities\
• common math mistakes\
• domain constraints

### Pipeline

Documents\
↓\
Chunking\
↓\
Embeddings\
↓\
Vector Database (Chroma)\
↓\
Top-k Retrieval\
↓\
Context for Solver Agent

The UI displays retrieved sources to ensure transparency.

------------------------------------------------------------------------

# Project Structure

Math_agent/

├── agents/\
│ ├── parser_agent.py\
│ ├── router_agent.py\
│ ├── solver_agent.py\
│ ├── verifier_agent.py\
│ ├── explainer_agent.py\
│ └── hitl_agent.py

├── rag/\
│ ├── retriever.py\
│ └── build_vector.py

├── tools/\
│ ├── ocr.py\
│ └── speech_to_text.py

├── memory/\
│ └── memory_store.py

├── knowledge_base/\
│ ├── derivative_rules.txt\
│ ├── algebra_identities.txt\
│ ├── trigonometry_rules.txt

├── app.py\
├── run.sh\
└── README.md

------------------------------------------------------------------------

# Installation

## 1. Clone the repository

git clone `<repo_url>`{=html}\
cd Math_agent

------------------------------------------------------------------------

## 2. Create virtual environment

python -m venv .venv\
source .venv/bin/activate

------------------------------------------------------------------------

## 3. Install dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 4. Install Ollama

Download from:

https://ollama.com

Then pull the model:

ollama pull qwen2.5:7b

------------------------------------------------------------------------

## 5. Build the vector database

python rag/build_vector.py

------------------------------------------------------------------------

# Running the Application

Run using the helper script:

./run.sh

or directly:

streamlit run app.py

The UI will open in the browser.

------------------------------------------------------------------------

# Example Usage

### Text Input

Find derivative of x\^2 + 3x

### Image Input

Upload a photo of a handwritten or textbook math problem.

### Audio Input

Speak a math question such as:

"What is the derivative of x squared plus three x"

------------------------------------------------------------------------

# Example Output

Derivative of x\^2 + 3x

Step 1: Apply power rule\
d/dx(x\^2) = 2x

Step 2: Differentiate 3x\
d/dx(3x) = 3

Final Answer:\
2x + 3

------------------------------------------------------------------------

# Technologies Used

• Python\
• Streamlit\
• LangChain\
• Ollama\
• ChromaDB\
• SymPy\
• OCR\
• Speech-to-Text

------------------------------------------------------------------------

# Future Improvements

• Support more math topics (geometry, probability)\
• Step verification with symbolic solvers\
• Interactive tutoring mode\
• Performance optimization\
• Distributed agent orchestration

------------------------------------------------------------------------

# Author

Rahul Mariyappagoudar
