from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from PIL import Image
import numpy as np
import pickle
import sys

# Force the default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'secret_key'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

# Load the model from the pickle file
with open('hybrid_model.pkl', 'rb') as f:
    hybrid_model = pickle.load(f)

# Define the input shape for the model
input_shape = (150, 150, 3)

# Define the class names
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']

def preprocess_image(image):
    # Resize and preprocess the image
    image = image.resize(input_shape[:2])  # Resize to the input shape required by the model
    image_array = np.array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

@app.route('/')
def index():
    # Always render the index.html page first
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            session.permanent = True  # Optional: Makes the session last beyond the browser session
            return redirect('/tumor_index')  # Redirect to tumor_index.html
        else:
            return render_template('login.html', error='Invalid user')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')

@app.route('/tumor_index')
def tumor_index():
    if 'email' not in session:
        return redirect('/login')
    return render_template('tumor_index.html')

@app.route('/pituitary')
def pituitary():
    if 'email' not in session:
        return redirect('/login')
    return render_template('pituitary.html')

@app.route('/giloma')
def glioma():
    if 'email' not in session:
        return redirect('/login')
    return render_template('giloma.html')

@app.route('/meningioma')
def meningioma():
    if 'email' not in session:
        return redirect('/login')
    return render_template('meningioma.html')

@app.route('/contact')
def contact():
    if 'email' not in session:
        return redirect('/login')
    return render_template('contact.html')

@app.route('/model')
def model_ui():
    if 'email' not in session:
        return redirect('/login')
    return render_template('model.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'email' not in session:
        return redirect('/login')
    if 'file' not in request.files:
        return render_template('results.html', error='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return render_template('results.html', error='No selected file'), 400
    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(file.stream).convert('RGB')
        image_array = preprocess_image(image)
        
        # For InceptionV3, duplicate the image_array to match the model's input requirements
        image_array_dup = np.copy(image_array)
        
        # Use the hybrid model to make predictions
        prediction = hybrid_model.predict([image_array, image_array_dup])
        predicted_class = np.argmax(prediction, axis=1)[0]
        predicted_label = class_names[predicted_class]
        
        return render_template('results.html', predicted_label=predicted_label)
    return render_template('results.html', error='Invalid file type'), 400

if __name__ == '__main__':
    app.run(debug=True)
