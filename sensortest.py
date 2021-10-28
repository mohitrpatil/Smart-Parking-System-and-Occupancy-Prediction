import RPi.GPIO as GPIO
from time import sleep
import csv
import datetime as dt
import urllib.request, json 
##------------------------------------------------------------------------------------------------------------------------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(18,GPIO.OUT)  ##Parking 1 - RED LED
GPIO.setup(15,GPIO.OUT)  ##Parking 1 - GREEN LED
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
GPIO.setup(7,GPIO.OUT)   ##Parking 2 - RED LED
GPIO.setup(8,GPIO.OUT)   ##Parking 2 - GREEN LED
GPIO.setup(12,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(6,GPIO.OUT)   ##Parking 3 - RED LED
GPIO.setup(19,GPIO.OUT)  ##Parking 3 - GREEN LED


with urllib.request.urlopen("http://192.168.2.11/send_data.php?occ=SELECT%20*%20FROM%20parkinginfo%20where%20parkingid=1") as url:
    data = json.loads(url.read().decode())
    occ1=data["occupied"]
    maxi1=data["max"]
    occ1=int(occ1)
    maxi1=int(maxi1)

with urllib.request.urlopen("http://192.168.2.11/send_data.php?occ=SELECT%20*%20FROM%20parkinginfo%20where%20parkingid=2") as url:
    data = json.loads(url.read().decode())
    occ2=data["occupied"]
    maxi2=data["max"]
    occ2=int(occ2)
    maxi2=int(maxi2)

with urllib.request.urlopen("http://192.168.2.11/send_data.php?occ=SELECT%20*%20FROM%20parkinginfo%20where%20parkingid=3") as url:
    data = json.loads(url.read().decode())
    occ3=data["occupied"]
    maxi3=data["max"]
    occ3=int(occ3)
    maxi3=int(maxi3)   
    

while True:


    parking1_in=GPIO.input(17)
    parking1_out=GPIO.input(27)

    parking2_in=GPIO.input(24)
    parking2_out=GPIO.input(25)

    parking3_in=GPIO.input(12)
    parking3_out=GPIO.input(16)

    
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if(parking1_in == 0):
        if(occ1<maxi1-1):
                occ1=occ1+1
                percentocc1=occ1*100/maxi1
                print('parking1 percent: %0.2f'%percentocc1)
                row = [1,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc1]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=1 : occupied=%d,maximum=%d" %(occ1,maxi1))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ1)+"&pid=1").read()
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(18,GPIO.LOW)
                sleep(2)
        else:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
            print("Parking full")
            sleep(2)

    
##-----------------------------------------------------------------------------

    if(parking1_out == 0):
        if(occ1>0):
                occ1=occ1-1
                percentocc1=occ1*100/maxi1
                print('parking1 percent: %0.2f'%percentocc1)
                row = [1,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc1]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=1 : occupied=%d,maximum=%d" %(occ1,maxi1))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ1)+"&pid=1").read()
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(18,GPIO.LOW)
                sleep(2)
        else:
            print("Parking full")
            sleep(2)
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if(parking2_in == 0):
        if(occ2<maxi2-1):
                occ2=occ2+1
                percentocc2=occ2*100/maxi2
                print('parking2 percent: %0.2f'%percentocc2)
                row = [2,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc2]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=2 : occupied=%d,maximum=%d" %(occ2,maxi2))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ2)+"&pid=2").read()
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(7,GPIO.LOW)
                sleep(2)
        else:
            GPIO.output(7,GPIO.HIGH)
            GPIO.output(8,GPIO.LOW)            
            print("Parking full")
            sleep(2)

    
##-----------------------------------------------------------------------------

    if(parking2_out == 0):
        if(occ2>0):
                occ2=occ2-1
                percentocc2=occ2*100/maxi2
                print('parking2 percent: %0.2f'%percentocc2)
                row = [2,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc2]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=2 : occupied=%d,maximum=%d" %(occ2,maxi2))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ2)+"&pid=2").read()
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(7,GPIO.LOW)          
                sleep(2)
        else:
            print("Parking full")
            sleep(2)  

##------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if(parking3_in == 0):
        if(occ3<maxi3):
                occ3=occ3+1
                percentocc3=occ3*100/maxi3
                print('parking2 percent: %0.2f'%percentocc2)
                row = [3,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc3]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=3 : occupied=%d,maximum=%d" %(occ3,maxi3))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ3)+"&pid=3").read()
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(6,GPIO.LOW)
                sleep(2)
        else:
            GPIO.output(6,GPIO.HIGH)
            GPIO.output(19,GPIO.LOW)            
            print("Parking full")
            sleep(2)

    
##-----------------------------------------------------------------------------

    if(parking3_out == 0):
        if(occ3>0):
                occ3=occ3-1
                percentocc3=occ3*100/maxi3
                print('parking2 percent: %0.2f'%percentocc2)
                row = [3,dt.datetime.now().strftime("%a"),dt.datetime.now().strftime("%d %b %Y"),dt.datetime.now().strftime("%H"),percentocc3]    
                with open('sensorlog.csv', 'a') as f:
                    w = csv.writer(f)
                    w.writerow(row)
                

                print("ID=3 : occupied=%d,maximum=%d" %(occ3,maxi3))
                urllib.request.urlopen("http://192.168.2.11/add_data.php?occ="+str(occ3)+"&pid=3").read()
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(6,GPIO.LOW)
                sleep(2)
        else:
            print("Parking full")
            sleep(2)

##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
