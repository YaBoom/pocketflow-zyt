import sys
sys.path.insert(0, '.')

from pocketflow import Node
from config import call_llm

def gpt_call(prompt: str, model: str = None) -> str:
    """Call LLM API using config."""
    return call_llm(prompt, model)


class RequirementAnalyzer(Node):
    """Analyze user requirement and break into actionable steps."""
    
    def prep(self, shared):
        """Get requirement from shared state."""
        return shared.get("user_requirement", "")
    
    def exec(self, prep_res):
        """Call GPT to analyze requirement."""
        prompt = f"""
        Analyze the following requirement and break it into 3-5 concrete steps:
        
        Requirement: {prep_res}
        
        Output format: One step per line, numbered.
        """
        return gpt_call(prompt)
    
    def post(self, shared, prep_res, exec_res):
        """Parse steps and store in shared state."""
        # Parse the steps (simple parsing for demo)
        lines = [line.strip() for line in exec_res.strip().split('\\n') if line.strip()]
        shared["steps"] = lines
        shared["raw_analysis"] = exec_res
        return "default"
