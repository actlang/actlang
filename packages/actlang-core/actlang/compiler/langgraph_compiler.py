from langgraph.graph import StateGraph

class LangGraphCompiler:
    def compile(self, actions):
        graph = StateGraph(dict)
        for action in actions:
            graph.add_node(action.__class__.__name__, action.run)
        for i in range(len(actions) - 1):
            graph.add_edge(actions[i].__class__.__name__, actions[i+1].__class__.__name__)
        graph.set_entry_point(actions[0].__class__.__name__)
        return graph.compile()
