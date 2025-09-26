# 🔍 SEO Keyword AI Agent

An AI-powered SEO keyword research tool that generates 50 high-opportunity keywords from any seed keyword, sorted by low competition and high search volume.

## 🚀 Features

- **AI-Powered Expansion**: Uses Ollama AI to generate relevant keyword variations
- **Real SEO Data**: Integrates with SE Ranking API for accurate metrics
- **Smart Scoring**: Opportunity-based ranking algorithm
- **N8N Automation**: Ready-to-use workflow automation
- **Professional UI**: Clean, responsive interface

## 📋 Quick Start

### Prerequisites
- Python 3.8+
- Ollama (with Mistral model)
- SE Ranking API account (optional)

### Installation
\\\ash
git clone https://github.com/yourusername/seo-keyword-ai-agent.git
cd seo-keyword-ai-agent/backend

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama
ollama serve

# Run application
python app.py
\\\

### Usage
1. Open \rontend/simple-ui.html\ in your browser
2. Enter a seed keyword (e.g., \
digital
marketing\)
3. Click \Generate
Keywords\
4. Get 50 sorted keyword opportunities

## 📊 Example Output
- **Input**: \digital
marketing\
- **Output**: 50 keywords with volume, competition, opportunity scores
- **Top Result**: \digital
marketing
for
beginners\ - 1200 searches, 15% competition

## 🛠️ Technology Stack
- **Backend**: Python Flask
- **AI**: Ollama (Mistral model)
- **SEO Data**: SE Ranking API
- **Frontend**: HTML/CSS/JavaScript
- **Automation**: N8N workflows

## 📁 Project Structure
\\\
seo-keyword-ai-agent/
├── backend/          # Flask API server
├── frontend/         # Web interface
├── n8n-workflows/    # Automation files
├── docs/            # Documentation
└── examples/        # Sample outputs
\\\

## 🔧 API Endpoints
- \POST /generate-keywords\ - Generate keywords
- \GET /health\ - Health check
- \POST /n8n-webhook\ - N8N integration

## 📄 License
MIT License - see LICENSE file for details.

## 🤝 Contributing
Contributions welcome! Please feel free to submit issues and pull requests.

---
**Built with ❤️ for SEO professionals and content creators**
