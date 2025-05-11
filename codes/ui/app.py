# Import libraries
import os
import sys
import shutil
import streamlit as st

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from codes.state_machine.state_machine_graph import run_state_machine_graph

# Streamlit UI Setup
st.set_page_config(page_title="Delisio MVP", layout="centered")
st.title("Delisio - A Multimodal State Machine for Personalized Recipe Generation")

# Header
st.markdown("""
### Research and developed by [Peyman Khodabandehlouei](https://www.linkedin.com/in/peyman-khodabandehlouei/)
- [Marketing Page](https://delisio.app)
- [Technical Report](https://github.com/PeymanKh/delisio_mvp)
- [GitHub Repository](https://github.com/PeymanKh/delisio_mvp)
---
""")

# Description
st.markdown("""
#### About This Project
Welcome to the Delisio MVP, an intelligence solution designed to generate personalized recipes from food images. This project demonstrates:

- Food Recognition: Utilizing a custom-trained Convolutional Neural Network (CNN) model for accurate dish classification.
- Text Generation: Leveraging a Large Language Model (LLM) for personalized recipe creation.
- Scalable State Management: Powered by LangGraph, enabling efficient, modular, and scalable state machine design.

For the full source code and detailed implementation, visit this [GitHub repository](https://github.com/PeymanKh/delisio_mvp).
""")

st.markdown("---")

# Important Note
st.markdown("""
### Important Note:
This MVP version of Delisio is a prototype designed to validate the core concept. Currently, it only supports 10 food categories for recognition, and edge cases may not be handled perfectly. 

#### Supported Food Categories:
- Burger
- Fried Chicken
- Kebab
- Paella
- Pasta
- Pizza
- Ramen
- Steak
- Sushi
- Tacos
""")

st.markdown("---")

# Upload Image
uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

# Dietary Preferences
st.subheader("Select Your Dietary Preferences")
diet_type = st.selectbox(
    "Choose your diet type:",
    options=[
        "No Preference",
        "Vegan",
        "Vegetarian",
        "Pescatarian",
        "Keto",
        "Low Carb",
        "High Protein",
        "Gluten-Free",
        "Dairy-Free"
    ]
)

# Nutritional Goal
nutritional_goal = st.selectbox(
    "Choose your nutritional goal:",
    options=[
        "No Preference",
        "Weight Loss",
        "Muscle Gain",
        "Balanced Diet",
        "Heart Health",
        "Diabetes Management",
        "Boost Immunity"
    ]
)

# Generate Recipe Button
if st.button("Generate Recipe"):
    if uploaded_file:
        try:
            # Ensure the temp directory exists
            temp_dir = "temp"
            os.makedirs(temp_dir, exist_ok=True)

            # Save the uploaded image to a temporary file
            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")

            # Directly write the uploaded file to disk
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_file.read())

            # Double-check if the image is saved properly
            if not os.path.exists(temp_image_path):
                st.error("Error: Image could not be saved.")
            else:
                # Send image and user preferences to LangGraph State Machine
                initial_state = {
                    "image_path": temp_image_path,
                    "diet_type": diet_type,
                    "nutritional_goal": nutritional_goal
                }

                # Running the State Machine (Secure without Debugging for Users)
                result = run_state_machine_graph(initial_state)

                # Display Results
                st.subheader("Prediction Result")
                recognized_dish = result.get("recognized_dish", "Unknown")
                llm_response = result.get('llm_response', 'No description available')

                if recognized_dish:
                    st.write(f"Recognized Dish: {recognized_dish}")
                else:
                    st.error("Failed to recognize the dish.")

                st.markdown(llm_response, unsafe_allow_html=True)

            # Cleanup (Safe Check)
            if os.path.exists(temp_image_path):
                try:
                    os.remove(temp_image_path)
                except Exception as e:
                    st.warning(f"Temporary file could not be deleted: {str(e)}")

        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
    else:
        st.error("Please upload an image first.")

st.markdown("---")
st.caption("© 2025 Peyman Khodabandehlouei. All rights reserved.")
