from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
import sys,random,time
from threading import Thread
class oyun_ekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ekran_y=548
        self.ekran_x=890

        self.setWindowTitle("iki kişilik top oyunu   version : 2.1")
        self.setGeometry(100,100,self.ekran_x,self.ekran_y)
        self.setMinimumSize(self.ekran_x,self.ekran_y)
        self.setMaximumSize(self.ekran_x, self.ekran_y)
        self.setAutoFillBackground(True)
        self.pa=self.palette()
        self.pa.setColor(self.backgroundRole(),Qt.black)
        self.setPalette(self.pa)
        dum = Thread(target=self.keyPressEvent)
        dum.start()
        self.içerik()

    def içerik(self):

        ########################    kazanmak için
        self.kazan=QLabel(self)
        self.E = QPushButton(self)
        self.E.setGeometry(0,0,0,0)
        ###################################################
        ##################     başlangicta olack oplanlar
        self.sure=0
        self.scor_1 = 0
        self.scor_2 = 0
        self.yazı_1=QLabel(self)
        self.yazı_1.setText(f"""<font color="#00ff00" size="6"> Scor : {self.scor_1}</font>""")
        self.yazı_1.setGeometry(20,10,300,50)
        self.yazı_2 = QLabel(self)
        self.yazı_2.setText(f"""<font color="#00ff00" size="6"> Sure : {self.sure}</font>""")
        self.yazı_2.setGeometry(700, 10, 300, 50)
        self.yazı_3 = QLabel(self)
        self.yazı_3.setText(f"""<font color="#00ff00" size="6"> Scor : {self.scor_2}</font>""")
        self.yazı_3.setGeometry(1350, 10, 500, 50)
        self.yazı_4 = QLabel(self)
        self.yazı_4.setText(f"""<font color="#00ff00" size="4">Tüm hakları saklıdır © 2020 | yalcınyazılımcılık</font>""")
        self.yazı_4.setGeometry(50,self.ekran_y-70, 500, 50)
        self.buton_1y=300
        self.buton_2y=300
        self.button_1=QPushButton(self)
        self.button_1.setText("1")
        self.button_1.setGeometry(50,self.buton_1y,30,200)
        self.button_2 = QPushButton(self)
        self.button_2.setText("2")
        self.button_2.setGeometry(self.ekran_x-90,self.buton_2y, 30, 200)
        ########################   top içerikleri
        self.top_at()
        self.ivme=0
        self.top_x=750
        self.top_y=400
        self.top = QPushButton(self)
        self.top.setText("top")
        self.top.setGeometry(self.top_x,self.top_y,40,40)
        self.top_oyna=QTimer()
        self.top_oyna.timeout.connect(self.top_hareket)
        self.top_oyna.start(30-self.ivme)
        self.sn= QTimer()
        self.sn.timeout.connect(self.sre)
        self.sn.start(1000)
        self.show()
    def sre(self):
        self.sure+=1
    def top_at(self):
        ra = random.randint(0, 1)
        raa = random.randint(0, 1)
        if ra == 0:
            self.işaret_x = 10
        else:
            self.işaret_x = -10
        if ra == 1:
            self.işaret_y = 10
        else:
            self.işaret_y = -10
    def cubuklar(self,buton,x):
        def bak_hepsıne_y(basla,bitis):
            for i in range(basla,bitis):
                if self.top_y==i:
                    return True
        if x=="1":
            if bak_hepsıne_y(buton,buton+200)and self.top_x <= 80 and self.top_x>=50:
                return True
        elif x=="2":
                if bak_hepsıne_y(buton, buton + 200) and self.top_x <= self.ekran_x-120 and self.top_x >= self.ekran_x-140 :
                    return True
    def bittir(self):
        self.kazan.setText(f"""<font color="#00ff00" size="6"> ------------  KAZANAN OYUNCU --------------- </font><br><br><br>
                                <font color="#00ff00" size="6">oyuncu 1 : {self.scor_1}    ________    oyuncu 2 :  {self.scor_2}</font> <br><br>
                                <font color="#00ff00" size="6"> ----------------  GECEN SURE  :  {self.sure} -------------- </font><br><br><br>
                                <font color="#00ff00" size="6"> ----------  Tekrar oynamak ıstermisiniz -----</font><br><br>
        """)
        self.kazan.setGeometry(500,100,500,500)
        self.E.setText( "EVET ")
        self.E.setGeometry(700,500,100,50)

        self.E.clicked.connect(self.basla)
        self.top_oyna.stop()
        self.sn.stop()

    def basla(self):
        self.ivme = 0
        self.top_x = 750
        self.top_y = 400
        self.buton_1y = 300
        self.buton_2y = 300
        self.sure = 0
        self.scor_1 = 0
        self.scor_2 = 0
        self.E.setGeometry(0, 0, 0, 0)
        self.top_at()
        self.kazan.setText("")
        self.button_2.setGeometry(self.ekran_x-90,self.buton_2y, 30, 200)
        self.button_1.setGeometry(50, self.buton_1y, 30, 200)
        self.top_oyna.start(30-self.ivme)
        self.sn.start(1000)
    def top_hareket(self):
        self.top_x+=self.işaret_x
        self.top_y+=self.işaret_y

        if self.top_x==self.ekran_x-40:
            self.işaret_x=0
            self.işaret_y = 0
            self.bittir()
        elif self.top_x==0:
            self.işaret_x=0
            self.işaret_y = 0
            self.bittir()
        elif self.top_y==self.ekran_y-40:
            self.işaret_y=-10
        elif self.top_y==0:
            self.işaret_y=+10
        if self.cubuklar(self.buton_1y,"1"):
            self.ivme+=1
            self.scor_1 += 1
            self.işaret_x=10
        if self.cubuklar(self.buton_2y,"2"):
            self.ivme+=1
            self.scor_2+=1
            self.işaret_x = -10
        self.top.setGeometry(self.top_x, self.top_y, 40, 40)
        self.yazı_3.setText(f"""<font color="#00ff00" size="6"> Scor : {self.scor_2}</font>""")
        self.yazı_2.setText(f"""<font color="#00ff00" size="6"> Sure : {self.sure}</font>""")
        self.yazı_1.setText(f"""<font color="#00ff00" size="6"> Scor : {self.scor_1}</font>""")
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==87:
            if self.buton_1y<20:
                pass
            else:
                self.buton_1y -=10
                self.button_1.setGeometry(50, self.buton_1y, 30,200)
        if QKeyEvent.key() == 83:
            if self.buton_1y > self.ekran_y-228:
                pass
            else:
                self.buton_1y += 10
                self.button_1.setGeometry(50, self.buton_1y, 30, 200)
        if QKeyEvent.key()==56:
            if self.buton_2y<20:
                pass
            else:
                self.buton_2y -=10
                self.button_2.setGeometry(self.ekran_x-90, self.buton_2y, 30,200)
        if QKeyEvent.key() == 50:
            if self.buton_2y > self.ekran_y-228:
                pass
            else:
                self.buton_2y += 10
                self.button_2.setGeometry(self.ekran_x-90, self.buton_2y, 30, 200)


app=QApplication(sys.argv)
oyun=oyun_ekran()
oyun.show()
sys.exit(app.exec_())