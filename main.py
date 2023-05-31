import pytesseract
from PIL import Image
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QTextEdit
from PyQt5 import QtCore
from hanspell import spell_checker

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

        # 한글만 추출
        text = re.sub('[^가-힣\s]', '', text)
        text = text.replace(" ", "")

        # # 맞춤법 검사 진행

        lines = text.splitlines()

        # Perform spell checking on each line
        corrected_lines = []
        for line in lines:
            spelled_line = spell_checker.check(line)
            corrected_lines.append(spelled_line.checked)

        # Join the corrected lines back into a single string
        corrected_text = '\n'.join(corrected_lines)

        print(corrected_text)

        # 텍스트 프린트
        self.text_edit.setText(corrected_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImagePathViewer()
    window.show()
    sys.exit(app.exec_())