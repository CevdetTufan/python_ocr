import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img=Image.open('test.jpg')
text=pytesseract.image_to_string(img)

print(text)



