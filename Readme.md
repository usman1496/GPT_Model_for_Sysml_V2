// Overview:
This repository, GPT_Model_for_SysML_v2, contains a web-based chat application powered by a pre-trained GPT-Neo 2.7B model trained on Sysmlv2 dataset. The application is built using Flask for the backend, along with the transformers library from Hugging Face for model interaction. The front-end features a simple user interface, enabling users to interact with the GPT model in a chatbot-like manner.

// Key Features:
Flask Web Application: The backend provides REST APIs to interface with the GPT-Neo model.
Frontend UI: A clean, responsive chat interface built using HTML, CSS, and JavaScript.
GPT-Neo 2.7B Model: Utilizes a pre-trained GPT-Neo 2.7B model trained on Sysmlv2 dataset, which must be downloaded and loaded locally.
Environment Configuration: Uses environment variables managed by a .env file for configurable settings such as the model path.
Important Note: Pre-trained Model Required
To run this application, you must have a pre-trained GPT-Neo 2.7B model trained on Sysml v2. Then this model should be downloaded and placed in a directory accessible to the application. You can obtain the GPT-Neo model from the Hugging Face Model Hub or any custom-trained version of GPT-Neo. Ensure that all model files (shards) are present in the specified path.

// Setup and Installation
Prerequisites: 
1) Python 3.8+
2) PyTorch (compatible with your system's GPU or CPU)
3) Hugging Face transformers library
4) Flask

// Environment Setup
Clone this repository:

1) bash
Copy code
git clone https://github.com/your-username/GPT_Model_for_SysML_v2.git
cd GPT_Model_for_SysML_v2
Set up a virtual environment and activate it:

2) bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

3) bash
Copy code
pip install -r requirements.txt
Download and place the GPT-Neo model:

Download the GPT-Neo 2.7B model from the Hugging Face Hub or use your own trained version.
Ensure the model files are placed in a directory.


4) bash
Copy code
MODEL_PATH=C:/Users/musma/Desktop/gpt_neo_2.7B_trained
FLASK_ENV=development
Running the Application
To start the Flask application locally:

5) bash
Copy code
python run.py
The app will be accessible at http://localhost:5000.

// Summary
This project demonstrates how to integrate a pre-trained GPT-Neo 2.7B model into a Flask-based web application to create an interactive chatbot interface. The app supports CPU and GPU environments and allows for flexible configuration using environment variables. You must download and set up a pre-trained model to use this application.
