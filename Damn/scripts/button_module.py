from PyQt5.QtWidgets import QInputDialog, QMessageBox

def button_module(parent):
    times_but, ok = QInputDialog.getInt(parent, '输入提示', '按钮模块个数')
    if ok:
        bat_num = 0
        car_con = None
        frk_con = None
        for times in range(times_but):
            but_col_box = QMessageBox(parent)
            but_col_box.setWindowTitle('输入提示')
            but_col_box.setText('线的颜色？')
            white_button = but_col_box.addButton("白色", QMessageBox.ActionRole)
            red_button = but_col_box.addButton("红色", QMessageBox.ActionRole)
            yellow_button = but_col_box.addButton("黄色", QMessageBox.ActionRole)
            blue_button = but_col_box.addButton("蓝色", QMessageBox.ActionRole)
            cancel_button = but_col_box.addButton(QMessageBox.Cancel)
            reply = but_col_box.exec_()
            if reply == QMessageBox.Cancel:
                continue
            if but_col_box.clickedButton() == white_button:
                col_but = 1
            elif but_col_box.clickedButton() == red_button:
                col_but = 2
            elif but_col_box.clickedButton() == yellow_button:
                col_but = 3
            elif but_col_box.clickedButton() == blue_button:
                col_but = 4
            but_char_box = QMessageBox(parent)
            but_char_box.setWindowTitle('输入提示')
            but_char_box.setText('按钮上的字？')
            discontinue_button = but_char_box.addButton("中止", QMessageBox.ActionRole)
            hold_button = but_char_box.addButton("按住", QMessageBox.ActionRole)
            detonate_button = but_char_box.addButton("引爆", QMessageBox.ActionRole)
            cancel_button = but_char_box.addButton(QMessageBox.Cancel)
            reply = but_char_box.exec_()
            if reply == QMessageBox.Cancel:
                continue
            if but_char_box.clickedButton() == discontinue_button:
                char_but = 1
            elif but_char_box.clickedButton() == hold_button:
                char_but = 2
            elif but_char_box.clickedButton() == detonate_button:
                char_but = 3
            if times == 0:
                bat_num, ok = QInputDialog.getInt(parent, '输入提示', '电池数量')
                if not ok:
                    return
            reply = QMessageBox.question(parent, '输入提示', 'CAR 是否亮？', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
               car_con = 1 
            else:
               car_con = 0
            reply = QMessageBox.question(parent, '输入提示', 'FRK 是否亮？', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
               frk_con = 1 
            else:
               frk_con = 0
            if col_but == 4 and char_but == 1:
                QMessageBox.information(parent, '结果', '按住按钮，参考下文')
            elif bat_num > 1 and char_but == 3:
                QMessageBox.information(parent, '结果', '按下按钮并立即松开')
            elif col_but == 1 and car_con == 1:
                QMessageBox.information(parent, '结果', '按住按钮，参考下文')
            elif bat_num >= 2 and frk_con == 1:
                QMessageBox.information(parent, '结果', '按下按钮并立即松开')
            elif col_but == 3:
                QMessageBox.information(parent, '结果', '按住按钮，参考下文')
            elif char_but == 2 and col_but == 2:
                QMessageBox.information(parent, '结果', '按下按钮并立即松开')
            else:
                QMessageBox.information(parent, '结果', '按住按钮，参考下文')
            QMessageBox.information(parent, '提示', '蓝色：在任意数位显示4时松开\n白色：在任意数位显示1时松开\n黄色：在任意数位显示5时松开\n其他颜色： 在任意数位显示1时松开')
    parent.switch_module()