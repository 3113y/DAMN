from PyQt5.QtWidgets import QInputDialog, QMessageBox, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os

def maze_module(parent):
    parent.mark_site = [0, 0]
    parent.maze_click_count = 0
    parent.first_col = 0
    parent.second_col = 0
    times_maz, ok = QInputDialog.getInt(parent, '输入提示', '迷宫模块个数')
    if ok:
        available_coords = "可用的第一个标识坐标:\n(1,1), (1,3), (1,6), (2,2), (2,5), (3,4), (3,5), (4,5), (4,6)"
        QMessageBox.information(parent, '提示', available_coords)

        grid = QGridLayout()
        for row in range(6):
            for col in range(6):
                button = QPushButton(f'({row+1}, {col+1})')
                button.clicked.connect(lambda _, r=row, c=col: on_button_click(parent, r, c))
                grid.addWidget(button, row, col)
        parent.setLayout(grid)
        parent.setWindowTitle('按下两个标识方块所在的位置')
    else:
        return

def on_button_click(parent, row, col):
    if parent.maze_click_count == 0:
        parent.mark_site[0] = row + 1
        parent.first_col = col + 1
    else:
        parent.mark_site[1] = row + 1
        parent.second_col = col + 1

    parent.maze_click_count += 1
    if parent.maze_click_count == 2:
        pic_name = parent.mark_site[0] * 10 + parent.first_col
        available_pics = [11, 13, 16, 22, 25, 34, 35, 45, 46]
        if pic_name not in available_pics:
            QMessageBox.warning(parent, '警告', f'坐标 ({parent.mark_site[0]}, {parent.first_col}) 对应的图片不存在\n可用的坐标组合请参考游戏手册')
            parent.maze_click_count = 0
            parent.mark_site = [0, 0]
            return

        file_name = f"pictures\\{pic_name}.jpg"
        parent.file_name = file_name
        load_and_display_image(parent)

def load_and_display_image(parent):
    try:
        if not os.path.exists(parent.file_name):
            QMessageBox.warning(parent, '错误', f'图片文件不存在:\n{parent.file_name}')
            return

        pixmap = QPixmap(parent.file_name)
        if pixmap.isNull():
            QMessageBox.warning(parent, '错误', f'无法加载图片:\n{parent.file_name}')
        else:
            layout = QVBoxLayout()
            image_label = QLabel(parent)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

            return_button = QPushButton("返回主菜单", parent)
            return_button.clicked.connect(parent.switch_module)
            layout.addWidget(return_button)

            parent.setLayout(layout)
            parent.resize(pixmap.width(), pixmap.height())
    except Exception as e:
        QMessageBox.critical(parent, '错误', f'加载图片时出现错误:\n{str(e)}')