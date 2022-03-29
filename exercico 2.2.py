import math
angulo=float(input("angulo"))
n=math.cos(math.radians(angulo))
s=math.sin(math.radians(angulo))
l=math.tan(math.radians(angulo))

print("cos({}), é qui vale a {:.2f}".format(angulo,n))
print("sin({}), é qui vale a {:.2f}".format(angulo,s))
print("tan({}), é qui vale a {:.2f}".format(angulo,l))
