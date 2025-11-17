# MNIST Digit Classifier 🖌️

A **handwritten digit classifier** using a **Convolutional Neural Network (CNN)** trained on the MNIST dataset. This project also includes a **Streamlit app** where you can draw a digit and get real-time predictions.

---

## Features

- CNN model trained on MNIST dataset (0-9 digits)
- Streamlit web app with a **drawable canvas**
- Real-time predictions for handwritten digits
- Easy to run locally or deploy
---

## Project Structure
digit_identifier/
├─ notebooks/
│ └─ mnist_train.ipynb # Training notebook
├─ models/
│ └─ mnist_cnn_model.keras # Saved trained model
├─ app.py # Streamlit app
├─ requirements.txt # Python dependencies
└─ README.md # Project description


---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/digit_identifier.git
cd digit_identifier
```

## Create a virtual environment
```bash
conda create -n mnist_cnn python=3.11
conda activate mnist_cnn
```
## Install dependencies
```bash
pip install -r requirements.txt
```

## Training the Model
```bash
jupyter notebook notebooks/mnist_train.ipynb
```

## Running the Streamlit App
```bash
streamlit run app.py
````

