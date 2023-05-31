import pytesseract
from PIL import Image

# Path to Tesseract OCR executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image using PIL
image_path = 'sheet_modify.jpg'
image = Image.open(image_path)

# Preprocess the image (optional)
# You can use PIL or other image processing libraries to enhance image quality

# Convert PIL image to RGB format
image = image.convert('RGB')

# Perform OCR using Tesseract
custom_config = r'--oem 3 --psm 6 -l kor'  # OCR configuration with Korean language
text = pytesseract.image_to_string(image, config=custom_config)

# Print the recognized text
print(text)