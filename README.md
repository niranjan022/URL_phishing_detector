# URL_phishing_detector

Dataset URL
https://drive.google.com/uc?export=download&id=1ivOv-ZfPt6xn2Jbt-9sgqM8Pcc2qPXuT

📌 Introduction

Phishing attacks are one of the most common cyber threats, where malicious websites try to trick users into revealing sensitive information such as usernames, passwords, and credit card details.

This project is a machine learning-based phishing URL detection system built with Streamlit.

Users can enter a URL, and the system classifies it as Safe or Phishing.

The backend uses an ML model trained on a dataset of phishing and benign URLs.

The frontend is a simple Streamlit web app for user interaction.

📂 Project Structure
phishing-detector/
 ├── app.py                # Streamlit app (frontend + backend connection)
 ├── sample_dataset.csv     # Small sample dataset for testing
 ├── requirements.txt       # Dependencies
 ├── utils.py (optional)    # Helper functions for preprocessing
 └── README.md

🔗 External Files

Since GitHub has file size limits:

Model file (.pkl) → Download here

Full dataset → Download here

▶️ How to Run the Project Locally
1. Clone the Repository
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Download Model File

Download the model from: Model Link

Place it in the project root directory (same folder as app.py).

5. Run the Streamlit App
streamlit run app.py


Your app will open in the browser at:
👉 http://localhost:8501/

🌐 Deployment

The app can also be deployed on Streamlit Cloud or other platforms (Heroku, Render, AWS).

On Streamlit Cloud, the app automatically downloads the model from the provided link at runtime.

📊 Dataset

The dataset contains features extracted from URLs such as length, number of dots, presence of suspicious symbols, etc.

A sample dataset is included in this repo (sample_dataset.csv).

The full dataset can be downloaded here: Dataset Link
.

🙌 Acknowledgements

Streamlit
 for the web framework.

Scikit-learn
