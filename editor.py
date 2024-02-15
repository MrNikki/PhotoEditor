from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from PIL import Image, ImageFilter
import os



class ImageEditor(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = ""
        self.ui.btn_dir.clicked.connect(self.show_files)
        self.ui.list_files.itemClicked.connect(self.showimage)
        self.ui.btn_bw.clicked.connect(self.do_bw)
        self.ui.btn_left.clicked.connect(self.do_left)
        self.ui.btn_right.clicked.connect(self.do_right)
        self.ui.btn_mirror.clicked.connect(self.do_mirror)
        self.ui.btn_sharp.clicked.connect(self.do_sharp)
        self.ui.btn_4.clicked.connect(self.add_light)
        self.ui.btn_3.clicked.connect(self.minus_light)
        self.ui.btn_1.clicked.connect(self.blurr)
        self.ui.btn_2.clicked.connect(self.relief)
        self.ui.btn_5.clicked.connect(self.save_choosen_image)

        

    def choose_dir(self):
        self.workdir = QtWidgets.QFileDialog.getExistingDirectory()
    
    def filter(self, files, extentions):
        result = []
        for file in files:
            for ex in extentions:
                if file.endswith(ex):
                    result.append(file)
        return result
    
    def show_files(self):
        extentions = [".jpg", ".png", ".jpeg", ".bmp"]
        self.choose_dir()
        try:
            files = os.listdir(self.workdir)
            files = self.filter(files, extentions)
            self.ui.list_files.clear()
            for file in files:
                self.ui.list_files.addItems(files)


        except:
            win = QtWidgets.QMessageBox()
            win.setText("Кудиииииииииииииии?????")
            win.exec()
    def loadimage(self, name):
        self.filename = name
        self.path = os.path.join(self.workdir, self.filename)
        self.image = Image.open(self.path)

    def showimage(self):
        if self.ui.list_files.selectedItems():
            name = self.ui.list_files.selectedItems()[0].text()
            self.loadimage(name)

            pix = QtGui.QPixmap(self.path)
            w, h = self.ui.image.width(), self.ui.image.height()
            pix = pix.scaled(w,h, QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(pix)

    def show_changed(self):
        self.loadimage("changed.jpg")
        pix = QtGui.QPixmap(self.path)
        w, h = self.ui.image.width(), self.ui.image.height()
        pix = pix.scaled(w,h, QtCore.Qt.KeepAspectRatio)
        self.ui.image.setPixmap(pix)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveimage()
        self.show_changed()

    def do_left(self):
        self.image = self.image.rotate(270)
        self.saveimage()
        self.show_changed()


    def do_right(self):
        self.image = self.image.rotate(90)
        self.saveimage()
        self.show_changed()

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        self.show_changed()

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveimage()
        self.show_changed()

    def blurr(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(10))
        self.saveimage()
        self.show_changed()

    def relief(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveimage()
        self.show_changed()

    def add_light(self):
        self.image = self.image.point(lambda x: x * 2)
        self.saveimage()
        self.show_changed()
        
    def minus_light(self):
        self.image = self.image.point(lambda x: x * 0.5)
        self.saveimage()
        self.show_changed()



    def saveimage(self):
        self.path = os.path.join(self.workdir, "changed.jpg")
        self.image = self.image.convert("RGB")
        self.image.save(self.path)

    def save_choosen_image(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        path = os.path.join(path, "changed.jpg")
        self.image.save(path)
        win = QtWidgets.QMessageBox()
        win.setText("Файл збережено!")
        win.exec()






    

app = QtWidgets.QApplication([])
win = ImageEditor()
win.show()
app.exec()
