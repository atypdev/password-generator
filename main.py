import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 219)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 391, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(6, 6, 131, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 53, 18))
        self.label_3.setObjectName("label_3")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 94, 51, 32))
        self.spinBox.setObjectName("spinBox")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(225, 140, 74, 22))
        self.radioButton_2.setObjectName("Normal")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(79, 140, 140, 22))
        self.radioButton.setObjectName("Special")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(305, 140, 98, 22))
        self.radioButton_3.setObjectName("Passphrase")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 43, 18))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(31, 140, 43, 18))
        self.label_4.setObjectName("label_4")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 29, 88, 34))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.passgen(self.spinBox.value(), self.lineEdit))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 30))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Generated Password:"))
        self.label_3.setText(_translate("MainWindow", "Settings:"))
        self.radioButton_2.setText(_translate("MainWindow", "Normal"))
        self.radioButton.setText(_translate("MainWindow", "Special Characters"))
        self.radioButton_3.setText(_translate("MainWindow", "Passphrase"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.label_4.setText(_translate("MainWindow", "Type"))
        self.pushButton.setText(_translate("MainWindow", "Generate!"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

    def passgen(self, length, lineEdit):
        if length == 0:
            lineEdit.setText("ERROR: Length cannot be 0")
            return
        
        if not (self.radioButton.isChecked() or self.radioButton_3.isChecked() or self.radioButton_2.isChecked()):
            lineEdit.setText("ERROR: Must select a password type!")
            return
        
        if self.radioButton.isChecked():
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        elif self.radioButton_3.isChecked():
            password = '-'.join(random.choice(passphrase_words) for _ in range(length))
        elif self.radioButton_2.isChecked():
            password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        
        lineEdit.setText(password)

password_characters = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],  # digits
    ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?', "'", '"', '\\', '/']  # additional special characters
]

passphrase_words = [
    'fantastic', 'wonderful', 'magnificent', 'amazing',  # Positive adjectives
    'serenity', 'tranquility', 'harmony', 'peaceful',  # Calm and peaceful words
    'whisper', 'giggle', 'murmur', 'laughter',  # Soft and gentle sounds
    'breeze', 'ocean', 'mountain', 'forest',  # Natural landscapes
    'moonlight', 'starlight', 'firelight', 'candlelight',  # Types of light
    'treasure', 'fortune', 'wealth', 'riches',  # Words related to abundance
    'bravery', 'courage', 'heroic', 'valiant',  # Words related to courage
    'inspiration', 'creativity', 'imagination', 'innovation',  # Creative words
    'legendary', 'mythical', 'mystical', 'enchantment',
    'serendipity', 'ephemeral', 'ethereal', 'effervescent',  # Beautiful and uncommon words
    'cascade', 'serenade', 'melody', 'symphony',  # Musical terms
    'silhouette', 'twilight', 'silvery', 'glimmer',  # Twilight and moon-related words
    'radiant', 'luminous', 'gleaming', 'shimmering',  # Bright and radiant words
    'sapphire', 'emerald', 'topaz', 'amethyst',  # Gemstone names
    'nostalgia', 'memories', 'recollection', 'remembrance',  # Words related to memory
    'victory', 'triumph', 'conquer', 'achievement',  # Words related to success
    'serenity', 'tranquility', 'calm', 'peacefulness',  # Words conveying peace and calm
    'adventure', 'explore', 'discovery', 'journey',  # Words evoking adventure and exploration
    'correct', 'horse', 'battery', 'staple',  # Example passphrase from XKCD comic
    'sunshine', 'rainbow', 'butterfly', 'garden',  # Nature-related words
    'chocolate', 'cookie', 'cupcake', 'icecream',  # Food-related words
    'adventure', 'explorer', 'journey', 'discovery'
]

# length = int(input("Enter desired length:"))
# pass_type = int(input("What type of password do you want to generate? (0 = Special, 1 = Passphrase, 2 = Normal)[2]:"))
# password = ""
        
# passw = passgen(length, pass_type)
# print("Generated password for type %s:" % pass_type + " " + passw)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Qt PassGen")
    MainWindow.show()
    sys.exit(app.exec_())