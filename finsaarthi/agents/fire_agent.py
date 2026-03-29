from typing import List, Dict
from finsaarthi.tools.financial_calc import calculate_sip_for_goal

class FIREAgent:
    def __init__(self):
        pass

    def plan_fire_path(self, user_profile: Dict) -> Dict:
        """Calculate the roadmap to Financial Independence."""
        target_corpus = user_profile.get('target_corpus', 10000000) # Default 1Cr
        years = user_profile.get('retirement_years', 20)
        expected_return = user_profile.get('expected_return', 0.12)
        current_savings = user_profile.get('current_savings', 0)

        sip_needed = calculate_sip_for_goal(target_corpus, years, expected_return, current_savings)

        return {
            "sip_needed": sip_needed,
            "plan": f"To reach ₹{target_corpus/1e7}Cr in {years} years, you need a monthly SIP of ₹{sip_needed}.",
            "status": "FIRE roadmap calculated successfully."
        }

if __name__ == "__main__":
    pass
