import sys
sys.path.insert(0, '.')

from pocketflow import Node

# Mock GPT call - replace with actual OpenAI API
def gpt_call(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Call GPT API."""
    # TODO: Replace with actual OpenAI API call
    import os
    # api_key = os.getenv("OPENAI_API_KEY")
    # ...
    return f"[MOCK RESPONSE] {prompt[:50]}..."


class GPTNode(Node):
    """Generic GPT calling node."""
    
    def __init__(self, system_prompt: str = ""):
        self.system_prompt = system_prompt
        super().__init__()
    
    def prep(self, shared):
        """Extract input from shared state."""
        return shared.get("user_input", "")
    
    def exec(self, prep_res):
        """Call GPT API."""
        try:
            if not prep_res:
                return "Error: No input provided"
            return gpt_call(prep_res)
        except Exception as e:
            # TODO: Add proper error handling
            return f"Error: {str(e)}"
    
    def post(self, shared, prep_res, exec_res):
        """Store result in shared state."""
        shared["gpt_response"] = exec_res
        shared["last_prompt"] = prep_res
        return "default"
