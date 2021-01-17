import sys
import os
import time
import threading
import json
import random
import getpass

gameover=True

def baslangic():
    global xsonkonum
    os.system('cls')
    x[30+780] = "#"
    xsonkonum=x.index("#")
    print("*x")
    time.sleep(0.18)

def clearcmd():
    sys.stdout.write("\x1b[2J\x1b[H")

yonlistesi=[]
xsonkonum=""
kenara_gelince_olme_listesi=[]
kendine_degince_olme_listesi=[]
yenen_yem_listesi=[]
yenen_yem_sayisi=0
konum_gecmisi=[]

def yondegistirme():
    while True:
        if gameover ==False:
            break
        elif gameover== True:

            yon=getpass.getpass(prompt="*"*120)
            if yon == "a" or yon == "d" or yon == "w" or yon == "s":
                yonlistesi.append(yon)
thread1_yondegistirme=threading.Thread(target=yondegistirme)

def sagahareket_ilk():
    global xsonkonum
    def pozisyonsagyeni(h):
        global kenara_gelince_olme_listesi
        global konum_gecmisi
        global yenen_yem_listesi
        kenara_gelince_olme_listesi.append(x[h])
        yenen_yem_listesi.append(x[h])
        x[h]="#"
        konum_gecmisi.append(xsonkonum+k1)
        if len(konum_gecmisi) >1:
            x[konum_gecmisi[-2-yenen_yem_sayisi]] = " "
    k1=0
    while gameover:
        pozisyonsagyeni(xsonkonum+k1)
        print(*x)
        time.sleep(0.18)
        try:
            if yonlistesi[0] == "s":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1
                clearcmd()
                asagihareket()
            if yonlistesi[0] == "w":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1
                clearcmd()
                yukarihareket()
        except:
            pass
            clearcmd()
        k1+=1
thread4_sagahareket_ilk=threading.Thread(target=sagahareket_ilk)
def sagahareket():
    global xsonkonum
    def pozisyonsagyeni(h):
        global kenara_gelince_olme_listesi
        global konum_gecmisi
        global yenen_yem_listesi
        global kendine_degince_olme_listesi
        kenara_gelince_olme_listesi.append(x[h+1])
        kendine_degince_olme_listesi.append(x[h+1])
        yenen_yem_listesi.append(x[h+1])
        x[h+1]="#"
        konum_gecmisi.append(xsonkonum+k1+1)
        x[konum_gecmisi[-2-yenen_yem_sayisi]] = " "
    k1=0
    while gameover:
        pozisyonsagyeni(xsonkonum+k1)
        print(*x)
        time.sleep(0.18)
        try:
            if yonlistesi[0] == "s":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1+1
                clearcmd()
                asagihareket()
            elif yonlistesi[0] == "w":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1+1
                clearcmd()
                yukarihareket()
            elif yonlistesi[0] == "a" or yonlistesi[0] == "d":
                del yonlistesi[0]
                clearcmd()
                pass
        except:
            pass
            clearcmd()
        k1+=1
def solahareket():
    global xsonkonum
    def pozisyonsolayeni(h):
        global kenara_gelince_olme_listesi
        global konum_gecmisi
        global yenen_yem_listesi
        global kendine_degince_olme_listesi
        kenara_gelince_olme_listesi.append(x[h-1])
        kendine_degince_olme_listesi.append(x[h-1])
        yenen_yem_listesi.append(x[h-1])
        x[h-1]="#"
        konum_gecmisi.append(xsonkonum-k1-1)
        x[konum_gecmisi[-2-yenen_yem_sayisi]] = " "
    k1=0
    while gameover:
        pozisyonsolayeni(xsonkonum-k1)
        print(*x)
        time.sleep(0.18)
        try:
            if yonlistesi[0] == "s":
                del yonlistesi[0]
                xsonkonum = xsonkonum-k1-1
                clearcmd()
                asagihareket()
            elif yonlistesi[0] == "w":
                del yonlistesi[0]
                xsonkonum = xsonkonum-k1-1
                clearcmd()
                yukarihareket()
            elif yonlistesi[0] == "a" or yonlistesi[0] == "d":
                del yonlistesi[0]
                clearcmd()
                pass
        except:
            pass
            clearcmd()
        k1+=1
def asagihareket():
    global xsonkonum
    def pozisyonasagiyeni(h):
        global kenara_gelince_olme_listesi
        global konum_gecmisi
        global yenen_yem_listesi
        global kendine_degince_olme_listesi
        kenara_gelince_olme_listesi.append(x[h+60])
        kendine_degince_olme_listesi.append(x[h+60])
        yenen_yem_listesi.append(x[h+60])
        x[h+60]="#"
        konum_gecmisi.append(xsonkonum+k1+60)
        x[konum_gecmisi[-2-yenen_yem_sayisi]] = " "
    k1=0
    while gameover:
        pozisyonasagiyeni(xsonkonum+k1)
        print(*x)
        time.sleep(0.18)
        try:
            if yonlistesi[0] == "d":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1+60
                clearcmd()
                sagahareket()
            elif yonlistesi[0] == "a":
                del yonlistesi[0]
                xsonkonum = xsonkonum+k1+60
                clearcmd()
                solahareket()
            elif yonlistesi[0] == "w" or yonlistesi[0] == "s":
                del yonlistesi[0]
                clearcmd()
                pass
        except:
            pass
            clearcmd()
        k1+=60
def yukarihareket():
    global xsonkonum
    def pozisyonyukariyeni(h):
        global kenara_gelince_olme_listesi
        global konum_gecmisi
        global yenen_yem_listesi
        global kendine_degince_olme_listesi
        kenara_gelince_olme_listesi.append(x[h-60])
        kenara_gelince_olme_listesi.append(x[h-60])
        yenen_yem_listesi.append(x[h-60])
        x[h-60]="#"
        konum_gecmisi.append(xsonkonum-k1-60)
        x[konum_gecmisi[-2-yenen_yem_sayisi]] = " "
    k1=0
    while gameover:
        pozisyonyukariyeni(xsonkonum-k1)
        print(*x)
        time.sleep(0.18)
        try:
            if yonlistesi[0] == "d":
                del yonlistesi[0]
                xsonkonum = xsonkonum-k1-60
                clearcmd()
                sagahareket()

            elif yonlistesi[0] == "a":
                del yonlistesi[0]
                xsonkonum = xsonkonum-k1-60
                clearcmd()
                solahareket()
            elif yonlistesi[0] == "w" or yonlistesi[0] == "s":
                del yonlistesi[0]
                clearcmd()
                pass
        except:
            pass
            clearcmd()
        k1+=60

def kenara_gelince_olme():
    global gameover
    while True:
        if "-" in kenara_gelince_olme_listesi:
            gameover=False
            break
thread2_kenara_gelince_olme=threading.Thread(target=kenara_gelince_olme)

def kendine_degince_olme():
    global gameover
    while True:
        if "#" in kendine_degince_olme_listesi:
            gameover=False
            break
thread6_kendine_degince_olme=threading.Thread(target=kendine_degince_olme)

def random_yem_baslangic():
    for z in range(10):
        y=0
        while x[y] == "-" and "#":
            y = random.randint(0,1679)
        x[y] = "s"
def random_yem_ekleme():
    while True:
        if gameover ==False:
            break
        elif gameover== True:
            if x.count("s") <10:
                y=0
                while x[y] == "-" and "#":
                    y=random.randint(0,1679)
                x[y] = "s"
thread3_random_yem_ekleme=threading.Thread(target=random_yem_ekleme)

def yenen_yem():
    global yenen_yem_sayisi
    while True:
        if gameover ==False:
            break
        elif gameover== True:
            yenen_yem_sayisi = yenen_yem_listesi.count("s")
thread5_yenen_yem=threading.Thread(target=yenen_yem)

def gameover_():
    while True:
        if gameover == False:
            print("GG WP")
            print(f"yenilen yem sayısı: {yenen_yem_listesi.count('s')}")
            print(f"son uzunluk: {yenen_yem_listesi.count('s')+1}")
            print(f"skor: {yenen_yem_listesi.count('s')*10}")
            break
thread7_gameover_=threading.Thread(target=gameover_)

with open('template.json',"r") as f:
    x= json.load(f)

thread1_yondegistirme.start()
baslangic()
thread2_kenara_gelince_olme.start()
thread6_kendine_degince_olme.start()
thread7_gameover_.start()
random_yem_baslangic()
thread3_random_yem_ekleme.start()
thread5_yenen_yem.start()
thread4_sagahareket_ilk.start()










