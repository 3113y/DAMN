from PyQt5.QtWidgets import QInputDialog, QMessageBox

def line_module(parent):
    times_str, ok = QInputDialog.getInt(parent, '输入提示', '线路模块个数', 1)
    if ok:
        serial_num_end = 0
        for times in range(times_str):
            strs_arr = [0] * 6
            for i in range(6):
                str_col_box = QMessageBox(parent)
                str_col_box.setWindowTitle('输入提示')
                str_col_box.setText('线的颜色？')
                white_button = str_col_box.addButton("白色", QMessageBox.ActionRole)
                red_button = str_col_box.addButton("红色", QMessageBox.ActionRole)
                yellow_button = str_col_box.addButton("黄色", QMessageBox.ActionRole)
                blue_button = str_col_box.addButton("蓝色", QMessageBox.ActionRole)
                black_button = str_col_box.addButton("黑色", QMessageBox.ActionRole)
                cancel_button = str_col_box.addButton(QMessageBox.Cancel)
                reply = str_col_box.exec_()
                if reply == QMessageBox.Cancel:
                    parent.switch_module()  # 返回主菜单
                    return
                if str_col_box.clickedButton() == white_button:
                    strs_arr[i] = 1
                elif str_col_box.clickedButton() == red_button:
                    strs_arr[i] = 2
                elif str_col_box.clickedButton() == yellow_button:
                    strs_arr[i] = 3
                elif str_col_box.clickedButton() == blue_button:
                    strs_arr[i] = 4
                elif str_col_box.clickedButton() == black_button:
                    strs_arr[i] = 5
            if times == 0:
                serial_num_end, ok = QInputDialog.getInt(parent, '输入提示', '输入序列号末位')
                if not ok:
                    return
            str_sum = 0
            strs_num_sum = [0] * 6
            strs_arr_rem0 = [0] * 6
            j = 0
            for i in range(6):
                if strs_arr[i] != 0:
                    strs_arr_rem0[j] = strs_arr[i]
                    j += 1
            strs_arr_end_num = j
            for i in range(6):
                strs_num_sum[strs_arr[i]] += 1
            for i in range(6):
                if strs_arr[i] != 0:
                    str_sum += 1
            if str_sum == 3:
                if strs_num_sum[1] == 1:
                    if strs_arr[4] == 1:
                        QMessageBox.information(parent, '结果', '最后一根')
                    elif strs_num_sum[3] > 1:
                        QMessageBox.information(parent, '结果', '最后一根蓝线')
                    else:
                        QMessageBox.information(parent, '结果', '最后一根线')
                else:
                    QMessageBox.information(parent, '结果', '第二根')
            elif str_sum == 4:
                if strs_num_sum[1] > 1 and serial_num_end % 2 == 1:
                    QMessageBox.information(parent, '结果', '最后一根红线')
                elif strs_num_sum[1] == 0 and strs_arr_rem0[strs_arr_end_num - 1] == 2:
                    QMessageBox.information(parent, '结果', '第一根线')
                elif strs_num_sum[3] == 1:
                    QMessageBox.information(parent, '结果', '第一根线')
                elif strs_num_sum[2] > 1:
                    QMessageBox.information(parent, '结果', '最后一根线')
                else:
                    QMessageBox.information(parent, '结果', '第二根线')
            elif str_sum == 5:
                if strs_arr_rem0[strs_arr_end_num - 1] == 4 and serial_num_end % 2 == 1:
                    QMessageBox.information(parent, '结果', '第四根线')
                elif strs_num_sum[1] == 1 and strs_num_sum[2] > 1:
                    QMessageBox.information(parent, '结果', '第一根线')
                elif strs_num_sum[4] == 0:
                    QMessageBox.information(parent, '结果', '第二根线')
                else:
                    QMessageBox.information(parent, '结果', '第一根线')
            else:
                if strs_num_sum[2] == 0 and serial_num_end % 2 == 1:
                    QMessageBox.information(parent, '结果', '第三根线')
                elif strs_num_sum[2] == 1 and strs_num_sum[0] > 1:
                    QMessageBox.information(parent, '结果', '第四根线')
                elif strs_num_sum[1] == 0:
                    QMessageBox.information(parent, '结果', '最后一根线')
                else:
                    QMessageBox.information(parent, '结果', '第四根线')
    parent.switch_module()