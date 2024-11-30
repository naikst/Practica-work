import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Настройки графического интерфейса приложения."""
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = ['images/ds.png',
                  'images/ifg.png']
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/profile_image.png":
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f'Файл не найден.\n{error}')

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText('Никита К')
        user_label.setFont(QFont('Bahnschrift SemiBold SemiConden', 20))
        user_label.move(85, 140)
        bio_label = QLabel(self)
        bio_label.setText('Программист')
        bio_label.setFont(QFont('Bahnschrift SemiBold SemiConden', 17))
        bio_label.move(15, 180)
        about_label = QLabel(self)
        about_label.setText('О себе: Я программист, который любит программировать.')
        about_label.setWordWrap(True)
        about_label.move(15, 190)
        skills_label = QLabel(self)
        skills_label.setText('Начинающий специалист')
        skills_label.setFont(QFont('Bahnschrift SemiBold SemiConden', 17))
        skills_label.move(15, 240)
        languages_label = QLabel(self)
        languages_label.setText("Python, OOP")
        languages_label.move(15, 260)
        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Bahnschrift SemiBold SemiConden", 17))
        experience_label.move(15, 290)
        developer_label = QLabel(self)
        developer_label.setText("Python Разработчик")
        developer_label.move(15, 310)
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2011 - настоящее время")
        dev_dates_label.setFont(QFont("Bahnschrift SemiBold SemiConden", 10))
        dev_dates_label.move(15, 330)
        driver_label = QLabel(self)
        driver_label.setText("Водитель доставки пиццы")
        driver_label.move(15, 350)
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Bahnschrift SemiBold SemiConden", 10))
        driver_dates_label.move(15, 370)

    # Run program


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
