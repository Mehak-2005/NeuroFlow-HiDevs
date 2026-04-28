from PIL import Image
import pytesseract
from . import ExtractedPage

def extract_image(file_path):
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)

    return [ExtractedPage(
        page_number=0,
        content=text,
        content_type="image_description",
        metadata={}
    )]