**Career Guidance AI** is a web-based decision support system that helps students in Kerala choose suitable academic and career paths after secondary schooling (10th / 12th).

Unlike API-based solutions, this project uses a **locally trained machine learning model** to provide **explainable, reliable, and offline** career recommendations.

---

## 🎯 Problem Statement

Many students face confusion after secondary education due to:

* Lack of personalized career guidance
* Social and peer pressure
* Limited awareness of alternative education paths
* Financial and location constraints

This project addresses these challenges by analyzing a student’s background, interests, personality, and constraints to suggest suitable courses.

---

## 👥 Target Users

* Students after 10th or 12th
* First-generation learners
* Students from budget-constrained families
* Career counselors (as a support tool)

---

## 🧠 Solution Approach

1. Collect structured responses from students
2. Convert qualitative answers into numerical features
3. Use a trained **Decision Tree model** to predict suitable courses
4. Provide **clear explanations** for each recommendation

The system focuses on **clarity, explainability, and reliability**.

---

## 🏗️ System Architecture

```text
User
 ↓
Streamlit UI
 ↓
Feature Mapping
 ↓
Trained ML Model (Decision Tree)
 ↓
Course Recommendation + Explanation
```

---

## 🤖 AI / ML Design

### Model Used

* **Decision Tree Classifier**
* Trained using `scikit-learn`

### Why Decision Tree?

* Works well with small datasets
* Highly explainable
* Suitable for education and counseling systems
* No external API dependency

### Features Used

* Class completed (10th / 12th)
* Stream (Science / Others)
* Interest in technology or creativity
* Learning style (Practical / Theory)
* Personality (Introvert / Extrovert)
* Budget constraint
* Location preference
* Career goal (Early job / Higher studies)

---

## 🧪 Dataset

* Dataset is **synthetic and manually designed**
* Based on real-world counseling logic
* Stored in `data/training_data.csv`
* Easily extensible with real student data in future

---

## 🧩 Explainability

The system provides:

* A predicted course
* A human-readable explanation such as:

  > “Recommended based on your interest in technology, budget preference, and goal of early employment.”

This makes the system transparent and trustworthy.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – Web interface
* **scikit-learn** – Machine learning
* **pandas** – Data handling
* **joblib** – Model persistence

---

## 📂 Project Structure

```text
career-guidance-ai/
│
├── app.py                  # Streamlit application
├── ai_engine.py            # ML inference & explanation logic
├── train_model.py          # Model training script
├── storage.py              # Response storage
├── requirements.txt        # Dependencies
├── README.md               # Documentation
│
└── data/
    ├── training_data.csv   # Dataset
    └── responses.json      # User responses
```

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model

```bash
python train_model.py
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

* Use real student datasets
* Improve model accuracy with more data
* Add Malayalam language support
* Add parent / counselor dashboard
* Course and college recommendation mapping
* Replace ML model with advanced models if needed

---

## ⚠️ Limitations

* Dataset is small and synthetic
* Recommendations are advisory, not guarantees
* Not a replacement for professional counseling

---

## 📄 Conclusion

This project demonstrates how **AI can be applied responsibly** in education using **explainable, offline machine learning models**.
The focus is on **system design, reliability, and transparency**, making it suitable for real-world deployment with future enhancements.
