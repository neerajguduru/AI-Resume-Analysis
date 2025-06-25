from pdfminer.high_level import extract_text
import pytesseract
from PIL import Image
from io import BytesIO

def extract_text_from_file(file):
    filename = file.filename.lower()

    try:
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(BytesIO(file.read()))
            img = img.convert('L').resize((img.width // 2, img.height // 2))  # grayscale + downscale
            return pytesseract.image_to_string(img)

        elif filename.endswith('.pdf'):
            return extract_text(BytesIO(file.read()))

        else:
            return "❌ Unsupported file type."
    except Exception as e:
        return f"❌ Error reading file: {e}"
