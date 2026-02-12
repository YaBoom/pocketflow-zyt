import sys
sys.path.insert(0, '.')

from pocketflow import Node, Flow
from config import call_llm

def gpt_call(prompt: str, model: str = None) -> str:
    """Call LLM API using config."""
    return call_llm(prompt, model)


class GPTNode(Node):
    """Basic GPT calling node."""
    
    def prep(self, shared):
        return shared.get("user_input", "")
    
    def exec(self, prep_res):
        if not prep_res:
            return "No input provided"
        return gpt_call(prep_res)
    
    def post(self, shared, prep_res, exec_res):
        shared["gpt_response"] = exec_res
        return "default"


class EchoNode(Node):
    """Simple echo node for testing."""
    
    def exec(self, prep_res):
        return f"Echo: {prep_res}"
    
    def post(self, shared, prep_res, exec_res):
        shared["echo"] = exec_res
        return "default"


def main():
    """Run basic chatbot example."""
    print("🤖 PocketFlow Basic Chatbot Demo")
    print("-" * 40)
    
    # Create nodes
    gpt = GPTNode()
    echo = EchoNode()
    
    # Chain them: gpt -> echo
    gpt >> echo
    
    # Create flow
    flow = Flow(gpt)
    
    # Run
    shared = {"user_input": "Hello, PocketFlow!"}
    result = flow.run(shared)
    
    print(f"Input: {shared['user_input']}")
    print(f"GPT Response: {result.get('gpt_response')}")
    print(f"Echo: {result.get('echo')}")


if __name__ == "__main__":
    main()
