# 横一直線に数字や文字を表示する(空白をつけて表示する)時に使う
def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)
