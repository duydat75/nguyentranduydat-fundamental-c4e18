import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import  *

import freakingmath
import random, math

WIDTH = 280
HEIGHT = 500
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
PADDING = 30
status_bar_height = -1

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board = Board(self)
        self.setCentralWidget(self.board)

        #self.statusbar = self.statusBar()
        #self.board.msg2Statusbar[str].connect(self.statusbar.showMessage)
        #status_bar_height = self.statusbar.height()
        #print("status bar height : {0}".format(status_bar_height))

        pal = QPalette()
        role = QPalette.Background
        pal.setColor(role, QColor("#009688"))
        self.setPalette(pal)

        self.board.start()
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry((screen.width() - WIDTH) / 2, (screen.height() - HEIGHT) / 2, WIDTH, HEIGHT)
        self.setWindowTitle('Freaking Math')
        self.show()

class Board(QWidget):
    msg2Statusbar = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent)
        self.initData()
        self.initBoard()
        # TODO: using keyboard to select True/False

    def initBoard(self):
##        self.score = 0

        # Initialize buttons
        trueBtnX = PADDING
        trueBtnY = HEIGHT - PADDING - BUTTON_HEIGHT

        falseBtnX = WIDTH  - PADDING - BUTTON_WIDTH
        falseBtnY = trueBtnY

        self.trueBtn = QPushButton("", self)
        self.trueBtn.setGeometry(trueBtnX, trueBtnY, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.trueBtn.setIcon(QIcon(".//img/true.png"))
        self.trueBtn.clicked.connect(self.handleCorrect)
        self.trueBtn.setIconSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))

        self.falseBtn = QPushButton("", self)
        self.falseBtn.setGeometry(falseBtnX, falseBtnY, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.icon = QIcon(".//img/false.png")
        self.falseBtn.setIcon(self.icon)
        self.falseBtn.setIconSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.falseBtn.clicked.connect(self.handleWrong)

        self.correctSound = QSound(".//sound/score.wav")
        self.incorrectSound = QSound(".//sound/gameover.wav")

    def initData(self):
        self.question = ""
        self.score = 0

    def start(self):
        self.msg2Statusbar.emit(str(self.score))
        self.getRandomMathProblem()
        # self.timer.start(Board.Speed, self)
        # self.renderNewQuestion()

    def getRandomNum(self):
        min = 1
        max = 10
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def getRandomAnswer(self):
        printed_answer = random.random() * (1 + 10) + 1
        return math.floor(printed_answer)

    def getRandomMathProblem(self):
        # self.num1 = self.getRandomNum()
        # self.num2 = self.getRandomNum()
        # self.answer = self.num1 + self.num2

        [self.num1, self.num2, self.sign, self.answer] =  freakingmath.generate_quiz()

        # TODO: need to rename properly genAnswer()

        # if (self.genAnswer() == 0) or (self.genAnswer() == 2):
        #     self.printed_answer = self.answer + 1
        # else:
        #     self.printed_answer = self.answer

##        self.question = ("%s + %d \n= %s"
##                     % (self.num1, self.num2, self.answer))
        if self.sign == "/":
            self.question = "{0} {1} {2} \n= {3:.2f}".format(self.num1, self.sign, self.num2, self.answer)
        else:
            self.question = "{0} {1} {2} \n= {3}".format(self.num1, self.sign, self.num2, self.answer)

        print(self.question)

    # def genAnswer(self):
    #     min = 0
    #     max = 3
    #     randomNum = random.random() * (max - min) + min
    #     return math.floor(randomNum)

    def increaseScore(self):
        self.score += 1
        # self.msg2Statusbar.emit(str(self.score))

    def resetScore(self):
        self.score = 0
        # self.msg2Statusbar.emit(str(self.score))
        # self.msg2Statusbar.emit(str("You Wrong! Reset Scrore."))

    def handleCorrect(self):
        if freakingmath.check_answer(self.num1, self.num2, self.sign, self.answer, True):
            self.increaseScore()
            self.correctSound.play()
        else:
            self.resetScore()
            self.incorrectSound.play()
        self.getRandomMathProblem()
        self.repaint()

    def handleWrong(self):
        if freakingmath.check_answer(self.num1, self.num2, self.sign, self.answer, False):
            self.increaseScore()
            self.correctSound.play()
        else:
            self.resetScore()
            self.incorrectSound.play()
        self.getRandomMathProblem()
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # Draw question
        qp.setPen(QColor("#E0F2F1"))
        qp.setFont(QFont('Roboto', 48, QFont.Bold))
        qp.drawText(QRect(0, 0, WIDTH, HEIGHT), Qt.AlignCenter, self.question)

        # Draw score
        qp.setPen(QColor("#E0F2F1"))
        qp.setFont(QFont('Roboto', 20, QFont.Bold))
        qp.drawText(QRect(0, 0, WIDTH, HEIGHT), Qt.AlignTop | Qt.AlignRight, str(self.score)) #Bit mask

        # TODO: Add Timer

    # def renderNewQuestion(self):
    #     self.getRandomMathProblem()
    #     self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
