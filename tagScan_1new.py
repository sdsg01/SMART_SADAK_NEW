#import time
from database1 import *
#from datetime import datetime
#from get_Analysis import *
import get_Analysis
# from dateutil.tz import *

while True:
    temp = input('Type what you want to send, hit enter:\r\n')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #curr = datetime.now()
    # print(curr)

    veh1 = scan_details(temp, 1, current_time)
    veh1.add()
    str = input("Do you want traffic congestion data? yes/no\n")
    if(str == "yes"):
        #obj = get_analysis()
        obj = get_Analysis.get_analysis()
        obj.show_data()
'''
if(veh_d.get_class_by_rfid(temp) == 'Heavy'):
    hr_chk = t.tm_hour
    #offence_type = "heavy_duty"
    if(hr_chk<6) or (hr_chk>15):0005150446
    
        o1 = offences(temp,current_time,'heavy_duty')
        o1.add()

traffic_signal = None

signal = db.reference('/Traffic_light').get()
#l = signal.listen(signal_listener)
#l.close()

if(signal == 'red'):
    o2 = offences(temp,current_time,"signal_violation")#offence_type)
    o2.add()
    #show_message('signal_violation')
    client.messages.create(to="+919767034552",
                   from_="+12512203113",
                   body="Dear citizen, your vehicle has been detected in a traffic signal violation!!")

'''

'''
while 1:
    #init_serial()
    temp = input('Type what you want to send, hit enter:\r\n')
    database.add(temp)
    tmp = input('Type ID to be retreived :\n')
    #print(type(tmp))
    database.get_by_rfid(tmp)
    #ser.write(temp)         #Writes to the SerialPort
    #print(temp)
'''
