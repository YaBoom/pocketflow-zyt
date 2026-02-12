"""
PocketFlow - 100行代码的极简LLM框架
Source: https://github.com/The-Pocket/PocketFlow
"""

from typing import Any, Dict, Optional

class Node:
    """Base node class for PocketFlow."""
    
    def prep(self, shared: Dict[str, Any]) -> Any:
        """Prepare inputs for execution."""
        return None
    
    def exec(self, prep_res: Any) -> Any:
        """Execute the node's logic."""
        return None
    
    def post(self, shared: Dict[str, Any], prep_res: Any, exec_res: Any) -> Optional[str]:
        """Post-process results and decide next action."""
        return None
    
    def run(self, shared: Dict[str, Any]) -> Optional[str]:
        """Run the node: prep -> exec -> post."""
        prep_res = self.prep(shared)
        exec_res = self.exec(prep_res)
        return self.post(shared, prep_res, exec_res)


class Flow:
    """Flow that orchestrates nodes."""
    
    def __init__(self, start_node: Node):
        self.start_node = start_node
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, Dict[str, str]] = {}
    
    def add_node(self, name: str, node: Node):
        """Add a node to the flow."""
        self.nodes[name] = node
    
    def add_edge(self, from_node: str, to_node: str, action: str = "default"):
        """Add an edge between nodes."""
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node][action] = to_node
    
    def run(self, shared: Dict[str, Any]) -> Any:
        """Execute the flow."""
        current = self.start_node
        while current:
            action = current.run(shared)
            # Simple linear flow for now
            if hasattr(current, '_next'):
                current = current._next
            else:
                current = None
        return shared


# Utility for chaining nodes
def connect(from_node: Node, to_node: Node):
    """Connect two nodes."""
    from_node._next = to_node
    return to_node

# Allow >> operator for connection
Node.__rshift__ = lambda self, other: connect(self, other)
