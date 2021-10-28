
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
import urllib.request,json

data = pd.read_csv("sensorlog.csv")

x = data.iloc[:,[0,1,3]]
y = data.iloc[:,[4]]
day = datetime.datetime.now()
day = day.strftime("%A")

#print(day)

if day == 'Sunday':
    cur_day = 0
elif day == 'Monday':
    cur_day = 1
elif day == 'Tuesday':
    cur_day = 2
elif day == 'Wednesday':
    cur_day = 3
elif day == 'Thursday':
    cur_day = 4
elif day == 'Friday':
    cur_day = 5
elif day == 'Saturday':
    cur_day = 6

DAY = {'Sun': 0,'Mon': 1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6}
x.day = [DAY[item] for item in x.day]


#print(x)

model = LinearRegression()
model.fit(x,y)

##x_test = np.array([[1,2,5]])
##y_pred = model.predict(x_test)
##print(y_pred[0][0])

print('Parking 1:')
for i in range(24):
    x_test = np.array([[1,cur_day,i]])
    y_pred = model.predict(x_test)  
    urllib.request.urlopen("http://192.168.2.11/add_data1.php?occ="+str(y_pred[0][0])+"&pid="+str(i)).read()
    print(i,y_pred[0][0])

print('Parking 2:')
for i in range(24):
    x_test = np.array([[2,cur_day,i]])
    y_pred = model.predict(x_test)    
    print(i,y_pred[0][0])
    urllib.request.urlopen("http://192.168.2.11/add_data2.php?occ="+str(y_pred[0][0])+"&pid="+str(i)).read()

print('Parking 3:')
for i in range(24):
    x_test = np.array([[3,cur_day,i]])
    y_pred = model.predict(x_test)    
    print(i,y_pred[0][0])
    urllib.request.urlopen("http://192.168.2.11/add_data3.php?occ="+str(y_pred[0][0])+"&pid="+str(i)).read()

##
##Parking 1:
##0 18.693284449410093
##1 21.16536783077128
##2 23.637451212132472
##3 26.10953459349366
##4 28.58161797485485
##5 31.053701356216038
##6 33.525784737577226
##7 35.99786811893842
##8 38.46995150029961
##9 40.942034881660796
##10 43.41411826302199
##11 45.88620164438318
##12 48.358285025744365
##13 50.83036840710555
##14 53.30245178846675
##15 55.774535169827935
##16 58.24661855118912
##17 60.71870193255031
##18 63.1907853139115
##19 65.66286869527269
##20 68.13495207663388
##21 70.60703545799507
##22 73.07911883935625
##23 75.55120222071744
##Parking 2:
##0 18.435982609061202
##1 20.90806599042239
##2 23.38014937178358
##3 25.85223275314477
##4 28.324316134505956
##5 30.796399515867147
##6 33.26848289722834
##7 35.740566278589526
##8 38.21264965995071
##9 40.6847330413119
##10 43.156816422673096
##11 45.62889980403429
##12 48.10098318539548
##13 50.573066566756665
##14 53.04514994811785
##15 55.51723332947904
##16 57.98931671084023
##17 60.461400092201416
##18 62.9334834735626
##19 65.40556685492379
##20 67.87765023628498
##21 70.34973361764617
##22 72.82181699900737
##23 75.29390038036856
##Parking 3:
##0 18.17868076871231
##1 20.6507641500735
##2 23.12284753143469
##3 25.594930912795878
##4 28.06701429415707
##5 30.539097675518256
##6 33.01118105687945
##7 35.48326443824064
##8 37.955347819601826
##9 40.427431200963014
##10 42.8995145823242
##11 45.371597963685396
##12 47.84368134504658
##13 50.31576472640777
##14 52.787848107768966
##15 55.25993148913015
##16 57.73201487049134
##17 60.20409825185253
##18 62.676181633213716
##19 65.14826501457492
##20 67.6203483959361
##21 70.09243177729729
##22 72.56451515865848
##23 75.03659854001967
