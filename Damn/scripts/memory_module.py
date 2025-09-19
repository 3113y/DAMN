from PyQt5.QtWidgets import QInputDialog, QMessageBox

def memory_module(parent):
    times_rem, ok = QInputDialog.getInt(parent, '输入提示', '记忆模块个数')
    if ok:
        for times in range(times_rem):
            rem_stage = [0] * 5
            rem_stage_site = [0] * 5
            rem_stage_scre = [0] * 5

            rem_stage[0], ok = QInputDialog.getInt(parent, '输入提示', '输入大屏上的数字')
            if not ok:
                return
            if rem_stage[0] == 1:
                rem_stage_scre[0], ok = QInputDialog.getInt(parent, '输入提示', '按下第二个位置按钮并输入该数字')
                rem_stage_site[0] = 2
            elif rem_stage[0] == 2:
                rem_stage_scre[0], ok = QInputDialog.getInt(parent, '输入提示', '按下第二个位置按钮并输入该数字')
                rem_stage_site[0] = 2
            elif rem_stage[0] == 3:
                rem_stage_scre[0], ok = QInputDialog.getInt(parent, '输入提示', '按下第三个位置按钮并输入该数字')
                rem_stage_site[0] = 3
            else:
                rem_stage_scre[0], ok = QInputDialog.getInt(parent, '输入提示', '按下第四个位置按钮并输入该数字')
                rem_stage_site[0] = 3
            if not ok:
                return

            rem_stage[1], ok = QInputDialog.getInt(parent, '输入提示', '输入大屏上的数字')
            if not ok:
                return
            if rem_stage[1] == 1:
                rem_stage_site[1], ok = QInputDialog.getInt(parent, '输入提示', '按下数字为4的按钮并输入该数字位置')
                rem_stage_scre[1] = 4
            elif rem_stage[1] == 2:
                rem_stage_scre[1], ok = QInputDialog.getInt(parent, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                rem_stage_site[1] = rem_stage_site[0]
            elif rem_stage[1] == 3:
                rem_stage_scre[1], ok = QInputDialog.getInt(parent, '输入提示', '按下第一个位置按钮并输入该数字')
                rem_stage_site[1] = 1
            else:
                rem_stage_scre[1], ok = QInputDialog.getInt(parent, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                rem_stage_site[1] = rem_stage_site[0]
            if not ok:
                return

            rem_stage[2], ok = QInputDialog.getInt(parent, '输入提示', '输入大屏上的数字')
            if not ok:
                return
            if rem_stage[2] == 1:
                rem_stage_site[2], ok = QInputDialog.getInt(parent, '输入提示', f'按下数字为{rem_stage_scre[1]}的按钮并输入该数字位置')
                rem_stage_scre[2] = rem_stage_scre[1]
            elif rem_stage[2] == 2:
                rem_stage_site[2], ok = QInputDialog.getInt(parent, '输入提示', f'按下数字为{rem_stage_scre[0]}的按钮并输入该数字位置')
                rem_stage_scre[2] = rem_stage_scre[0]
            elif rem_stage[2] == 3:
                rem_stage_scre[2], ok = QInputDialog.getInt(parent, '输入提示', '按下第三个位置按钮并输入该数字')
                rem_stage_site[2] = 3
            else:
                rem_stage_site[2], ok = QInputDialog.getInt(parent, '输入提示', '按下数字为4的按钮并输入该数字位置')
                rem_stage_scre[2] = 4
            if not ok:
                return

            rem_stage[3], ok = QInputDialog.getInt(parent, '输入提示', '输入大屏上的数字')
            if not ok:
                return
            if rem_stage[3] == 1:
                rem_stage_scre[3], ok = QInputDialog.getInt(parent, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                rem_stage_site[3] = rem_stage_site[0]
            elif rem_stage[3] == 2:
                rem_stage_scre[3], ok = QInputDialog.getInt(parent, '输入提示', '按下第一个位置按钮并输入该数字')
                rem_stage_site[3] = 1
            else:
                rem_stage_scre[3], ok = QInputDialog.getInt(parent, '输入提示', f'按下第{rem_stage_site[1]}个位置按钮并输入该数字')
                rem_stage_site[3] = rem_stage_site[1]
            if not ok:
                return

            rem_stage[4], ok = QInputDialog.getInt(parent, '输入提示', '输入大屏上的数字')
            if not ok:
                return
            if rem_stage[4] == 1:
                QMessageBox.information(parent, '结果', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
            elif rem_stage[4] == 2:
                QMessageBox.information(parent, '结果', f'按下第{rem_stage_site[1]}个位置按钮并输入该数字')
            elif rem_stage[4] == 3:
                QMessageBox.information(parent, '结果', f'按下第{rem_stage_site[3]}个位置按钮并输入该数字')
            else:
                QMessageBox.information(parent, '结果', f'按下第{rem_stage_site[2]}个位置按钮并输入该数字')
    parent.switch_module()