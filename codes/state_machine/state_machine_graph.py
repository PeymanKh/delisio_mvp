# Import libraries
from langgraph.graph import StateGraph
from codes.state_machine.states import DelisioStates, GraphState


class LangGraphBuilder:
    """Builds and compiles the food image classification LangGraph pipeline."""

    def __init__(self):
        self.state_class = GraphState
        self.state_processor = DelisioStates()

    def build(self):
        builder = StateGraph(GraphState)

        # Add nodes
        builder.add_node("Process", self.state_processor.process_state)
        builder.add_node("Complete", lambda x: x)

        # Define flow
        builder.set_entry_point("Process")
        builder.add_edge("Process", "Complete")

        # Compile the graph
        return builder.compile()


# Function to Run the StateGraph
def run_state_machine_graph(initial_state: dict) -> dict:
    """
    Runs the LangGraph-based state machine for food recognition and LLM query.

    Args:
        initial_state (dict): Initial state containing image path and user preferences.

    Returns:
        dict: Final state containing recognized dish and LLM response.
    """
    # Build and compile the LangGraph
    flow = LangGraphBuilder().build()

    # Debugging: Print Initial State
    print("Debug - Initial State Before Flow:", initial_state)

    # Ensure the initial state is a dictionary and image path is a string
    if not isinstance(initial_state, dict):
        raise ValueError("Initial state must be a dictionary.")

    if not isinstance(initial_state.get("image_path"), str):
        raise ValueError("Image path in initial state must be a string.")

    # Run the state machine
    final_state = flow.invoke(initial_state)

    # Debugging: Print Final State
    print("Debug - Final State After Flow:", final_state)

    # Ensure the final state is a dictionary
    if not isinstance(final_state, dict):
        raise ValueError("Final state must be a dictionary.")

    return final_state
