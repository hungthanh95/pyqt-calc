import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

# Create an instance of QApplication
app = QApplication(sys.argv)

# create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('pyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
# helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# helloMsg.move(60, 15)

# QHBoxLayout manager
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
# window.setLayout(layout)

# QVBoxLayout manager
# layout1 = QVBoxLayout()
# layout1.addWidget(QPushButton('Top'))
# layout1.addWidget(QPushButton('Center'))
# layout1.addWidget(QPushButton('Bottom'))
# window.setLayout(layout1)


# QGridLayout manager
# layout2 = QGridLayout()
# layout2.addWidget(QPushButton('Button (0, 0)'), 0, 0)
# layout2.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout2.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout2.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout2.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout2.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout2.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout2.addWidget(QPushButton('Button (2, 1) = 2 Columns Span'), 2, 1, 1, 2)
# window.setLayout(layout2)


# QFormLayout manager
layout3 = QFormLayout()
layout3.addRow('Name:', QLineEdit())
layout3.addRow('Age:', QLineEdit())
layout3.addRow('Job:', QLineEdit())
layout3.addRow('Hobbies:', QLineEdit())
window.setLayout(layout3)


# show your application's GUI
window.show()

# run your application's event loop (or main loop)
sys.exit(app.exec_())