import utilities as li
import math as m

def func(x):
    s=m.exp(-(x**2))
    return(s)
eq=func
el=func



N_t=li.N_value(0,1,2,"T")
print("N for trapezoidal",N_t)
t=li.Trapzoidal_meth(el,0,1,N_t)
print("value from trapezoidal method",t)

N_f=li.N_value(0,1,2,"M")
print("N for rectangle method",N_f)
f=li.Rectangle_meth(eq,0,1,N_f)
print("value from rectangle mehod",f)

N_k=li.N_value(0,1,12,"S")
print("N for simpson method",N_k)
k=li.Simpson_rule(eq,0,1,N_k)
print("value from simpson method",k)


#output:
# N for trapezoidal 13
# value from trapezoidal method 0.7464612610366895
# N for rectangle method 10
# value from rectangle mehod 0.7471308777479975
# N for simpson method 3
# N made even 4
# value from simpson method 0.7468553797909872
