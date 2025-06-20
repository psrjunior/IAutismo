import os
from flask import Flask, request, jsonify
from google.cloud import vision

# Caminho absoluto do secret montado no Cloud Run
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/app/iautismo-service-account.json'

app = Flask(__name__)

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_content = image_file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    return jsonify({'labels': labels})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
