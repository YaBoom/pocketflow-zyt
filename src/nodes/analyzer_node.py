import sys
sys.path.insert(0, '.')

from pocketflow import Node


class RequirementAnalyzer(Node):
    """Analyze user requirement and break into actionable steps."""
    
    def prep(self, shared):
        """Get requirement from shared state."""
        return shared.get("user_requirement", "")
    
    def exec(self, prep_res):
        """Call GPT to analyze requirement."""
        # TODO: Replace with actual GPT call
        # This is mock logic for demonstration
        prompt = f"""
        Analyze the following requirement and break it into 3-5 concrete steps:
        
        Requirement: {prep_res}
        
        Output format: One step per line, numbered.
        """
        # Mock response
        return """
        1. Parse and validate user input
        2. Query external API for data
        3. Process and format the results
        4. Deliver output to user
        """
    
    def post(self, shared, prep_res, exec_res):
        """Parse steps and store in shared state."""
        # Parse the steps (simple parsing for demo)
        lines = [line.strip() for line in exec_res.strip().split('\\n') if line.strip()]
        shared["steps"] = lines
        shared["raw_analysis"] = exec_res
        return "default"
