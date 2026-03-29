# FinSaarthi — India's First Agentic Financial Life OS

FinSaarthi is an AI-powered multi-agent financial intelligence platform that acts as a personal CFO for every Indian. It transforms raw financial data into personalized, actionable roadmaps across savings, investments, tax, insurance, and retirement planning.

## 🚀 Key Features
- **MF Portfolio X-Ray**: Instant analysis of mutual fund portfolios via CAMS/KFintech statements.
- **FIRE Path Planner**: Month-by-month SIP roadmap to achieve financial independence.
- **Tax Wizard**: AI-driven tax optimization and regime comparison.
- **Couple's Money Planner**: Dual-income optimization for household financial efficiency.

## 🛠️ Tech Stack
- **AI Framework**: LangGraph (Multi-agent orchestration).
- **LLM**: Google Gemini 1.5 Pro.
- **Vector DB**: ChromaDB (RAG for financial regulations).
- **Backend**: FastAPI.
- **Frontend**: Streamlit.

## 📁 Project Structure
- `finsaarthi/agents/`: Specialized AI agents (Portfolio, FIRE, Tax, Couple).
- `finsaarthi/tools/`: Core financial calculation engines.
- `finsaarthi/rag/`: RAG pipeline and financial knowledge base.
- `app.py`: Main Streamlit application.
- `api.py`: FastAPI backend.

## 🚦 Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your `GOOGLE_API_KEY` in a `.env` file.
4. Run the app: `streamlit run app.py`

---
*Created for ET AI Hackathon 2026*
