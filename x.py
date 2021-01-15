import os
import time
x=list("   |"*900)
os.system('cls' if os.name == 'nt' else 'clear')
def saghareket():


    def pozisyonsagyeni(h):
        x[h+1]="o"
        x[h-3]=" "
    k1=0

    while True:

        pozisyonsagyeni(32+k1)
        n1=0
        with open('zxc.txt','w') as f:
            pass

        for y in range(15):
            with open('zxc.txt','a') as f:
                f.write(f"{''.join(x[n1:60+n1])}\n")
            n1+=60
        with open('zxc.txt', "r") as f:
            ekran=f.read()
        print(ekran)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        k1+=4
saghareket()









