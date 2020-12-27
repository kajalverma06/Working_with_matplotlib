#Q-1) Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
import matplotlib.pyplot as plt
values = [1,2,3,4,5]
plt.plot(values,values,linewidth = 5)
plt.title('PLOT',fontsize=8)
plt.xlabel('Values',fontsize = 8)
plt.ylabel('Values',fontsize = 8)
plt.tick_params(axis='both',labelsize = 14)
plt.show()

#Q-2)Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and
# a title.
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,3,1,3]
plt.plot(x,y)
plt.title("PLOT")
plt.xlabel('x-axis',fontsize = 10)
plt.ylabel('y-axis',fontsize = 10)
plt.show()

#Q-3) Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to
# October 7, 2016
import matplotlib.pyplot as plt
import pandas as pd
financial_data = pd.read_csv('sample_data.csv',sep=',',parse_dates=True,index_col=0)
financial_data.plot()
plt.show()

#Q-4)Write a Python program to plot two or more lines on same plot with suitable legends of each line.
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[4,2,3,1]
plt.plot(x,y,label = 'Line-1')
plt.plot(y,x,label= 'Line-2')
plt.title('TWO LINE PLOT')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.legend()
plt.show()

#Q-5)Write a Python program to plot two or more lines with legends, different widths and colors.
import matplotlib.pyplot as plt
x1 = [10,20,30,40]
y1 = [20,40,10,40]
plt.plot(x1,y1,label='Line-1',c=(0,0,1),linewidth=3)
x2 = [30,10,40,20]
y2 = [10,40,20,30]
plt.plot(x2,y2,label='Line-2',c=(1,0,0),linewidth=6)
plt.title('Coloured Lines')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()

#Q-6) Write a Python program to plot two or more lines with different styles.
import matplotlib.pyplot as plt
x1 = [10,20,30,40]
y1 = [20,40,10,40]
plt.plot(x1,y1,label='Line-1-dotted',c=(0,0,1),linewidth=3,linestyle='dotted')
x2 = [30,10,40,20]
y2 = [10,40,20,30]
plt.plot(x2,y2,label='Line-2-dashed',c=(0,1,0),linewidth=6,linestyle='dashed')
plt.title('Different Lines')
plt.show()
