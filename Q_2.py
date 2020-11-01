import utilities as li
import math as m

def func(x):
    s=x/(1+x)
    return(s)
eq=func
el=func
A=["N","Trapezoidal method","Midpoint method","Simpson","Analytical"]
li.write_table(A,'w')

r=(5,10,25)
for i in r:
    B=[]
    B.append(i)
    t=li.Trapzoidal_meth(el,1,3,i)
    B.append(t)

    f=li.Rectangle_meth(eq,1,3,i)
    B.append(f)

    s=li.Simpson_rule(eq,1,3,i)
    B.append(s)
    B.append(1.30685281944)
    i=i+1
    li.write_table(B,'a')

#Ouput
#N made even 6
#N made even 26
#file:
# N                             Trapezoidal method            Midpoint method               Simpson                       Analytical
# 5                             1.3043650793650796            1.308092114284065             1.3068302068302067            1.30685281944
# 10                            1.3062285968245722            1.3071646395900398            1.3068497693110694            1.30685281944
# 25                            1.306752839424082             1.3069028019555275            1.3068527513069685            1.30685281944
