import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import numpy as np
import pygame
import time

numbers = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024])

probs = [0.20, 0.20, 0.25, 0.20, 0.10, 0.04, 0.005, 0.004, 0.001]

list_a = np.random.choice(numbers, size=(6, 6), p=probs)
'''
sound_file = "music.mp3"

pygame.mixer.init()
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)'''





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setWindowTitle("2048 Game: win by reaching 2048!")
        self.setGeometry(700, 300, 500, 500)
        self.numbers = numbers
        self.probs = probs


        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button5 = QPushButton()
        self.button6 = QPushButton()
        self.button7 = QPushButton()
        self.button8 = QPushButton()
        self.button9 = QPushButton()
        self.button10 = QPushButton()
        self.button11 = QPushButton()
        self.button12 = QPushButton()
        self.button13 = QPushButton()
        self.button14 = QPushButton()
        self.button15 = QPushButton()
        self.button16 = QPushButton()
        self.button17 = QPushButton()
        self.button18 = QPushButton()
        self.button19 = QPushButton()
        self.button20 = QPushButton()
        self.button21 = QPushButton()
        self.button22 = QPushButton()
        self.button23 = QPushButton()
        self.button24 = QPushButton()
        self.button25 = QPushButton()
        self.button26 = QPushButton()
        self.button27 = QPushButton()
        self.button28 = QPushButton()
        self.button29 = QPushButton()
        self.button30 = QPushButton()
        self.button31 = QPushButton()
        self.button32 = QPushButton()
        self.button33 = QPushButton()
        self.button34 = QPushButton()
        self.button35 = QPushButton()
        self.button36 = QPushButton()
        self.list_b = np.zeros((6, 6), dtype=int)






        for i in range(6):
            for j in range(6):
                if i == 0 and j == 0:
                    self.button1 = QPushButton(str(list_a[0][0]), self)
                elif i ==0 and j == 1:
                    self.button2 = QPushButton(str(list_a[0][1]), self)
                elif i ==0 and j == 2:
                    self.button3 = QPushButton(str(list_a[0][2]), self)
                elif i ==0 and j == 3:
                    self.button4 = QPushButton(str(list_a[0][3]), self)
                elif i ==0 and j == 4:
                    self.button5 = QPushButton(str(list_a[0][4]), self)
                elif i ==0 and j == 5:
                    self.button6 = QPushButton(str(list_a[0][5]), self)
                elif i ==1 and j == 0:
                    self.button7 = QPushButton(str(list_a[1][0]), self)
                elif i == 1 and j == 1:
                    self.button8 = QPushButton(str(list_a[1][1]), self)
                elif i == 1 and j == 2:
                    self.button9 = QPushButton(str(list_a[1][2]), self)
                elif i == 1 and j == 3:
                    self.button10 = QPushButton(str(list_a[1][3]), self)
                elif i == 1 and j == 4:
                    self.button11 = QPushButton(str(list_a[1][4]), self)
                elif i == 1 and j == 5:
                    self.button12 = QPushButton(str(list_a[1][5]), self)
                elif i == 2 and j == 0:
                    self.button13 = QPushButton(str(list_a[2][0]), self)
                elif i == 2 and j == 1:
                    self.button14 = QPushButton(str(list_a[2][1]), self)
                elif i == 2 and j == 2:
                    self.button15 = QPushButton(str(list_a[2][2]), self)
                elif i == 2 and j == 3:
                    self.button16 = QPushButton(str(list_a[2][3]), self)
                elif i == 2 and j == 4:
                    self.button17 = QPushButton(str(list_a[2][4]), self)
                elif i == 2 and j == 5:
                    self.button18 = QPushButton(str(list_a[2][5]), self)

                elif i == 3 and j == 0:
                    self.button19 = QPushButton(str(list_a[3][0]), self)
                elif i == 3 and j == 1:
                    self.button20 = QPushButton(str(list_a[3][1]), self)
                elif i == 3 and j == 2:
                    self.button21 = QPushButton(str(list_a[3][2]), self)
                elif i == 3 and j == 3:
                    self.button22 = QPushButton(str(list_a[3][3]), self)
                elif i == 3 and j == 4:
                    self.button23 = QPushButton(str(list_a[3][4]), self)
                elif i == 3 and j == 5:
                    self.button24 = QPushButton(str(list_a[3][5]), self)

                elif i == 4 and j == 0:
                    self.button25 = QPushButton(str(list_a[4][0]), self)
                elif i == 4 and j == 1:
                    self.button26 = QPushButton(str(list_a[4][1]), self)
                elif i == 4 and j == 2:
                    self.button27 = QPushButton(str(list_a[4][2]), self)
                elif i == 4 and j == 3:
                    self.button28 = QPushButton(str(list_a[4][3]), self)
                elif i == 4 and j == 4:
                    self.button29 = QPushButton(str(list_a[4][4]), self)
                elif i == 4 and j == 5:
                    self.button30 = QPushButton(str(list_a[4][5]), self)

                elif i == 5 and j == 0:
                    self.button31 = QPushButton(str(list_a[5][0]), self)
                elif i == 5 and j == 1:
                    self.button32 = QPushButton(str(list_a[5][1]), self)
                elif i == 5 and j == 2:
                    self.button33 = QPushButton(str(list_a[5][2]), self)
                elif i == 5 and j == 3:
                    self.button34 = QPushButton(str(list_a[5][3]), self)
                elif i == 5 and j == 4:
                    self.button35 = QPushButton(str(list_a[5][4]), self)
                elif i == 5 and j == 5:
                    self.button36 = QPushButton(str(list_a[5][5]), self)
        for i in range(6):
            for j in range(6):
                index = i * 6 + j + 1  # because buttons are 1-indexed (button1 to button36)
                button = getattr(self, f"button{index}")
                text = button.text()
                self.list_b[i][j] = int(text) if text.isdigit() else 0

        vbox = QGridLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox.setSpacing(0)  # No space between widgets
        vbox.setContentsMargins(0, 0, 0, 0)
        for i in range(37):
            getattr(self, f"button{index}").setFixedSize(60,60)

        vbox.addWidget(self.button1, 0, 0)
        vbox.addWidget(self.button2, 0, 1)
        vbox.addWidget(self.button3, 0, 2)
        vbox.addWidget(self.button4, 0, 3)
        vbox.addWidget(self.button5, 0, 4)
        vbox.addWidget(self.button6, 0, 5)
        vbox.addWidget(self.button7, 1, 0)
        vbox.addWidget(self.button8, 1, 1)
        vbox.addWidget(self.button9, 1, 2)
        vbox.addWidget(self.button10, 1, 3)
        vbox.addWidget(self.button11, 1, 4)
        vbox.addWidget(self.button12, 1, 5)
        vbox.addWidget(self.button13, 2, 0)
        vbox.addWidget(self.button14, 2, 1)
        vbox.addWidget(self.button15, 2, 2)
        vbox.addWidget(self.button16, 2, 3)
        vbox.addWidget(self.button17, 2, 4)
        vbox.addWidget(self.button18, 2, 5)
        vbox.addWidget(self.button19, 3, 0)
        vbox.addWidget(self.button20, 3, 1)
        vbox.addWidget(self.button21, 3, 2)
        vbox.addWidget(self.button22, 3, 3)
        vbox.addWidget(self.button23, 3, 4)
        vbox.addWidget(self.button24, 3, 5)
        vbox.addWidget(self.button25, 4, 0)
        vbox.addWidget(self.button26, 4, 1)
        vbox.addWidget(self.button27, 4, 2)
        vbox.addWidget(self.button28, 4, 3)
        vbox.addWidget(self.button29, 4, 4)
        vbox.addWidget(self.button30, 4, 5)
        vbox.addWidget(self.button31, 5, 0)
        vbox.addWidget(self.button32, 5, 1)
        vbox.addWidget(self.button33, 5, 2)
        vbox.addWidget(self.button34, 5, 3)
        vbox.addWidget(self.button35, 5, 4)
        vbox.addWidget(self.button36, 5, 5)
        central_widget.setLayout(vbox)
        for i in range(1, 37):
            getattr(self, f'button{i}').setFixedSize(60, 60)  # Set each button to 60x60 pixels
        self.setStyleSheet("""
          QPushButton{
          font-family: Arial;
          font-size: 25px;
          border: 3px solid;
          padding: 0px;
          margin: 0px;
          }
          QPushButton:hover{
          background-color: lightblue;}
         """)
        for i in range(1, 37):
            getattr(self, f'button{i}').clicked.connect(self.on_click)
        self.first_clicked_button = None
        self.second_clicked_button = None
        self.get_color()


    def on_click(self):


        sender = self.sender()

        # First click
        if self.first_clicked_button is None:
            self.first_clicked_button = sender
            sender.setStyleSheet("font-weight: bold; font-size: 25px;")


            return

        # Second click
        if sender != self.first_clicked_button:
            self.second_clicked_button = sender
            sender.setStyleSheet("font-weight: bold; font-size: 25px;")


            # Now check if adjacent
            if self.are_adjacent(self.first_clicked_button, self.second_clicked_button):
                if self.first_clicked_button.text() == self.second_clicked_button.text():
                    new_val = str(int(self.second_clicked_button.text()) * 2)
                    self.second_clicked_button.setText(new_val)
                    pos1 = self.get_position(self.first_clicked_button)

                    if pos1:
                        row, col = pos1

                        # Choose a new random value from list_a
                        new_value = np.random.choice(self.numbers, p=self.probs)  # assuming you saved those

                        # Update the text of the first button
                        self.first_clicked_button.setText(str(new_value))

                        # Update the internal list as well
                        self.list_b[row][col] = new_value


            # Reset styles and clicked buttons
            self.first_clicked_button.setStyleSheet("")
            self.second_clicked_button.setStyleSheet("")
            self.get_color()
            self.first_clicked_button = None
            self.second_clicked_button = None
        else:
            self.first_clicked_button.setStyleSheet("")
            self.get_color()
            self.first_clicked_button = None
        for i in range(6):
            for j in range(6):
                index = i * 6 + j + 1  # because buttons are 1-indexed (button1 to button36)
                button = getattr(self, f"button{index}")
                text = button.text()
                self.list_b[i][j] = int(text) if text.isdigit() else 0
        if self.check2048():
            msg = QLabel("🎉 You Win! 2048 reached!")
            msg.setStyleSheet("font-size: 30px; color: green;")
            msg.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(msg)
        if self.isLose(self.list_b):
            msg = QLabel(":( You lose! No possible tries")
            msg.setStyleSheet("font-size: 30px; color: red;")
            msg.setAlignment(Qt.AlignCenter)



    def get_position(self, button):
        for i in range(6):
            for j in range(6):
                index = i * 6 + j + 1
                if getattr(self, f"button{index}") == button:
                    return (i, j)
        return None


    def are_adjacent(self, btn1, btn2):
        pos1 = self.get_position(btn1)
        pos2 = self.get_position(btn2)

        if not pos1 or not pos2:
            return False

        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])

        return max(dx, dy) == 1 and (dx + dy) >= 1

    def check2048(self):
        for i in range(6):
            for j in range(6):
                if self.list_b[i][j] == 2048:
                    return True
        return False

    def get_color(self):
        for i in range(1, 37):
            if int(getattr(self, f'button{i}').text()) == 4:
                getattr(self, f'button{i}').setStyleSheet("""background-color: green;""")
            elif int(getattr(self, f'button{i}').text()) == 8:
                getattr(self, f'button{i}').setStyleSheet("background-color: lime;")
            elif int(getattr(self, f'button{i}').text()) == 16:
                getattr(self, f'button{i}').setStyleSheet("background-color: yellow;")
            elif int(getattr(self, f'button{i}').text()) == 32:
                getattr(self, f'button{i}').setStyleSheet("background-color: orange;")
            elif int(getattr(self, f'button{i}').text()) == 64:
                getattr(self, f'button{i}').setStyleSheet("background-color: red;")
            elif int(getattr(self, f'button{i}').text()) == 128:
                getattr(self, f'button{i}').setStyleSheet("background-color: magenta;")
            elif int(getattr(self, f'button{i}').text()) == 256:
                getattr(self, f'button{i}').setStyleSheet("background-color: cyan;")
            elif int(getattr(self, f'button{i}').text()) == 512:
                getattr(self, f'button{i}').setStyleSheet("background-color: blue;")
            elif int(getattr(self, f'button{i}').text()) == 1024:
                getattr(self, f'button{i}').setStyleSheet("background-color: purple;")
    def isLose(self, listCheck):
        for i in range(6):
            for j in range(6):
                current = listCheck[i][j]
                match i:
                    case 0 | 1 | 2 | 3 | 4 | 5:
                        match j:
                            case 0 | 1 | 2 | 3 | 4 | 5:
                                # Right
                                if j < 5 and current == listCheck[i][j + 1]:
                                    return True
                                # Down
                                if i < 5 and current == listCheck[i + 1][j]:
                                    return True
                                # Down-Right (↘)
                                if i < 5 and j < 5 and current == listCheck[i + 1][j + 1]:
                                    return True
                                # Down-Left (↙)
                                if i < 5 and j > 0 and current == listCheck[i + 1][j - 1]:
                                    return True
                                # Up
                                if i > 0 and current == listCheck[i - 1][j]:
                                    return True
                                # Left
                                if j > 0 and current == listCheck[i][j - 1]:
                                    return True
                                # Up-Right (↗)
                                if i > 0 and j < 5 and current == listCheck[i - 1][j + 1]:
                                    return True
                                # Up-Left (↖)
                                if i > 0 and j > 0 and current == listCheck[i - 1][j - 1]:
                                    return True
        return False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()











