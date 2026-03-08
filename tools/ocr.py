import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):

    image = np.array(Image.open(image_path))

    result = reader.readtext(image)

    text = []

    for (_, detected_text, _) in result:
        text.append(detected_text)

    return " ".join(text)