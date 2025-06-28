# 🦋 Enchanted Wings – Marvels of Butterfly Species

**Team ID:** LTVIP2025TMID44964  
**Team Size:** 4  
**Team Leader:** Vaddi Vyshnavi Devi  
**Team Members:**

- Swathi Ponnaganti
- Sunkara Naga Venkata Kanaka Sri Varshitha
- T Vinay

## 📌 Project Overview

**Enchanted Wings** is a deep learning-based butterfly species classification system designed to help researchers, educators, and citizen scientists identify butterfly species from images. It leverages transfer learning with CNN architectures like MobileNetV2 or EfficientNetB0 to classify 75 butterfly species with over 6,499 images.

---

## 🚩 Problem Statement

Manual butterfly identification is slow and requires expert knowledge. This project aims to automate that process using an AI-based image classification system.

---

## 💡 Proposed Solution

- Use **transfer learning** on pre-trained CNNs.
- Classify butterflies from a dataset of 6,499 labeled images.
- Develop a lightweight and accurate prediction model.
- Deploy via **Streamlit** or **Flask** for easy user interaction.

---

## 👥 Target Users

- Biodiversity scientists
- Ecologists
- Students and educators
- Citizen science communities

---

## 🎯 Expected Outcomes

- Accurate butterfly classification model
- Easy-to-use web-based interface
- Promotion of conservation and ecological awareness

---

## 🧱 Tech Stack

- **Language:** Python 3.x
- **Libraries:** TensorFlow, Keras, NumPy, Pandas, scikit-learn
- **Deployment:** Flask / Streamlit (optional TensorFlow Lite for mobile)
- **Development:** Jupyter Notebooks or modular Python scripts

---

## 🛠 Project Phases

### 1. **Brainstorming & Ideation**

- Problem identification
- User needs and expected output

### 2. **Requirement Analysis**

- Functional and technical requirements
- Challenges like dataset imbalance and small sample size

### 3. **Project Design**

- Modular deep learning pipeline
- Responsive, user-friendly interface
- Optional educational and conservation features

### 4. **Agile Planning**

- Iterative sprints for data cleaning, model training, UI setup
- Task assignments based on module expertise

### 5. **Project Development**

- Preprocessing pipeline
- Transfer learning with MobileNetV2
- Dropout, early stopping to reduce overfitting
- Colab used for GPU access

### 6. **Functional & Performance Testing**

- Label encoding validation, error handling
- Achieved ~80–90% accuracy
- Ready for deployment testing

---

## ✅ Features

- Image upload & species prediction
- Confidence score with species details
- Mobile-friendly and educational interface
- Expandable for field use and research logging

---

## ⚠️ Challenges Addressed

- Dataset imbalance → Augmentation, weighting
- Overfitting → Dropout, regularization
- Hardware limitations → Google Colab
- Robust model saving/loading

---

## 📁 Future Scope

- Full deployment via web or mobile
- Integration with biodiversity databases
- Community features for shared contributions
