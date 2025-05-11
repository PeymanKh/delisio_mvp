# Import libraries
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file (OpenAI API key)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(f"{project_root}/.env")


def get_llm_response(dish_name: str, diet_type: str = "No Preference", nutritional_goal: str = "No Preference") -> str:
    """
    Queries the LLM (GPT-4) using LangChain to generate content for a given dish name.

    Args:
        dish_name (str): Name of the dish recognized by the model.
        diet_type (str): User's dietary preference (e.g., Vegan, Keto).
        nutritional_goal (str): User's nutritional goal (e.g., Weight Loss, Muscle Gain).

    Returns:
        str: LLM-generated response for the dish in Markdown format.
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

    prompt = f"""
    You are a professional chef and nutritionist. Based on the following user preferences:
    - Diet: {diet_type}
    - Nutritional Goal: {nutritional_goal}

    Provide a detailed description of the dish {dish_name}, including:
    - Ingredients (adjusted for the diet).
    - Preparation methods.
    - Any substitutions to meet the dietary and nutritional goals.
    """

    response = llm.invoke(prompt)

    return response.content
