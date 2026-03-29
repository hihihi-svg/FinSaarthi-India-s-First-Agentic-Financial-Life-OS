from typing import List, Dict
from finsaarthi.tools.financial_calc import compare_tax_regimes, calculate_sip_for_goal

class CoupleAgent:
    def __init__(self):
        pass

    def optimize_household_finance(self, partner_1: Dict, partner_2: Dict) -> Dict:
        """Optimize tax and investments across dual incomes."""
        # 1. Individual tax analysis
        p1_tax = compare_tax_regimes(
            partner_1.get('salary', 0),
            partner_1.get('80c', 0),
            partner_1.get('hra', 0),
            partner_1.get('nps', 0),
            partner_1.get('medical', 0)
        )
        p2_tax = compare_tax_regimes(
            partner_2.get('salary', 0),
            partner_2.get('80c', 0),
            partner_2.get('hra', 0),
            partner_2.get('nps', 0),
            partner_2.get('medical', 0)
        )

        # 2. Joint optimization logic (simplified)
        # Suggest shifting HRA to the partner with higher bracket if applicable
        joint_savings = 0
        recommendation = "Maintain current splits."

        if partner_1.get('salary', 0) > partner_2.get('salary', 0):
            recommendation = f"Consider maximizing {partner_1.get('name', 'Partner 1')}'s HRA if rent is shared."
        
        return {
            "partner_1_status": p1_tax,
            "partner_2_status": p2_tax,
            "joint_recommendation": recommendation,
            "status": "Couple optimization analysis complete."
        }

if __name__ == "__main__":
    pass
