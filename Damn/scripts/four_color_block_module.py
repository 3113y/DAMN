from PyQt5.QtWidgets import QInputDialog, QMessageBox

def four_color_block_module(parent):
    times_fbl, ok = QInputDialog.getInt(parent, '输入提示', '四色方块模块数（默认无失误）')
    if ok:
        serial_num_aeiou = None
        for times in range(times_fbl):
            if times == 0:
                reply = QMessageBox.question(parent, '输入提示', '是否有元音字母AEIOU？', QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                   serial_num_aeiou = 1 
                else:
                   serial_num_aeiou = 0
            if serial_num_aeiou == 1:
                QMessageBox.information(parent, '结果', '红-蓝，蓝-红，绿-黄，黄-绿')
            else:
                QMessageBox.information(parent, '结果', '红-蓝，蓝-黄，绿-绿，黄-红')
    parent.switch_module()