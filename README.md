# CTS-HACKATHON-BRAIN-TUMOR-CLASSIFICATION
Deep learning project for brain tumor detection using MRI scans. Implements CNN, MobileNetV3, VGG16, InceptionV3, and a Hybrid VGG16+InceptionV3 model, achieving up to 93.5% accuracy. Includes preprocessing (Normalization, CLAHE, Augmentation), model training, evaluation, and comparison of architectures.
# 🧠 Brain Tumor Detection using Deep Learning

This project focuses on **early detection and classification of brain tumors** using **MRI images** with **Deep Learning models**.  
We implemented **CNN, VGG16, InceptionV3, and a Hybrid Model** (VGG16 + InceptionV3) to achieve high accuracy in detecting benign and malignant tumors.

---

## 🚀 Project Overview
- Early detection of brain tumors is crucial for treatment.
- MRI images are analyzed using deep learning to automate detection.
- Implemented data preprocessing (normalization, CLAHE, augmentation).
- Compared multiple models:
  - **Basic CNN**
  - **Enhanced CNN**
  - **MobileNetV3**
  - **Hybrid Model (VGG16 + InceptionV3)**

---

## 📊 Results
| Model              | Accuracy |
|--------------------|----------|
| CNN (Basic)        | 46.8%    |
| CNN (Enhanced)     | 84%      |
| Hybrid (VGG16+IncepV3) | **93.5%** |

---

## 🛠️ Tech Stack
- **Python 3.x**
- **TensorFlow / Keras**
- **NumPy, Pandas**
- **OpenCV (CLAHE)**
- **Matplotlib, Seaborn**

---

## 🔧 Installation & Usage
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/CTS-NPN-Project.git
   cd CTS-NPN-Project
