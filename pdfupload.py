from flask import Flask, jsonify, request
from pdf_metadata_extractor import extract_information
from pdf_file_processing import process_pdf_and_segment  # Adjust the filename accordingly
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Endpoint to upload a PDF document
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file format. Please upload a PDF file'}), 400


# Endpoint to call extract_information for a specific file
@app.route('/get_metadata/<filename>', methods=['GET'])
def get_metadata(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if filename.endswith('.pdf') and os.path.exists(file_path):
        metadata = extract_information(file_path)
        return jsonify(metadata)
    else:
        return jsonify({'error': 'File not found or not a PDF'})
    

if __name__ == '__main__':
    app.run(debug=True)
#curl -X POST -F "file=@$PathToPDF$" http://localhost:5000/upload
