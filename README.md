# 🦋 Enchanted Wings – Butterfly Species Classification Project

## 📁 Project Overview

**Enchanted Wings** is a deep learning-based application that classifies butterfly species from input images using transfer learning. The project combines a trained CNN model with a user-friendly web interface built using Flask and HTML templates.

---

## 🧠 Key Features

- Image upload via web interface (`input.html`)
- Butterfly species prediction using a trained model (`vgg16_model.h5`)
- Output display with predicted species (`output.html`)
- Modular codebase with Flask backend (`app.py`)
- Streamlined UI using HTML/CSS templates
- Includes a Jupyter Notebook (`Enchanted_Wings.ipynb`) for development & testing

---

## 🗂 Folder Structure

```
project_root/
│
├── document/
│   └── projectReport.pdf               # Final project documentation
│
├── output_images/                      # Stores generated output images
│
├── static/                             # Static assets (CSS, JS, images if any)
│
├── templates/                          # HTML templates for the web interface
│   ├── index.html                      # Homepage
│   ├── input.html                      # Image upload page
│   └── output.html                     # Result display page
│
├── video_demo/                         # (Optional) Folder for demonstration videos
│
├── app.py                              # Flask backend script
├── Enchanted_Wings.ipynb              # Model development and training in Jupyter Notebook
├── requirements.txt                    # Required Python libraries
├── vgg16_model.h5                      # Pre-trained classification model
├── README.md                           # This README file
```

---

## ⚙️ Setup Instructions

1. **Clone the repository or download the folder.**

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the application:**

```bash
python app.py
```

4. **Open your browser and navigate to:**

```
http://127.0.0.1:5000/
```

---

## 🧪 Model Details

- **Architecture:** VGG16 (with transfer learning)
- **Dataset:** 6,499 butterfly images across 75 species
- **Training:** Conducted in `Enchanted_Wings.ipynb`
- **Performance:** ~80–90% validation accuracy

---

## 🔮 Future Enhancements

- Mobile-friendly responsive UI
- TensorFlow Lite integration for mobile apps
- Add user contributions to central butterfly database
- Real-time map of sightings for citizen science

---

## 👥 Team Info

**Team ID:** LTVIP2025TMID44964  
**Team Leader:** Vaddi Vyshnavi Devi  
**Team Members:**

- Swathi Ponnaganti
- Sunkara Naga Venkata Kanaka Sri Varshitha
- T Vinay

---

## 📄 License

This project is intended for educational and research purposes.
