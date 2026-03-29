from typing import List, Dict
from finsaarthi.tools.financial_calc import compare_tax_regimes
from finsaarthi.rag.knowledge_base import FinSaarthiKnowledgeBase

class TaxAgent:
    def __init__(self, kb: FinSaarthiKnowledgeBase):
        self.kb = kb

    def analyze_tax_situation(self, user_profile: Dict) -> Dict:
        """Analyze user salary and provide tax optimization tips."""
        gross_salary = user_profile.get('gross_salary', 0)
        deductions_80c = user_profile.get('deductions_80c', 0)
        hra = user_profile.get('hra', 0)
        nps = user_profile.get('nps', 0)
        medical = user_profile.get('medical', 0)

        # 1. Run regime comparison
        comparison = compare_tax_regimes(gross_salary, deductions_80c, hra, nps, medical)

        # 2. Query Knowledge Base for specific advice (RAG)
        query = f"Tax deductions for salary {gross_salary} with 80C {deductions_80c}"
        rag_context = self.kb.query(query, k=2)
        
        advice = [doc.page_content for doc in rag_context]
        if not advice:
            advice = ["Consider maximizing 80C (up to 1.5L) and NPS (up to 50k) for better savings."]

        return {
            "comparison": comparison,
            "advice": advice,
            "status": "Tax analysis complete."
        }

if __name__ == "__main__":
    # Placeholder for local testing
    pass
