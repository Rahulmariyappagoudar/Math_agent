#!/bin/bash

echo "Starting AI Math Mentor..."

# Activate virtual environment
source .venv/bin/activate

# Start Ollama if not running
if ! pgrep -x "ollama" > /dev/null
then
    echo "Starting Ollama..."
    ollama serve &
    sleep 3
fi

# Run Streamlit app
echo "Launching Streamlit..."
streamlit run app.py
