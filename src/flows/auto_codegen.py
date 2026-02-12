import sys
sys.path.insert(0, '.')

from pocketflow import Node, Flow
from config import call_llm

def gpt_call(prompt: str, model: str = None) -> str:
    """Call LLM API using config."""
    return call_llm(prompt, model)


class RequirementAnalyzer(Node):
    """Analyze user requirement and break into steps."""
    
    def prep(self, shared):
        return shared.get("user_requirement", "")
    
    def exec(self, prep_res):
        prompt = f"""
        Analyze this requirement and break into 3-5 steps:
        {prep_res}
        
        Output format: one step per line
        """
        return gpt_call(prompt)
    
    def post(self, shared, prep_res, exec_res):
        lines = [line.strip() for line in exec_res.strip().split('\\n') if line.strip()]
        shared["steps"] = lines
        shared["raw_analysis"] = exec_res
        return "default"


class CodeGenerator(Node):
    """Generate PocketFlow code based on steps."""
    
    def prep(self, shared):
        return shared.get("steps", [])
    
    def exec(self, prep_res):
        steps_text = "\\n".join(prep_res)
        prompt = f"""
        Generate PocketFlow code for these steps:
        {steps_text}
        """
        return gpt_call(prompt)
    
    def post(self, shared, prep_res, exec_res):
        shared["generated_code"] = exec_res
        return "default"


class ContextRefiner(Node):
    """Refine context between nodes (my addition)."""
    
    def prep(self, shared):
        return shared.get("steps", [])
    
    def exec(self, prep_res):
        # Format steps more clearly
        formatted = "Task list:\\n"
        for i, step in enumerate(prep_res, 1):
            formatted += f"{i}. {step}\\n"
        return formatted
    
    def post(self, shared, prep_res, exec_res):
        shared["refined_context"] = exec_res
        return "default"


def main():
    """Run auto code generation demo."""
    print("🤖 Auto Code Generation with PocketFlow")
    print("-" * 40)
    
    # Create nodes
    analyzer = RequirementAnalyzer()
    refiner = ContextRefiner()  # My addition to improve context
    generator = CodeGenerator()
    
    # Chain: analyzer -> refiner -> generator
    analyzer >> refiner >> generator
    
    # Create flow
    flow = Flow(analyzer)
    
    # Run
    shared = {
        "user_requirement": "Build a bot that checks weather and sends email"
    }
    result = flow.run(shared)
    
    print(f"Requirement: {shared['user_requirement']}")
    print(f"\\nSteps identified:")
    for step in result.get('steps', []):
        print(f"  - {step}")
    print(f"\\nGenerated code preview:")
    print(result.get('generated_code', 'None'))
    print(f"\\nRefined context:")
    print(result.get('refined_context', 'None'))


if __name__ == "__main__":
    main()
