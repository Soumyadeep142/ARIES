from numpy import *
from matplotlib.pyplot import *

ID=loadtxt("Period.txt", usecols=(0), unpack='True')
ref_id, x_axis, y_axis=loadtxt('refstars_new.list', usecols=(0,1,2), unpack='true')

Variable_ID=[]
Variable_x=[]
Variable_y=[]

Non_Variable_ID=[]
Non_Variable_x=[]
Non_Variable_y=[]
for (i,x,y) in zip(ref_id, x_axis, y_axis):
	if i in ID:
		Variable_ID.append(i)
		Variable_x.append(x)
		Variable_y.append(y)
	else:
		Non_Variable_ID.append(i)
		Non_Variable_x.append(x)
		Non_Variable_y.append(y)
scatter(Non_Variable_x, Non_Variable_y, marker='+', s=1, color='cyan')		
scatter(Variable_x, Variable_y, marker='+', s=120, color='red', label='Variable Stars')
legend(loc='best')
xlabel("X-axis")
ylabel("Y-axis")
savefig("Variable.png")
