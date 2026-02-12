import sys
sys.path.insert(0, '.')

from pocketflow import Node


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
        
        # TODO: Replace with actual GPT call
        # Mock response
        code = '''
from pocketflow import Node, Flow

class Step1Node(Node):
    def exec(self, prep_res):
        # TODO: Implement step 1
        return "Step 1 done"

class Step2Node(Node):
    def exec(self, prep_res):
        # TODO: Implement step 2  
        return "Step 2 done"

# Create flow
step1 = Step1Node()
step2 = Step2Node()
step1 >> step2
flow = Flow(step1)
        '''
        return code.strip()
    
    def post(self, shared, prep_res, exec_res):
        """Store generated code."""
        shared["generated_code"] = exec_res
        # TODO: Add code validation
        return "default"
