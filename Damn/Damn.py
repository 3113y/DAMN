import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from scripts.line_module import line_module
from scripts.button_module import button_module
from scripts.four_color_block_module import four_color_block_module
from scripts.memory_module import memory_module
from scripts.maze_module import maze_module

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.switch_module()

    def switch_module(self):
        str_col_box = QMessageBox(self)
        str_col_box.setWindowTitle('选择模块')
        str_col_box.setText('哪个模块？')
        line_module_button = str_col_box.addButton("线路模块", QMessageBox.ActionRole)
        button_module_button = str_col_box.addButton("按钮模块", QMessageBox.ActionRole)
        four_color_block_module_button = str_col_box.addButton("四色方块模块", QMessageBox.ActionRole)
        memory_module_button = str_col_box.addButton("记忆模块", QMessageBox.ActionRole)
        maze_module_button = str_col_box.addButton("迷宫模块", QMessageBox.ActionRole)
        cancel_button = str_col_box.addButton(QMessageBox.Cancel)

        reply = str_col_box.exec_()
        if str_col_box.clickedButton() == cancel_button:
            sys.exit(0)
            return
        if str_col_box.clickedButton() == line_module_button:
            line_module(self)
        elif str_col_box.clickedButton() == button_module_button:
            button_module(self)
        elif str_col_box.clickedButton() == four_color_block_module_button:
            four_color_block_module(self)
        elif str_col_box.clickedButton() == memory_module_button:
            memory_module(self)
        elif str_col_box.clickedButton() == maze_module_button:
            maze_module(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())