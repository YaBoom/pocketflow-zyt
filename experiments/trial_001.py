# Trial 001: Basic Node Testing
# Status: Works but error handling is missing

import sys
sys.path.insert(0, '..')

from pocketflow import Node, Flow

class TestNode(Node):
    def exec(self, prep_res):
        print(f"Executing with: {prep_res}")
        return f"Result: {prep_res}"
    
    def post(self, shared, prep_res, exec_res):
        shared["output"] = exec_res
        return "default"

# Run test
shared = {"input": "test data"}
node = TestNode()
node.prep = lambda s: s.get("input")

flow = Flow(node)
result = flow.run(shared)

print(f"Final result: {result}")
print("Trial 001 completed - basic flow works!")
