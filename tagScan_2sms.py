import time, sys
from database1 import *
from datetime import datetime
import traceback
import requests
from tkinter import *

global SIGNAL_FLAG
#global SPEED_FLAG
#from twilio.rest import Client

#client = Client("AC9013a67233fa74a0a2630e3b8794f339", "7619f91e69f61219a386290e65478239")

url = "https://www.fast2sms.com/dev/bulk"


while True:
    SIGNAL_FLAG = True
    #SPEED_FLAG = True
    temp = input('Type what you want to send, hit enter:\r\n')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t) 
    curr = datetime.now()

    veh = scan_details(temp, 2, current_time)
    veh.add()

    veh_d = vehicle_details(None, None, None, None, None, None)
    if(veh_d.get_by_rfid()=="0014508966"):
        ref.update({'Signal Flag': False})
    else:

        try:
            #Overspeeding offence
            speed = get_speed(temp, 1, 2, 45)
            print("Current Speed of vehicle is : ", speed," cm/seconds")
            
            m= Tk()
            x = speed
            m.minsize(width=600, height=100)
            l = Label(m, text=x,font=('Helvetica', 24),bg="black",fg="white", justify = CENTER)
            l.pack()    
            m.after(3000, lambda: m.destroy()) 
            m.mainloop()
            


            if(speed > 12):
                o_speed = offences(temp, current_time, 'overspeeding')
                o_speed.add()
                print("Overspeeding vehicle.\n")
                print("...Sending message...")
                #SPEED_FLAG = False
                payload = "sender_id=FSTSMS&message=Dear Citizen, Overspeeding detected! &language=english&route=p&numbers=9765373859"
                headers = {
                    'authorization': "GoWcnFgAzQ6jelCZ75UiXV0NqvwuhxBk2Ts9bHdaSD8ROtE43L1UtkPjhGTwu4RX7BzfYZIqb0Qy2CKF",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                print("Message sent to offender.\n")
                # client.messages.create(to="+919767034552",
                #                      from_="+12512203113",
                #                     body="Dear citizen, your vehicle has been detected overspeeding!!")
        except:
            #Wrong Way offence
            #traceback.print_exc(file=sys.stdout)
            #if(SPEED_FLAG):
            o_ww = offences(temp, current_time, 'wrong_way')
            o_ww.add()
            print("Wrong direction on road.\n")
            print("...Sending message...")
            payload = "sender_id=FSTSMS&message=Dear Citizen, Wrong way rule violation at Jyoti Talkies Chowk, Zone-1 &language=english&route=p&numbers=9765373859"
            headers = {
                'authorization': "GoWcnFgAzQ6jelCZ75UiXV0NqvwuhxBk2Ts9bHdaSD8ROtE43L1UtkPjhGTwu4RX7BzfYZIqb0Qy2CKF",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print("Message sent to offender.\n")
            # client.messages.create(to="+919767034552",
            #                      from_="+12512203113",
            #                     body="Dear citizen, your vehicle has been detected in Jyoti Talkies Chowk, Zone-1, MP Nagar.")
            SIGNAL_FLAG = False


        #Heavy vehicle offence
        if(veh_d.get_class_by_rfid(temp) == 'Heavy'):
            hr_chk = t.tm_hour
            #offence_type = "heavy_duty"
            if(hr_chk<23) or (hr_chk>6):
                o1 = offences(temp,current_time,'heavy_duty')
                o1.add()
                print("Heavy Duty vehicle driving at illegal times.\n")
                print("...Sending message...")
                payload = "sender_id=FSTSMS&message=Dear Citizen, Heavy Vehicle detected! &language=english&route=p&numbers=9765373859"
                headers = {
                    'authorization': "GoWcnFgAzQ6jelCZ75UiXV0NqvwuhxBk2Ts9bHdaSD8ROtE43L1UtkPjhGTwu4RX7BzfYZIqb0Qy2CKF",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                print("message sent to offender.\n")
                #client.messages.create(to="+919767034552",
                 #                      from_="+12512203113",
                  #                     body="Dear citizen, your vehicle has been detected in a no heavy-vehicle zone!!")

        #Traffic signal offence
        if(SIGNAL_FLAG):
            signal = db.reference('/Traffic_light').get()
            if(signal == 'red'):
                o2 = offences(temp,current_time,"signal_violation")#offence_type)
                o2.add()
                print("Traffic Signal violated.\n")
                print("...Sending message...")
                payload = "sender_id=FSTSMS&message=Dear Citizen, Signal Violation! &language=english&route=p&numbers=9765373859"
                headers = {
                    'authorization': "GoWcnFgAzQ6jelCZ75UiXV0NqvwuhxBk2Ts9bHdaSD8ROtE43L1UtkPjhGTwu4RX7BzfYZIqb0Qy2CKF",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                print("Message sent to offender.\n")

        #show_message('signal_violation')
    #    client.messages.create(to="+919767034552",
    #                   from_="+12512203113",
    #                   body="Dear citizen, your vehicle has been detected in a traffic signal violation!!")
    #if(SIGNAL_FLAG):
     #  remove(temp, 1)

    #remove(temp, 2)

