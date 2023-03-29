x=[1,2,3,4,5]
y=[4,7,9,12,16]
n=len(x)

sumax=0
for i in range(n):
    xv=x[i]
    sumax=sumax+xv

sumay=0
for i in range(n):
    yv=y[i]
    sumay=sumay+xv

sumaxy=0
for i in range(n):
    xv=x[i]
    yv=y[i]
    producto=xv*yv
    sumaxy=sumaxy+producto
print("sumaxy={}".format(sumaxy))

sumax2=0
for i in range(n):
    xv=x[i]
    producto=xv*xv
    sumax2=sumax2+producto
print("sumaxy={}".format(sumaxy))
promx=sumax/n
promy=sumay/n
print("promx={}".format(promx))
print("promy={}".format(promy))
    
