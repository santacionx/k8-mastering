from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set up the folder where files will be stored
UPLOAD_FOLDER = '/data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    # Render the HTML template for the home page with the upload form
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return redirect(url_for('list_files'))

@app.route('/files')
def list_files():
    # List all uploaded files
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('files.html', files=files)

@app.route('/files/<filename>')
def download_file(filename):
    # Allow users to download files
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            return file.read(), 200, {'Content-Type': 'application/octet-stream'}
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
