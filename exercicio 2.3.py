import math

n=float(input("cateto adjacente "))
n1=float(input("cateto oposto"))
s=n**2
s1=n1**2
s2=(math.sqrt(s+s1))
s3=math.hypot(n,n1)

print("cateto oposto {}m,mais cateto jacente {}m é igual a hipotenusa {}m".format(s,s1,s2))
print("hipotenusa {:.2f}".format(s3))
#dos os trez metodo estão correto#

print("{:.2f}m+{:.2f}m={:.2f}m".format(s,s1,s2))