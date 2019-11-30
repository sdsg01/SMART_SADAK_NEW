import time
from database import *
#global CHECK
global flag1
global CHECK
CHECK = False
flag1 = False
class signal:

    def show_signal(self):


        while 1:
            global CHECK
            traffic_light = 'red'
            print(traffic_light)
            ref.update({'Traffic_light': traffic_light})
            red(3)
            #print(CHECK)

            if(CHECK):
                green1(9)
            traffic_light = 'green'

            print(traffic_light)
            ref.update({'Traffic_light': traffic_light})
            green(3)

            if(CHECK):
                green1(7)
            traffic_light = 'yellow'
            print(traffic_light)
            ref.update({'Traffic_light': traffic_light})
            amber(3)
            if(CHECK):
                green1(9)

def red(a):
    for i in range(a):

        # from ty import EMER_FLAG
        ref1 = db.reference('Signal Flag')
        if (ref1.get()):

            global CHECK
            CHECK = True
            #print(CHECK)
            break
        time.sleep(0.05)
        light = "red"
        ref.update({'Traffic_light': light})

def amber(a):
    for i in range(a):

        # from ty import EMER_FLAG
        ref1 = db.reference('Signal Flag')
        if (ref1.get()):
            global CHECK
            CHECK = True
            break

        time.sleep(0.05)
        light = "yellow"
        ref.update({'Traffic_light': light})


def green(a):
    for i in range(a):

        # from ty import EMER_FLAG
        ref1 = db.reference('Signal Flag')
        #print(ref1.get())
        if (ref1.get()):
            global CHECK
            CHECK = True
            break
        time.sleep(0.05)
        light = "green"
        ref.update({'Traffic_light': light})

def green1(a):
    
    ref1 = db.reference('Signal Flag')
    print("....................")
    print("green")
    ref.update({'Traffic_light': "green"})
    while(ref1.get()):

        time.sleep(2)
    time.sleep(1)
    global CHECK
    CHECK = False


if (__name__=='__main__'):
    lf = signal()
    lf.show_signal()



