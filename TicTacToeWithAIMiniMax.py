from PyQt5 import QtCore, QtGui, QtWidgets
from os import system

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(350, 400)
        MainWindow.setMinimumSize(350, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 4
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(lambda: self.btnclicked(3))
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 9
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(lambda: self.btnclicked(8))
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 8
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(lambda: self.btnclicked(7))
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 3
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(lambda: self.btnclicked(2))
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 5
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(lambda: self.btnclicked(4))
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 6
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(lambda: self.btnclicked(5))
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 7
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(lambda: self.btnclicked(6))
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 1
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(lambda: self.btnclicked(0))
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 2
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(lambda: self.btnclicked(1))
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label")
        self.verticalLayout.addWidget(self.label_1)

        self.reset = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   reset button
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(lambda: self.resetall())
        self.verticalLayout.addWidget(self.reset)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startgame()

    # this function is for resetting the buttons of the playboard
    def resetall(self):
        self.label.setText("Player Turn.")
        arr = [self.btn1, self.btn2, self.btn3, self.btn4,
               self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        for btn in arr:
            btn.setEnabled(True)
            btn.setText(" ")

        # it begin from start resetting all things
        self.startgame()

    def finalstate(self, player):
        self.label.setText(player + " Wins!")
        ar = [self.btn1, self.btn2, self.btn3, self.btn4,
              self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        for p in ar:
            p.setEnabled(False)

    # this will start the game
    def startgame(self):
        self.human = 'O'
        self.computer = 'X'
        self.statusCount = 0
        self.ar = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']
                   ]

        # computer move first
        self.computerMove(self.ar)

    # this will check for game completion
    def isWinner(self, user):
        # checking rows
        if self.ar[0][0] == self.ar[0][1] and self.ar[0][1] == self.ar[0][2] and self.ar[0][0] == user:
            return True
        if self.ar[1][0] == self.ar[1][1] and self.ar[1][1] == self.ar[1][2] and self.ar[1][0] == user:
            return True
        if self.ar[2][0] == self.ar[2][1] and self.ar[2][1] == self.ar[2][2] and self.ar[2][0] == user:
            return True

        # checking columns
        if self.ar[0][0] == self.ar[1][0] and self.ar[1][0] == self.ar[2][0] and self.ar[0][0] == user:
            return True
        if self.ar[0][1] == self.ar[1][1] and self.ar[1][1] == self.ar[2][1] and self.ar[0][1] == user:
            return True
        if self.ar[0][2] == self.ar[1][2] and self.ar[1][2] == self.ar[2][2] and self.ar[0][2] == user:
            return True

        # checking diagonals
        if self.ar[0][0] == self.ar[1][1] and self.ar[1][1] == self.ar[2][2] and self.ar[0][0] == user:
            return True
        if self.ar[0][2] == self.ar[1][1] and self.ar[1][1] == self.ar[2][0] and self.ar[0][2] == user:
            return True
        # return false if there is no winner
        return False

    
    def getScore(self, state):
        # checking rows
        for row in range(3):
            if state[row][0] == state[row][1] == state[row][2]:
                if state[row][0] == self.computer:
                    return 10
                elif state[row][0] == self.human:
                    return -10

        # checking for columns
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col]:
                if state[0][col] == self.computer:
                    return 10
                elif state[0][col] == self.human:
                    return -10

        # checking for diagonals
        # left diagnal
        if state[0][0] == state[1][1] == state[2][2]:
            if state[0][0] == self.computer:
                return 10
            elif state[0][0] == self.human:
                return -10
        # right diagonal
        if state[0][2] == state[1][1] == state[2][0]:
            if state[1][1] == self.computer:
                return 10
            elif state[1][1] == self.human:
                return -10
        return 0

    # this function is for computer move
    def computerMove(self, state):
        self.statusCount += 1
        bstVal = -1000
        row, col = -1, -1

        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = self.computer

                    moveVal = self.minimax(state, 0, False)

                    state[i][j] = ' '

                    if moveVal > bstVal:
                        row, col = i, j
                        bstVal = moveVal

        self.ar[row][col] = self.computer

        system('cls')
        for x in self.ar:
            print(x)

        dct = {(0, 0): self.btn1, (0, 1): self.btn2, (0, 2): self.btn3,
               (1, 0): self.btn4, (1, 1): self.btn5, (1, 2): self.btn6,
               (2, 0): self.btn7, (2, 1): self.btn8, (2, 2): self.btn9
               }

        dct[(row, col)].setText(self.computer)
        dct[(row, col)].setEnabled(False)

        # checking the if there is a winner or not
        check = self.isWinner(self.computer)
        if check:
            self.finalstate(self.computer)
        elif self.statusCount >= 9:
            self.label.setText("Tie Game")
        elif self.statusCount < 9:
            self.label.setText("OnGoing")
        else:
            pass

    # the minimax algorithm
    def minimax(self, state, depth, isMax):
        score = self.getScore(state)
        # 10 for computer
        if score == 10:
            return score
        # -10 for human
        if score == -10:
            return score

        if isMax:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = self.computer
                        best = max(best, self.minimax(state, depth+1, False))
                        state[i][j] = ' '
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = self.human
                        best = min(best, self.minimax(state, depth+1, True))
                        state[i][j] = ' '
            return best

    # this function is for human turn
    def btnclicked(self, i):
        # first move is for player and second move for computer
        self.statusCount += 1

        arrr = [self.btn1, self.btn2, self.btn3, self.btn4,
                self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

        # changing text of the button to the curent player
        arrr[i].setText(self.human)
        # disabling the button
        arrr[i].setEnabled(False)
        # saving the state in the array
        self.edit_state(i, self.human)
        system('cls')
        for x in self.ar:
            print(x)
        # checking if there is a winner or not
        check = self.isWinner(self.human)
        if check:
            self.finalstate(self.human)

        elif self.statusCount >= 9:
            self.label.setText("Tie Game")

        elif self.statusCount < 9:
            self.label.setText("OnGoing")
            self.computerMove(self.ar)

    def edit_state(self, i, user):
        if i == 0:
            self.ar[0][0] = user
        elif i == 1:
            self.ar[0][1] = user
        elif i == 2:
            self.ar[0][2] = user
        elif i == 3:
            self.ar[1][0] = user
        elif i == 4:
            self.ar[1][1] = user
        elif i == 5:
            self.ar[1][2] = user
        elif i == 6:
            self.ar[2][0] = user
        elif i == 7:
            self.ar[2][1] = user
        elif i == 8:
            self.ar[2][2] = user
        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.btn4.setText(_translate("MainWindow", " "))
        self.btn9.setText(_translate("MainWindow", " "))
        self.btn8.setText(_translate("MainWindow", " "))
        self.btn3.setText(_translate("MainWindow", " "))
        self.btn5.setText(_translate("MainWindow", " "))
        self.btn6.setText(_translate("MainWindow", " "))
        self.btn7.setText(_translate("MainWindow", " "))
        self.btn1.setText(_translate("MainWindow", " "))
        self.btn2.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "Computer's Turn."))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.label_1.setText(_translate("MainWindow", "Human VS Computer"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
