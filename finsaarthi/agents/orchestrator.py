from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from finsaarthi.agents.tax_agent import TaxAgent
from finsaarthi.agents.portfolio_agent import PortfolioAgent
from finsaarthi.agents.fire_agent import FIREAgent
from finsaarthi.agents.couple_agent import CoupleAgent
from finsaarthi.rag.knowledge_base import FinSaarthiKnowledgeBase

class FinancialState(TypedDict):
    user_input: str
    intent: str
    user_profile: Dict
    agent_results: Dict
    audit_log: List[Dict]
    final_response: str

class FinSaarthiOrchestrator:
    def __init__(self, kb: FinSaarthiKnowledgeBase):
        self.kb = kb
        self.tax_agent = TaxAgent(kb)
        self.portfolio_agent = PortfolioAgent()
        self.fire_agent = FIREAgent()
        self.couple_agent = CoupleAgent()
        self.workflow = self._build_workflow()

    def _build_workflow(self):
        workflow = StateGraph(FinancialState)
        
        # Define nodes
        workflow.add_node("classify_intent", self.classify_intent_node)
        workflow.add_node("tax_agent", self.tax_agent_node)
        workflow.add_node("portfolio_agent", self.portfolio_agent_node)
        workflow.add_node("fire_agent", self.fire_agent_node)
        workflow.add_node("couple_agent", self.couple_agent_node)
        workflow.add_node("synthesize", self.synthesize_response_node)
        
        # Define edges
        workflow.set_entry_point("classify_intent")
        workflow.add_conditional_edges(
            "classify_intent",
            self.route_to_agent,
            {
                "tax": "tax_agent",
                "portfolio": "portfolio_agent",
                "fire": "fire_agent",
                "couple": "couple_agent"
            }
        )
        workflow.add_edge("tax_agent", "synthesize")
        workflow.add_edge("portfolio_agent", "synthesize")
        workflow.add_edge("fire_agent", "synthesize")
        workflow.add_edge("couple_agent", "synthesize")
        workflow.add_edge("synthesize", END)
        
        return workflow.compile()

    def classify_intent_node(self, state: FinancialState):
        """Simple intent classification (to be replaced with LLM)."""
        text = state['user_input'].lower()
        if "tax" in text: intent = "tax"
        elif "portfolio" in text or "fund" in text: intent = "portfolio"
        elif "retire" in text or "fire" in text: intent = "fire"
        elif "couple" in text or "partner" in text: intent = "couple"
        else: intent = "tax" # Default
        return {"intent": intent}

    def route_to_agent(self, state: FinancialState):
        return state['intent']

    def tax_agent_node(self, state: FinancialState):
        result = self.tax_agent.analyze_tax_situation(state['user_profile'])
        return {"agent_results": {"tax": result}}

    def portfolio_agent_node(self, state: FinancialState):
        result = self.portfolio_agent.analyze_cams_pdf(state['user_profile'].get('pdf_path', ''))
        return {"agent_results": {"portfolio": result}}

    def fire_agent_node(self, state: FinancialState):
        result = self.fire_agent.plan_fire_path(state['user_profile'])
        return {"agent_results": {"fire": result}}

    def couple_agent_node(self, state: FinancialState):
        result = self.couple_agent.optimize_household_finance(
            state['user_profile'].get('partner_1', {}),
            state['user_profile'].get('partner_2', {})
        )
        return {"agent_results": {"couple": result}}

    def synthesize_response_node(self, state: FinancialState):
        """Synthesize agent results into a final response."""
        intent = state['intent']
        result = state['agent_results'].get(intent, {})
        response = f"Based on my analysis: {result.get('status', 'Analysis complete.')}"
        return {"final_response": response}

    def run(self, user_input: str, user_profile: Dict):
        initial_state = {
            "user_input": user_input,
            "user_profile": user_profile,
            "agent_results": {},
            "audit_log": [],
            "final_response": ""
        }
        return self.workflow.invoke(initial_state)

if __name__ == "__main__":
    pass
