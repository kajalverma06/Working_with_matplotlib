#Q-1) Write a Python program to plot two or more lines and set the line markers.
import matplotlib.pyplot as plt
x1 = [10,20,30,40]
y1 = [20,40,10,40]
plt.plot(x1,y1,label='Line-1',color="Green",linestyle='dashdot',linewidth=5,marker='o',markerfacecolor='Blue',
         markersize=8)
plt.title('Graph with markers',fontsize=10)
plt.ylim(1,40)#sets the limits of axis
plt.xlim(1,40)
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()

#Q-2)Write a Python program to display the current axis limits values and set new axis values.
import matplotlib.pyplot as plt
x= range(1,8)
y= [i**2 for i in x]
plt.plot(x,y,color='Red',linestyle='dashed',linewidth=5,marker='o',markerfacecolor='green',markersize=8)
plt.title('plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
print(plt.axis())#printing the value of current axis
plt.axis([0,10,0,50])#setting new axis for values
plt.show()

#Q-3)Write a Python program to plot quantities which have an x and y position.
import matplotlib.pyplot as plt
x1=[2,3,5,6,8]
y1=[1,5,19,18,20]
x2=[3,4,6,7,9]
y2=[2,6,11,20,22]
plt.plot(x1,y1,color='red',linewidth=5,linestyle='dotted',marker='o',markerfacecolor='green',markersize=8)
plt.plot(x2,y2,color='green',linewidth=8,linestyle='dashed',marker='o',markerfacecolor='blue',markersize=6)
plt.plot(x1,y1,'g--')#ese v draw kr skte h lines
plt.plot(x2,y2,'bs')
plt.title('Plot')
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.show()

#Q-4) Write a Python program to plot several lines with different format styles in one command using array.
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,5.,0.2)
plt.plot(x,x,'g--',x,x**2,'bs',x,x**3,'r^')#green-dashed, blue-square, red-traingles
plt.show()

#Q-5) Write a Python program to fill the spane between the data sets
import matplotlib.pyplot as plt
x=list(range(11))
y=[i**2 for i in x]
z=[i**3 for i in x]
plt.scatter(x,y,c='blue',edgecolor='none',s=20)
plt.scatter(x,z,c='red',edgecolor='none',s=15)
plt.fill_between(x,y,z,facecolor='blue',alpha=0.25)
plt.title('Fill Colour',fontsize=8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

#Q-6) Write a Python program to plot graph with dates
from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
dates= [dt(2016,6,21),dt(2016,6,22),dt(2016,6,23),dt(2016,6,24)]
temp = [57,68,54,50]
fig=plt.figure(figsize=(10,6))
plt.plot(dates,temp,c='blue',marker='o',markerfacecolor='red',markersize=8)
plt.title('Temp',fontsize=10)
plt.fill_between(dates,temp,facecolor='green')
plt.xlabel('Dates',fontsize=8)
plt.ylabel('Temp',fontsize=8)
x_axis=plt.axes().get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter('%B/%d/%y'))
fig.autofmt_xdate()
plt.show()
