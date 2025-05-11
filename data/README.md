## Dataset

This project uses a custom dataset of images for training and evaluation. The dataset is hosted on Google Drive for easy access.

### Dataset Access
You can view and download the dataset manually using the link below:

**➡️ [Google Drive Dataset Link](https://drive.google.com/drive/folders/1o-WyAllNMNSCVfOZKQbcVazKbmeqSp_T?usp=drive_link)**

### How to Use the Dataset
1. **Visit the Google Drive Link:** Click the link above to open the dataset in your browser.
2. **Select the Files or Folders You Need:** For training the model again, you only need to download `split.zip` file and use it in notebook
3. **Download to Your Local Machine:**
   - If you want the full dataset, click the "Download All" button in Google Drive.
   - For specific images, right-click and choose "Download."

### Where to Place the Dataset
- After downloading, extract the dataset (if it is compressed) and place it in the `data/` folder of this project directory:

```code
my_ai_project/
├── data/  # Place the dataset here
├── codes/
├── models/
├── notebooks/
├── paper/
├── poster 
├── README.md 
├── .gitignore 
└── requirements.txt 
```


### ❓ Why Manual Download?
- Google Drive has a file limit for automated downloads via `gdown` (50 files), making manual download more reliable.
- Manually accessing the dataset allows you to preview files before downloading.

### ❗ Important Notes
- Make sure the dataset is placed in the `data/` directory for the project to work properly.
- The project code is designed to automatically read data from the `data/` folder.
