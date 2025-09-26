# Setup Guide

## Step-by-Step Installation

### 1. Install Ollama
\\\ash
# Download and install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the Mistral model
ollama pull mistral

# Start Ollama service
ollama serve
\\\

### 2. Setup Python Environment
\\\ash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
\\\

### 3. Configure Environment
Create \.env\ file in backend folder:
\\\nv
SE_RANKING_API_KEY=your_api_key_here
\\\

### 4. Run Application
\\\ash
python app.py
\\\

### 5. Access Frontend
Open \../frontend/simple-ui.html\ in your browser.

## Troubleshooting
- **Ollama connection issues**: Ensure \ollama serve\ is running
- **Port conflicts**: Change port in \pp.py\ if 5000 is busy
- **API errors**: Check SE Ranking API key validity
