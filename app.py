from flask import Flask, render_template, request, jsonify
from utils.image_processor import process_image
from utils.chat_handler import generate_response
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400
    
    # Save the image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)
    
    # Process image and generate response
    try:
        image_description = process_image(image_path)
        user_question = request.form.get('question', 'What is in this image?')
        response = generate_response(image_description, user_question)
        return jsonify({
            'description': image_description,
            'response': response,
            'image_url': f'/static/uploads/{image.filename}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)