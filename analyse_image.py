import os
from google.cloud import vision


# Set the path to your Google Cloud service account JSON key file here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

def analyze_image(path):
    # rest of your code...

# Set path to your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-key.json"

def analyze_image(path):
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    result = "Detected objects:\n"
    for label in labels:
        result += f"- {label.description} (score: {label.score:.2f})\n"

    return result
