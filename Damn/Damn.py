import sys
from tkinter import SEL
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox

class MainApp(QWidget):
    # 调用函数与模块
    def __init__(self):
        super().__init__()
        # 线路模块处理
        self.line_module()
        # 按钮模块处理
        self.button_module()
        # 四色方块模块处理
        self.four_color_block_module()
        # 记忆模块处理
        self.memory_module()
        # 迷宫模块处理
        self.maze_module()
    # 线路模块
    def line_module(self):
        # 获取线路模块个数
        times_str, ok = QInputDialog.getInt(self, '输入提示', '线路模块个数')
        if ok:
            serial_num_end = None
            for times in range(times_str):
                strs_arr = [0] * 6
                # 显示颜色输入提示信息
                for i in range(6):
                    # 获取线颜色输入
                    reply = QMessageBox.question(self, '输入提示', '线的颜色？', QMessageBox.White | QMessageBox.Red | QMessageBox.Yellow | QMessageBox.Blue | QMessageBox.Black)
                    if ok:
                        if reply==QMessageBox.White:
                            strs_arr[i] = 1
                        elif reply==QMessageBox.Red:
                            strs_arr[i] = 2
                        elif reply==QMessageBox.Yellow:
                            strs_arr[i] = 3
                        elif reply==QMessageBox.Blue:
                            strs_arr[i] = 4
                        else:
                            strs_arr[i] = 5
                    else:
                        return
                if times == 0:
                    # 仅在第一次循环时询问序列号末位
                    serial_num_end, ok = QInputDialog.getInt(self, '输入提示', '输入序列号末位')
                    if not ok:
                        return

                str_sum = 0  # 总线数
                strs_num_sum = [0] * 6  # 分别为白红黄蓝黑
                strs_arr_rem0 = [0] * 6  # 统计去0以后的线序所用数组
                j = 0
                for i in range(6):
                    if strs_arr[i] != 0:
                        strs_arr_rem0[j] = strs_arr[i]
                        j += 1
                strs_arr_end_num = j  # 保存最后一个数的排列号不用再次取值
                for i in range(6):
                    strs_num_sum[strs_arr[i]] += 1
                for i in range(6):
                    if strs_arr[i] != 0:
                        str_sum += 1
                if str_sum == 3:
                    if strs_num_sum[1] == 1:
                        if strs_arr[4] == 1:
                            QMessageBox.information(self, '结果', '最后一根')
                        elif strs_num_sum[3] > 1:
                            QMessageBox.information(self, '结果', '最后一根蓝线')
                        else:
                            QMessageBox.information(self, '结果', '最后一根线')
                    else:
                        QMessageBox.information(self, '结果', '第二根')
                elif str_sum == 4:
                    if strs_num_sum[1] > 1 and serial_num_end % 2 == 1:
                        QMessageBox.information(self, '结果', '最后一根红线')
                    elif strs_num_sum[1] == 0 and strs_arr_rem0[strs_arr_end_num - 1] == 2:
                        QMessageBox.information(self, '结果', '第一根线')
                    elif strs_num_sum[3] == 1:
                        QMessageBox.information(self, '结果', '第一根线')
                    elif strs_num_sum[2] > 1:
                        QMessageBox.information(self, '结果', '最后一根线')
                    else:
                        QMessageBox.information(self, '结果', '第二根线')
                elif str_sum == 5:
                    if strs_arr_rem0[strs_arr_end_num - 1] == 4 and serial_num_end % 2 == 1:
                        QMessageBox.information(self, '结果', '第四根线')
                    elif strs_num_sum[1] == 1 and strs_num_sum[2] > 1:
                        QMessageBox.information(self, '结果', '第一根线')
                    elif strs_num_sum[4] == 0:
                        QMessageBox.information(self, '结果', '第二根线')
                    else:
                        QMessageBox.information(self, '结果', '第一根线')
                else:
                    if strs_num_sum[2] == 0 and serial_num_end % 2 == 1:
                        QMessageBox.information(self, '结果', '第三根线')
                    elif strs_num_sum[2] == 1 and strs_num_sum[0] > 1:
                        QMessageBox.information(self, '结果', '第四根线')
                    elif strs_num_sum[1] == 0:
                        QMessageBox.information(self, '结果', '最后一根线')
                    else:
                        QMessageBox.information(self, '结果', '第四根线')
    # 按钮模块
    def button_module(self):
        # 获取按钮模块个数
        times_but, ok = QInputDialog.getInt(self, '输入提示', '按钮模块个数')
        if ok:
            bat_num = None
            car_con = None
            frk_con = None
            for times in range(times_but):
                col_but, ok = QInputDialog.getInt(self, '输入提示', '白红黄蓝分别为1234')
                if not ok:
                    return
                char_but, ok = QInputDialog.getInt(self, '输入提示', '中止按住引爆分别为123')
                if not ok:
                    return
                if times == 0:
                    # 仅在第一次循环时询问电池数量、CAR状态和FRK状态
                    bat_num, ok = QInputDialog.getInt(self, '输入提示', '电池数量')
                    if not ok:
                        return
                # 使用 QMessageBox.question 获取 CAR 状态
                reply = QMessageBox.question(self, '输入提示', 'CAR 是否亮？', QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                   car_con = 1 
                else:
                   car_con = 0
                # 使用 QMessageBox.question 获取 FRK 状态
                reply = QMessageBox.question(self, '输入提示', 'FRK 是否亮？', QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                   frk_con = 1 
                else:
                   frk_con = 0
                if col_but == 4 and char_but == 1:
                    QMessageBox.information(self, '结果', '按住按钮，参考下文')
                elif bat_num > 1 and char_but == 3:
                    QMessageBox.information(self, '结果', '按下按钮并立即松开')
                elif col_but == 1 and car_con == 1:
                    QMessageBox.information(self, '结果', '按住按钮，参考下文')
                elif bat_num >= 2 and frk_con == 1:
                    QMessageBox.information(self, '结果', '按下按钮并立即松开')
                elif col_but == 3:
                    QMessageBox.information(self, '结果', '按住按钮，参考下文')
                elif char_but == 2 and col_but == 2:
                    QMessageBox.information(self, '结果', '按下按钮并立即松开')
                else:
                    QMessageBox.information(self, '结果', '按住按钮，参考下文')
                QMessageBox.information(self, '提示', '蓝色：在任意数位显示4时松开\n白色：在任意数位显示1时松开\n黄色：在任意数位显示5时松开\n其他颜色： 在任意数位显示1时松开')
    # 四色方块模块
    def four_color_block_module(self):
        # 获取四色方块模块数
        times_fbl, ok = QInputDialog.getInt(self, '输入提示', '四色方块模块数（默认无失误）')
        if ok:
            serial_num_aeiou = None
            for times in range(times_fbl):
                if times == 0:
                    # 仅在第一次循环时询问是否有元音字母
                    reply = QMessageBox.question(self, '输入提示', '是否有元音字母AEIOU？', QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                       serial_num_aeiou = 1 
                    else:
                       serial_num_aeiou = 0
                if serial_num_aeiou == 1:
                    QMessageBox.information(self, '结果', '红-蓝，蓝-红，绿-黄，黄-绿')
                else:
                    QMessageBox.information(self, '结果', '红-蓝，蓝-黄，绿-绿，黄-红')
    # 记忆模块
    def memory_module(self):
        # 获取记忆模块个数
        times_rem, ok = QInputDialog.getInt(self, '输入提示', '记忆模块个数')
        if ok:
            for times in range(times_rem):
                rem_stage = [0] * 5  # 大屏上的数字
                rem_stage_site = [0] * 5  # 按下的数字
                rem_stage_scre = [0] * 5  # 按下的位置

                rem_stage[0], ok = QInputDialog.getInt(self, '输入提示', '输入大屏上的数字')
                if not ok:
                    return
                if rem_stage[0] == 1:
                    rem_stage_scre[0], ok = QInputDialog.getInt(self, '输入提示', '按下第二个位置按钮并输入该数字')
                    rem_stage_site[0] = 2
                elif rem_stage[0] == 2:
                    rem_stage_scre[0], ok = QInputDialog.getInt(self, '输入提示', '按下第二个位置按钮并输入该数字')
                    rem_stage_site[0] = 2
                elif rem_stage[0] == 3:
                    rem_stage_scre[0], ok = QInputDialog.getInt(self, '输入提示', '按下第三个位置按钮并输入该数字')
                    rem_stage_site[0] = 3
                else:
                    rem_stage_scre[0], ok = QInputDialog.getInt(self, '输入提示', '按下第四个位置按钮并输入该数字')
                    rem_stage_site[0] = 3
                if not ok:
                    return

                rem_stage[1], ok = QInputDialog.getInt(self, '输入提示', '输入大屏上的数字')
                if not ok:
                    return
                if rem_stage[1] == 1:
                    rem_stage_site[1], ok = QInputDialog.getInt(self, '输入提示', '按下数字为4的按钮并输入该数字位置')
                    rem_stage_scre[1] = 4
                elif rem_stage[1] == 2:
                    rem_stage_scre[1], ok = QInputDialog.getInt(self, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                    rem_stage_site[1] = rem_stage_site[0]
                elif rem_stage[1] == 3:
                    rem_stage_scre[1], ok = QInputDialog.getInt(self, '输入提示', '按下第一个位置按钮并输入该数字')
                    rem_stage_site[1] = 1
                else:
                    rem_stage_scre[1], ok = QInputDialog.getInt(self, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                    rem_stage_site[1] = rem_stage_site[0]
                if not ok:
                    return

                rem_stage[2], ok = QInputDialog.getInt(self, '输入提示', '输入大屏上的数字')
                if not ok:
                    return
                if rem_stage[2] == 1:
                    rem_stage_site[2], ok = QInputDialog.getInt(self, '输入提示', f'按下数字为{rem_stage_scre[1]}的按钮并输入该数字位置')
                    rem_stage_scre[2] = rem_stage_scre[1]
                elif rem_stage[2] == 2:
                    rem_stage_site[2], ok = QInputDialog.getInt(self, '输入提示', f'按下数字为{rem_stage_scre[0]}的按钮并输入该数字位置')
                    rem_stage_scre[2] = rem_stage_scre[0]
                elif rem_stage[2] == 3:
                    rem_stage_scre[2], ok = QInputDialog.getInt(self, '输入提示', '按下第三个位置按钮并输入该数字')
                    rem_stage_site[2] = 3
                else:
                    rem_stage_site[2], ok = QInputDialog.getInt(self, '输入提示', '按下数字为4的按钮并输入该数字位置')
                    rem_stage_scre[2] = 4
                if not ok:
                    return

                rem_stage[3], ok = QInputDialog.getInt(self, '输入提示', '输入大屏上的数字')
                if not ok:
                    return
                if rem_stage[3] == 1:
                    rem_stage_scre[3], ok = QInputDialog.getInt(self, '输入提示', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                    rem_stage_site[3] = rem_stage_site[0]
                elif rem_stage[3] == 2:
                    rem_stage_scre[3], ok = QInputDialog.getInt(self, '输入提示', '按下第一个位置按钮并输入该数字')
                    rem_stage_site[3] = 1
                else:
                    rem_stage_scre[3], ok = QInputDialog.getInt(self, '输入提示', f'按下第{rem_stage_site[1]}个位置按钮并输入该数字')
                    rem_stage_site[3] = rem_stage_site[1]
                if not ok:
                    return

                rem_stage[4], ok = QInputDialog.getInt(self, '输入提示', '输入大屏上的数字')
                if not ok:
                    return
                if rem_stage[4] == 1:
                    QMessageBox.information(self, '结果', f'按下第{rem_stage_site[0]}个位置按钮并输入该数字')
                elif rem_stage[4] == 2:
                    QMessageBox.information(self, '结果', f'按下第{rem_stage_site[1]}个位置按钮并输入该数字')
                elif rem_stage[4] == 3:
                    QMessageBox.information(self, '结果', f'按下第{rem_stage_site[3]}个位置按钮并输入该数字')
                else:
                    QMessageBox.information(self, '结果', f'按下第{rem_stage_site[2]}个位置按钮并输入该数字')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())