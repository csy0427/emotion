import argparse
import io
import os
from google.cloud import vision
from google.cloud.vision import types
GOOGLE_APPLICATION_CREDENTIALS="/Users/soo/Downloads/emotion/apikey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/soo/Downloads/emotion/apikey.json"

def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    return faces