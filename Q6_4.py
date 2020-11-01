import utilities as li
import math as m

def function(x):
    s=4/(1+x**2)
    return(s)
eq=function
X=[];dev=[];Y=[]

for r in range(10,30001,10):

    fun,var=li.Monte_Carlo(eq,0,1,r)
    X.append(fun)
    Y.append(r)
    dev.append(var**(1/2))
li.plotting(Y,X,"N","pi","pi vs N")

#Ouput:
#Graph pi vs N
