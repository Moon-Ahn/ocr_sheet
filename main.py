import pytesseract
from PIL import Image

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QTextEdit
from PyQt5 import QtCore

class ImagePathViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Path Viewer")
        self.resize(300, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.image_path_label = QLabel(self)
        self.image_path_label.setWordWrap(True)


        select_button = QPushButton("Select Image", self)
        select_button.clicked.connect(self.ocr)

        layout.addWidget(select_button)

        self.text_edit = QTextEdit(self)
        self.text_edit.setMinimumHeight(200)
        layout.addWidget(self.text_edit)

        layout.addWidget(self.image_path_label)

    def select_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.gif)")
        if file_path:
            return file_path

    def ocr(self):
        image_path = self.select_image()
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Load image using PIL
        image = Image.open(image_path)

        # Preprocess the image (optional)
        # You can use PIL or other image processing libraries to enhance image quality

        # Convert PIL image to RGB format
        image = image.convert('RGB')

        # Perform OCR using Tesseract
        custom_config = r'--oem 3 --psm 6 -l kor'  # OCR configuration with Korean language
        text = pytesseract.image_to_string(image, config=custom_config)

        # Print the recognized text
        self.text_edit.setText(text)
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImagePathViewer()
    window.show()
    sys.exit(app.exec_())