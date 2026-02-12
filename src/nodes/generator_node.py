import sys
sys.path.insert(0, '.')

from pocketflow import Node
from config import call_llm

def gpt_call(prompt: str, model: str = None) -> str:
    """Call LLM API using config."""
    return call_llm(prompt, model)


class CodeGenerator(Node):
    """Generate PocketFlow code based on analyzed steps."""
    
    def prep(self, shared):
        """Get steps from shared state."""
        return shared.get("steps", [])
    
    def exec(self, prep_res):
        """Generate code using GPT."""
        if not prep_res:
            return "Error: No steps provided"
        
        steps_text = "\\n".join(prep_res)
        prompt = f"""
        Generate Python code using the PocketFlow framework based on these steps:
        
        {steps_text}
        
        Requirements:
        - Use Node and Flow from pocketflow
        - Create a Node class for each step
        - Include prep, exec, and post methods
        - Add proper error handling (TODO)
        
        Output: Complete, runnable Python code.
        """
        
        return gpt_call(prompt)
    
    def post(self, shared, prep_res, exec_res):
        """Store generated code."""
        shared["generated_code"] = exec_res
        # TODO: Add code validation
        return "default"
