from PyQt5.Qt import QUrl, QDesktopServices
import requests
import webbrowser
from hashlib import new
from os import system
from tokenize import String
import sys


from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)


class MainWindow(QWidget):
    def query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()

    def __init


if __name__ == "__main__":

    main = Main()
    hostname = "127.0.0.1:8000"
    res = main.query(hostname)
    if res:
        print(res)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your host IP:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.text.setText(self.get_ip())
        self.label1.move(10, 35)

        self.label2 = QLabel("Enter your api-key:", self)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 50)
        set.label2.move(10, 45)

        self.label3 = QLabel("Enter the host name:", self)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 70)
        set.label3.move(10, 65)


        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 90)
        self.button = QPushButton("Send", self)
        self.button.move(10, 110)
        set.label4.move(10, 105)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        key = self.text3.text()
        hostip = self.text4.text()
        res = self.__query("http://"+hostip+"/ip/"+hostname+"?key="+key)
        if res and type(res)==dict:
            #Commandes utilisées pour récupérer les valeurs de latitude et de longitude :
            lat=str(res["latitude"])
            long=str(res["longitude"])
            #Intéraction avec la fenêtre:
            self.label2.setText("latitude="+lat+"\nlongitude="+long)
            self.label2.adjustSize()
            self.show()
            #Lien de openstreetmap pour lancer une requête de recherche :
            webbrowser.open(url="https://www.openstreetmap.org/?mlat=%22+lat+%22&mlon=%22+long+%22#map=12%22",new=0)


    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()