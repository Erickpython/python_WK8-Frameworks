# COVID-19 Research Publications Dashboard

This project provides an **interactive Streamlit dashboard** and an accompanying **Jupyter Notebook** to explore the [CORD-19 Research Challenge dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

* **`app.py`** – Streamlit web app to visualize publication trends, top journals, and a word cloud of paper titles.
* **`covid19Dataset.ipynb`** – Notebook with exploratory data analysis (EDA) of the dataset.

---

## 📂 Dataset

Download the dataset (`metadata.csv`) from Kaggle:
[CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Place the downloaded `metadata.csv` file in the **root directory** of this project.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<Erickpython>/<python_WK8-Frameworks>.git
cd <python_WK8-Frameworks>
```

### 2️⃣ Create a Virtual Environment

It’s recommended to use a virtual environment to keep dependencies isolated.

**Linux/MacOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3️⃣ Install Required Packages

Install all dependencies using:

```bash
pip install pandas matplotlib seaborn streamlit wordcloud jupyter
```

---

## 🚀 Running the Dashboard

After activating the virtual environment and ensuring `metadata.csv` is in the project folder:

```bash
streamlit run app.py
```

This will launch the dashboard in your default web browser at:

```
http://localhost:8501
```

---

## 📊 Exploring the Notebook

To open the Jupyter notebook for data analysis:

```bash
jupyter notebook covid19Dataset.ipynb
```

---

## 🛠️ Key Features

* **Filter publications by year**
* **Top 20 journals visualization**
* **Word cloud of paper titles**
* Clean and simple UI powered by **Streamlit**

---

## 📝 License

This project is for educational and research purposes. Check the [CORD-19 dataset license](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) before using the data in production.

---
