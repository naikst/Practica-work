import sys  # использовать sys для приема аргументов командной строки
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # инициализация класса
        self.initializeUI()  # инициализация окна

    def initializeUI(self):
        # Настраиваем графический интерфейс приложения
        self.setGeometry(200, 100, 250, 250)  # размер окна
        self.setWindowTitle('Примерный макет')  # название окна


        self.setUpMainWindow()  # инициализация главного окна
        self.show()  # показать окно


    def setUpMainWindow(self):
        # Создайте QLabel для отображения в главном окне.
        hello_label = QLabel(self)
        hello_label.setText('Дратуте')
        hello_label.move(50, 50)
        image = 'images/ds.png'
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(50, 100)
        except FileNotFoundError as error:
            print(f'Image not found.\nError: {error}')



if __name__ == '__main__':
    #Всегда создавайте объект QApplication вашего графического интерфейса перед любым другим объектом,
    # принадлежащим графическому интерфейсу, включая главное окно.
    app = QApplication(sys.argv)  # инициализация приложения
    window = MainWindow()  # инициализация окна
    sys.exit(app.exec())  # запуск приложения




