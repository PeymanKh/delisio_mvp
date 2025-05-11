import numpy as np
from typing import TypedDict, Optional
from codes.state_machine.llm_service import get_llm_response
from codes.state_machine.model_loader import load_model, preprocess_image


class GraphState(TypedDict, total=False):
    """Defines the state passed between LangGraph nodes."""
    image_path: str
    recognized_dish: Optional[str]
    llm_response: Optional[str]
    diet_type: Optional[str]
    nutritional_goal: Optional[str]


class DelisioStates:
    """
    Unified class that handles all state processing for food recognition:
    - Model loading (Singleton)
    - Image prediction (TensorFlow model)
    - LLM query for description (LangChain)
    """
    _model = None
    _class_names = [
        "Burger", "Fried Chicken", "Kebab", "Paella", "Pasta",
        "Pizza", "Ramen", "Steak", "Sushi", "Tacos"
    ]

    def __init__(self):
        """Initializes the FoodRecognitionState with model loading."""
        if DelisioStates._model is None:
            DelisioStates._model = load_model()

    def classify_image(self, state: GraphState) -> GraphState:
        """
        Predicts the food category for the given image using the TensorFlow model.

        Args:
            state (GraphState): Current state of the graph containing the image path.

        Returns:
            GraphState: Updated state with recognized dish name.
        """
        image_path = state.get("image_path")

        # Debugging Type Check
        if not isinstance(image_path, str):
            raise ValueError("Image path must be a string.")

        if not image_path:
            raise ValueError("Image path not found in state.")

        image = preprocess_image(image_path)
        predictions = DelisioStates._model.predict(image)
        recognized_dish = self._class_names[np.argmax(predictions)]
        state["recognized_dish"] = recognized_dish
        return state

    @staticmethod
    def generate_recipe(state: GraphState) -> GraphState:
        """
        Queries the LLM for a detailed description of the recognized dish.

        Args:
            state (GraphState): Current state of the graph containing the dish name.

        Returns:
            GraphState: Updated state with LLM response.
        """
        dish_name = state.get("recognized_dish")
        diet_type = state.get("diet_type", "No Preference")
        nutritional_goal = state.get("nutritional_goal", "No Preference")

        if not dish_name:
            raise ValueError("Recognized dish not found in state.")

        # Pass user preferences to LLM for personalized recipe
        llm_response = get_llm_response(
            dish_name=dish_name,
            diet_type=diet_type,
            nutritional_goal=nutritional_goal
        )

        state["llm_response"] = llm_response
        return state

    def process_state(self, state: GraphState) -> GraphState:
        """
        Main function that processes the state:
        - Predicts the dish using the model.
        - Queries the LLM for a detailed description.

        Args:
            state (GraphState): Initial state containing image path.

        Returns:
            GraphState: Final state with recognized dish and LLM response.
        """
        state = self.classify_image(state)
        state = self.generate_recipe(state)
        return state
