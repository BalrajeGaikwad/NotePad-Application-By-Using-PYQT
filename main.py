from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui",self)

        self.current_path=None

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undoFile)
        self.actionRudo.triggered.connect(self.redoFile)
        self.actionCut.triggered.connect(self.cutFile)
        self.actionCopy.triggered.connect(self.copyFile)
        self.actionPaste.triggered.connect(self.pasteFile)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionChange_Font_Size.triggered.connect(self.changeFontSize)
        
    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path=None

    def saveFile(self):
        if self.current_path is not None:
            #save the changes without opening the file 
            filetext=self.textEdit.toPlainText()
            print(filetext)
        else:
            self.saveFileAs


    def saveFileAs(self):
        print("New file saveFileAs")

    def openFile(self):
        fname=QFileDialog.getOpenFileName(self,'open file',r'C:\Users\Admin\Documents\Balraje G\NotePad Application Using PyQt Framework','Text files (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0],'r') as f:
            filetext=f.read()
            self.textEdit.setText(filetext)
        self.current_path=fname[0]

    def undoFile(self):
       self.textEdit.undo()

    def redoFile(self):
        self.textEdit.redo()

    def cutFile(self):
        self.textEdit.cut()

    def copyFile(self):
        self.textEdit.copy()

    def pasteFile(self):
        self.textEdit.paste()

    def setDarkMode(self):
        print("New file setDarkMode")

    def setLightMode(self):
        print("New file setLightMode")

    def changeFontSize(self):
        print("New file changeFontSize")

if __name__=="__main__":
    app=QApplication(sys.argv)
    ui=Main()
    ui.show()
    app.exec_()