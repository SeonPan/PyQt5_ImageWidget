# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLabel, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
import untitled
import sys, os, math


class ImageWidget(QWidget):
    group_num = 1  # 图像列表当前组数（页数）
    list_files = []  # 图像文件路径集
    signal_order = pyqtSignal(str)  # 图像项目信号
    signal_page = pyqtSignal(int)  # 页数信号

    def __init__(self, parent=None, dir='./', col=1, w=10, h=None, suit=0):
        super(ImageWidget, self).__init__(parent)
        self.get_files(dir)
        self.col = col
        self.w = w
        self.suit = suit
        if h == None:
            self.h = self.w / self.col
        else:
            self.h = h
        self.setFixedSize(self.w, self.h)
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.show_images_list()  # 初次加载形状图像列表

    def get_files(self, dir):  # 储存当前页需加载的图像路径
        for file in os.listdir(path=dir):  # 读取图像路径
            if file.endswith('jpg') or file.endswith('png'):
                self.list_files.append(dir + "/" + file)

    def show_images_list(self):  # 加载图像列表
        for i in range(self.hbox.count()):  # 每次加载先清空内容，避免layout里堆积label
            self.hbox.itemAt(i).widget().deleteLater()
        # 设置分段显示图像，每col个一段
        group_num = self.group_num
        start = 0
        end = self.col
        if group_num > 1:
            start = self.col * (group_num - 1)
            end = self.col * group_num
        count = 0  # 记录当前页载入的label数
        width = int(self.w / self.col)  # 自定义label宽度
        height = self.h  # 自定义label高度
        for index, path in enumerate(self.list_files):  # group_num = 1 则加载前col个，以此类推
            if index < start:
                continue
            elif index == end:
                break
            # 按路径读取成QPixmap格式的图像，根据适应方式调整尺寸
            if self.suit==0:
                pix = QPixmap(path).scaled(width-2*self.col, height-4)
            elif self.suit==1:
                pix = QPixmap(path)
                pix = QPixmap(path).scaled(int(pix.width()*height/pix.height())-2*self.col, height-4)
            elif self.suit==2:
                pix = QPixmap(path)
                pix = QPixmap(path).scaled(width-2*self.col, int(pix.height()*width/pix.width())-4)
            label = MyLabel(index)
            label.setPixmap(pix)  # 加载图片
            label.setFixedWidth(int(self.w / self.col)-5)
            self.hbox.addWidget(label)   # 在水平布局中添加自定义label
            label.signal_order.connect(self.choose_image)  # 绑定自定义label点击信号
            count += 1
        if not count==self.col:
            for i in range(self.col - count):
                label = QLabel()
                label.setFixedWidth(int(self.w / self.col))
                self.hbox.addWidget(label)  # 在水平布局中添加空label补位

    def turn_page(self, num):  # 图像列表翻页
        flag = len(self.list_files)
        if self.group_num == 1 and num == -1:  # 到首页时停止上翻
            QMessageBox.about(self, "Remind", "This is the first page!")
        elif (self.group_num == math.ceil(flag/self.col) and num == 1) or flag==0:  # 到末页时停止下翻
            QMessageBox.about(self, "Remind", "No more image! ")
        else:
            self.group_num +=  num  # 翻页
        self.signal_page.emit(self.group_num)
        self.show_images_list()  # 重新加载图像列表

    def choose_image(self, index):  # 选择图像
        self.signal_order.emit(self.list_files[index])

class MyLabel(QLabel):  # 自定义label，用于传递是哪个label被点击了
    signal_order = pyqtSignal(int)

    def __init__(self, order=None):
        super(MyLabel, self).__init__()
        self.order = order
        self.setStyleSheet("border-width: 2px; border-style: solid; border-color: gray")

    def mousePressEvent(self, e):  # 重载鼠标点击事件
        self.signal_order.emit(self.order)

class testForm(QWidget, untitled.Ui_Form):
    def __init__(self):
        super(testForm, self).__init__()
        self.setupUi(self)
        # 添加自定义图像组件
        self.image_widget = ImageWidget(self, dir='./shape_images', col=4, w=600)
        self.image_widget.move(20, 100)
        self.pB_previous.clicked.connect(lambda: self.image_widget.turn_page(-1))
        self.pB_next.clicked.connect(lambda: self.image_widget.turn_page(1))  # 图像列表翻页
        self.image_widget.signal_order.connect(self.change_path)
        self.image_widget.signal_page.connect(self.change_page)

    def change_path(self, path):
        self.lineEdit_path.setText(path)

    def change_page(self, index):
        self.lineEdit_page.setText(f"第{index}页")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = testForm()
    win.show()
    sys.exit(app.exec())
