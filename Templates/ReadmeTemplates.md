# 📂 Templates Folder

This folder contains all the **HTML templates** used in the Brain Tumor Detection project.  
These templates define the user interface for interacting with the system, such as uploading MRI images, viewing results, and navigating the application.

---

## 📄 Files in this folder

- **index.html** → Homepage of the project.  
- **tumor_index.html** → Main landing page for tumor detection module.  
- **login.html** → User login page.  
- **register.html** → User registration page.  
- **contact.html** → Contact page for reaching project maintainers/developers.  
- **model.html** → Displays details about the models (CNN, VGG16, InceptionV3, Hybrid).  
- **results.html** → Shows prediction results (benign/malignant) after model runs.  
- **giloma.html** → Information/results page related to **Glioma tumors**.  
- **meningioma.html** → Information/results page related to **Meningioma tumors**.  
- **pituitary.html** → Information/results page related to **Pituitary tumors**.  

---

## 📌 Usage in Flask

In Flask, these templates are rendered using `render_template()`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')
