
## Delisio: A Multimodal State Machine for Personalized Recipe Generation

Delisio is an intelligent solution to generates personalized recipes tailored to your dietary preferences, nutritional goals, and allergies. By combining state-of-the-art computer vision and natural language processing, Delisio can recognize dishes from images and create customized recipes using a multimodal state machine.

### Key Features:
- **Food Image Recognition:** Accurately classifies 10 popular dishes using a fine-tuned Convolutional Neural Network (CNN).
- **Personalized Recipe Generation:** Leverages a Large Language Model (LLM) to create recipes that match your dietary needs and preferences.
- **State Machine Architecture:** Manages the recipe generation process using a scalable LangGraph state machine.
- **Custom High-Quality Dataset:** Built using high-resolution images scraped from Google and Bing, ensuring excellent model performance.

---

## Methodology


This project uses a well-structured methodology for data processing, model training, and evaluation. For a detailed explanation of the methodology, including:

- Data Collection and Preparation
- Deep Learning Architecture
- Model Training and Fine-Tuning Process
- Evaluation Metrics and Results
- State Machine Architecture

I invite you to read **technical_report.pdf** located in the `paper/` folder of this project.

➡️ **Technical Report:** [paper/technical_report.pdf](./paper/technical_report.pdf)

This report provides a comprehensive and in-depth understanding of how this project was designed, implemented, and evaluated.

---

## Dataset

This project uses a custom dataset of images for training and evaluation. The dataset is hosted on Google Drive for easy access. This dataset has been manually cleaned after scraping to verify its quality and reliability.

### Dataset Access
You can view and download the dataset manually using the link below:

**➡️ [Google Drive Dataset Link](https://drive.google.com/drive/folders/1o-WyAllNMNSCVfOZKQbcVazKbmeqSp_T?usp=drive_link)**

### How to Use the Dataset
1. **Visit the Google Drive Link:** Click the link above to open the dataset in your browser.
2. **Select the Files or Folders You Need:** For training the model again, you only need to download `split.zip` file and use it in the notebook.
3. **Download to Your Local Machine:**
   - If you want the full dataset, click the "Download All" button in Google Drive.
   - For specific images, right-click and choose "Download."

---

## Project Structure

```code
delisio_mvp/
├── codes/                        # Python scripts used in different stages of the project
│   ├── data_processing/        
│   │   ├── __init__.py
│   │   ├── data_cleaning.py
│   │   ├── data_scraping.py
│   │   └── data_splitting.py
│   ├── state_machine/            # State machine logic and LLM service
│   │   ├── __init__.py
│   │   ├── llm_service.py
│   │   ├── model_loader.py
│   │   ├── state_machine_graph.py
│   │   └── states.py
│   └── ui/                      # Streamlit UI for the project
│       ├── __init__.py
│       └── app.py
├── data/                        # Directory for storing dataset (to be manually downloaded)
│   └── README.md                # Instructions for using the dataset
├── models/                      # Directory for trained and fine-tuned models
│   ├── fine_tuned_food_classifier.h5
│   └── food_classifier.h5            
├── notebook/                    # Jupyter notebook for experiments and evaluations
│   └── model_experiments.ipynb
├── paper/                       # Technical report and related documents
│   ├── technical_report.pdf
│   └── technical_report.zip
├── poster/
├── .gitignore
├── README.md
└── requirements.txt
```


---

## Project Setup

### Prerequisites
- Python 3.8 or above
- pip (Python package manager)
- Virtual Environment (recommended)

### Installation
1. **Clone the Repository:**
   ```bash
   git https://github.com/PeymanKh/delisio_mvp.git
   cd delisio_mvp
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Dataset:** Follow the instructions in the "Dataset" section.

---

## Usage

To test the model on you local machine, you can simply run the following code on your terminal:
```bash
streamlit run codes/ui/app.py
```

---
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Research and develop by [Peyman Khodabandehlouei](https://www.linkedin.com/in/peyman-khodabandehlouei/)
