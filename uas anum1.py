# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:47:06 2019

@author: Andidar83
"""

import numpy as np
import matplotlib.pyplot as plt
"""
#NO. 1
# A
#menggunakan rumus forward,backward,dan central finite difference

g= [0.1,0.1,0.7,0.5,-0.3,-0.5,0.1,0.8,1.5] #data anomaly gravitasi
y= [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0] #jarak y (km)

turunan=[] #list kosong untuk nantinya dimasukkan data hasil turunan
turunan1= (g[0+1]-g[0])/1 #forward dinite difference untuk data ke 1
turunan9= (g[8]-g[8-1])/1 #backward dinite difference untuk data ke terakhir

turunan.insert(0,turunan1) #memasukkan data ke list turunan
turunan.insert(len(turunan),turunan9) #memasukan data ke list turunan
for i in range(7): #untuk setiap suku di rentang 0 sampai 7
    d=1 #d dimulai dari 1
    for gi in range(7): #untuk setiap suku di rentang 0 sampai 7
        derivetive= (g[d+1]-g[d-1])/2 #central finite difference untuk suku data ke 2-8
        d=d+1
        turunan.append(derivetive)#memasukkan data ke list turunan
    break







plt.figure(figsize=(6,4))
plt.plot(y,turunan,'ob--')
plt.xlabel('jarak pada sumbu Y (km)')
plt.ylabel('FHD')
plt.title('Grafik First Horizontal Derivetive Sepanjang Y pada X=6 km')


# B

g = [[0,-0.2,-0.7,-0.8,-0.1,0.1,-0.3,-0.5,-0.7],[2.8,0.9,-0.3,-0.3,0,0.1,0.2,0.1,0],[3,1.1,-0.6,-0.4,-0.5,0.7,1.2,1.6,1.5],[3.8,0.6,-1.5,-2.5,-1.5,0.5,2.2,2,1.5],[2,-0.2,-2.7,-3.4,-2.9,-0.3,1.5,1.8,1],
     [0.5,-1.8,-3,-3.5,-2.6,-0.5,1,1.4,1.1],[0,-2.3,-2.7,-2.4,-1.5,0.1,0.6,0.9,1.2],[2,0.5,0,0.1,0.4,0.8,1.5,2,1.1],[4,2.3,2,1.5,1.6,1.5,1.5,1.6,1]]
x =[1,2,3,4,5,6,7,8,9]
y =[1,2,3,4,5,6,7,8,9]

#FHD pada arah x disepanjang y
turunanx=[] #list kosong untuk nantinya dimasukkan data hasil turunan

gx1 = [0,-0.2,-0.7,-0.8,-0.1,0.1,-0.3,-0.5,-0.7]
turunan1x1= (gx1[0+1]-gx1[0])/1 #forward dinite difference untuk data ke 1
turunan9x1= (gx1[8]-gx1[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x1)
gx2 = [2.8,0.9,-0.3,-0.3,0,0.1,0.2,0.1,0]
turunan1x2= (gx2[0+1]-gx2[0])/1 #forward dinite difference untuk data ke 1
turunan9x2= (gx2[8]-gx2[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x2)
gx3 = [3,1.1,-0.6,-0.4,-0.5,0.7,1.2,1.6,1.5]
turunan1x3= (gx3[0+1]-gx3[0])/1 #forward dinite difference untuk data ke 1
turunan9x3= (gx3[8]-gx3[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x3)
gx4 = [3.8,0.6,-1.5,-2.5,-1.5,0.5,2.2,2,1.5]
turunan1x4= (gx4[0+1]-gx4[0])/1 #forward dinite difference untuk data ke 1
turunan9x4= (gx4[8]-gx4[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x4)
gx5 = [2,-0.2,-2.7,-3.4,-2.9,-0.3,1.5,1.8,1]
turunan1x5= (gx5[0+1]-gx5[0])/1 #forward dinite difference untuk data ke 1
turunan9x5= (gx5[8]-gx5[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x5)
gx6 = [0.5,-1.8,-3,-3.5,-2.6,-0.5,1,1.4,1.1]
turunan1x6= (gx6[0+1]-gx6[0])/1 #forward dinite difference untuk data ke 1
turunan9x6= (gx6[8]-gx6[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x6)
gx7 = [0,-2.3,-2.7,-2.4,-1.5,0.1,0.6,0.9,1.2]
turunan1x7= (gx7[0+1]-gx7[0])/1 #forward dinite difference untuk data ke 1
turunan9x7= (gx7[8]-gx7[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x7)
gx8 = [2,0.5,0,0.1,0.4,0.8,1.5,2,1.1]
turunan1x8= (gx8[0+1]-gx8[0])/1 #forward dinite difference untuk data ke 1
turunan9x8= (gx8[8]-gx8[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x8)
gx9 = [4,2.3,2,1.5,1.6,1.5,1.5,1.6,1]
turunan1x9= (gx9[0+1]-gx9[0])/1 #forward dinite difference untuk data ke 1
turunan9x9= (gx9[8]-gx9[8-1])/1 #backward dinite difference untuk data ke terakhir
turunanx.append(turunan1x9)


for i in range(7): #untuk setiap suku di rentang 0 sampai 7
    d=1 #d dimulai dari 1
    for gi in range(7): #untuk setiap suku di rentang 0 sampai 7
        derivetivex1= (gx1[d+1]-gx1[d-1])/2 #central finite difference untuk suku data ke 2-8
        derivetivex2= (gx2[d+1]-gx2[d-1])/2
        derivetivex3= (gx3[d+1]-gx3[d-1])/2
        derivetivex4= (gx4[d+1]-gx4[d-1])/2
        derivetivex5= (gx5[d+1]-gx5[d-1])/2
        derivetivex6= (gx6[d+1]-gx6[d-1])/2
        derivetivex7= (gx7[d+1]-gx7[d-1])/2
        derivetivex8= (gx8[d+1]-gx8[d-1])/2
        derivetivex9= (gx9[d+1]-gx9[d-1])/2
        d=d+1
        turunanx.append(derivetivex1)#memasukkan data ke list turunan
        turunanx.append(derivetivex2)
        turunanx.append(derivetivex3)
        turunanx.append(derivetivex4)
        turunanx.append(derivetivex5)
        turunanx.append(derivetivex6)
        turunanx.append(derivetivex7)
        turunanx.append(derivetivex8)
        turunanx.append(derivetivex9)
    break

turunanx.append(turunan9x1)
turunanx.append(turunan9x2)
turunanx.append(turunan9x3)
turunanx.append(turunan9x4)
turunanx.append(turunan9x5)                     #Masukkan nilai turunan suku ke 9 
turunanx.append(turunan9x6)                     #hasil backward finite difference ke list turunanx
turunanx.append(turunan9x7)
turunanx.append(turunan9x8)
turunanx.append(turunan9x9)



#FHD pada arah y disepanjang x
turunany = []

gy1 = [0,2.8,3,3.8,2,0.5,0,2,4]
turunan1y1= (gy1[0+1]-gy1[0])/1 #forward dinite difference untuk data ke 1
turunan9y1= (gy1[8]-gy1[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y1)
gy2 = [-0.2,0.9,1.1,0.6,-0.2,-1.8,-2.3,0.5,2.3]
turunan1y2= (gy2[0+1]-gy2[0])/1 #forward dinite difference untuk data ke 1
turunan9y2= (gy2[8]-gy2[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y2)
gy3 = [-0.7,-0.3,-0.6,-1.5,-2.7,-3,-2.7,0,2]
turunan1y3= (gy3[0+1]-gy3[0])/1 #forward dinite difference untuk data ke 1
turunan9y3= (gy3[8]-gy3[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y3)
gy4 = [-0.8,-0.3,-0.4,-2.5,-3.4,-3.5,-2.4,0.1,1.5]
turunan1y4= (gy4[0+1]-gy4[0])/1 #forward dinite difference untuk data ke 1
turunan9y4= (gy4[8]-gy4[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y4)
gy5 = [-0.1,0,-0.5,-1.5,-2.9,-2.6,-1.5,0.4,1.6]
turunan1y5= (gy5[0+1]-gy5[0])/1 #forward dinite difference untuk data ke 1
turunan9y5= (gy5[8]-gy5[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y5)
gy6 = [0.1,0.1,0.7,0.5,-0.3,-0.5,0.1,0.8,1.5]
turunan1y6= (gy6[0+1]-gy6[0])/1 #forward dinite difference untuk data ke 1
turunan9y6= (gy6[8]-gy6[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y6)
gy7 = [-0.3,0.2,1.2,2.2,1.5,1,0.6,1.5,1.5]
turunan1y7= (gy7[0+1]-gy7[0])/1 #forward dinite difference untuk data ke 1
turunan9y7= (gy7[8]-gy7[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y7)
gy8 = [-0.5,0.1,1.6,2,1.8,1.4,0.9,2,1.6]
turunan1y8= (gy8[0+1]-gy8[0])/1 #forward dinite difference untuk data ke 1
turunan9y8= (gy8[8]-gy8[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y8)
gy9 = [-0.7,0,1.5,1.5,1,1.1,1.2,1.1,1]
turunan1y9= (gy9[0+1]-gy9[0])/1 #forward dinite difference untuk data ke 1
turunan9y9= (gy9[8]-gy9[8-1])/1 #backward dinite difference untuk data ke terakhir
turunany.append(turunan1y9)


for i in range(7): #untuk setiap suku di rentang 0 sampai 7
    d=1 #d dimulai dari 1
    for gi in range(7): #untuk setiap suku di rentang 0 sampai 7
        derivetivey1= (gy1[d+1]-gy1[d-1])/2 #central finite difference untuk suku data ke 2-8
        derivetivey2= (gy2[d+1]-gy2[d-1])/2
        derivetivey3= (gy3[d+1]-gy3[d-1])/2
        derivetivey4= (gy4[d+1]-gy4[d-1])/2
        derivetivey5= (gy5[d+1]-gy5[d-1])/2
        derivetivey6= (gy6[d+1]-gy6[d-1])/2
        derivetivey7= (gy7[d+1]-gy7[d-1])/2
        derivetivey8= (gy8[d+1]-gy8[d-1])/2
        derivetivey9= (gy9[d+1]-gy9[d-1])/2
        d=d+1
        turunany.append(derivetivey1)#memasukkan data ke list turunany
        turunany.append(derivetivey2)
        turunany.append(derivetivey3)
        turunany.append(derivetivey4)
        turunany.append(derivetivey5)
        turunany.append(derivetivey6)
        turunany.append(derivetivey7)
        turunany.append(derivetivey8)
        turunany.append(derivetivey9)
    break

turunany.append(turunan9y1)
turunany.append(turunan9y2)
turunany.append(turunan9y3)
turunany.append(turunan9y4)
turunany.append(turunan9y5)                     #Masukkan nilai turunan suku ke 9 
turunany.append(turunan9y6)                     #hasil backward finite difference ke list turunanx
turunany.append(turunan9y7)
turunany.append(turunan9y8)
turunany.append(turunan9y9)



#menghitung FHD total
def power (turunanx):
    return [a**2 for a in turunanx]   #pangkat 2 dari FHDx


def power (turunany):
    return [b**2 for b in turunany]    #pangkat 2 dari FHDy


FHDtot=np.array(power(turunanx))+np.array(power(turunanx)) #Jumlah antara FHDx^2+FHDy^2

import math
print ('nilai FHDTot adalah')
print (math.sqrt, FHDtot)     #Nilai FHDTot    

"""

    

'''
#NO . 2
# nilai awal 
t0 = 0
v0 = 10
h = 0.01

#nilai dari x yang kita cari
t = 1
euler(t0, v0, h, t)

# Mendefinisikan fungsi persamaan diferensial 
def func( t, v ): 
	return (-9.81 - 0.2*v**2) 
	
# fungsi dari rumus euler
def euler( t0, v, h, t ): 
	temp = -0

	# melakukan iterasi 
	 
	while t0 < t: 
        
		temp = v 
		v = v + h * func(t0, v) 
		t0 = t0 + h 

        print("solusi pada x = ", t, " adalah ","%.6f"% v) 
'''





#NO. 3

import numpy as np
xinit = 0.0 # initial mesh point
xfin = 2000.0 # final mesh point
yinit = 50.0 # initial value
yfin = 250.0 # final value
h = 100.0 # step size
numstep = int((xfin-xinit)/h)-1 # number of steps

z =[] #setiap point kedalaman dengan interval 100m dari 0m
for i in range(20): #untuk setiap suku di rentang 0 sampai 20
    d=0 #d dimulai dari 0
    for gi in range(20): #untuk setiap suku di rentang 0 sampai 20
        zi= d+h #central finite difference untuk suku data ke 0-20
        d=zi
        z.append(zi) #masukkan hasil ke list z
    break
z.insert(0,0.0) #nilai kedalaman awal yaitu 0 m





## DIFFERENTIAL EQUATION ##
def equation(y,dy,d2y):
    return c2*d2y + c1*dy + c0*y # specify our function

## DERIVATIVE COEFFICIENT ##
c2 = z # koefisien d2y
c1= 1  # koefisien dy
c0 = 0 # coefficient of y

upper1=[]   #nilai koefisien upper center dan lower pada setiap kedalaman(z) untuk disusun menjadi matrix A
lower1=[]
center1=[]
for i in range(21): 
    d=0 
    for gi in range(21): #rumus untuk koefisien upper lower dan center matrix dengan nilai z berubah ubah bergantung kedalaman
        upper=  (z[d]/(h**2))+(c1/(2*h))
        lower= (z[d]/(h**2))-(c1/(2*h))
        center = (-2*z[d])/(h**2)
        d=d+1
        
        upper1.append(upper)
        lower1.append(lower)
        center1.append(center)
    break


## COEFFICIENT MATRIX ##

A=np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.005,-0.02,0.015,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.015,-0.04,0.025,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0.024,-0.06,0.034,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0.035,-0.08,0.045,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0.045,-0.1,0.055,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.055,-0.12,0.065,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0.065,-0.14,0.075,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.075,-0.16,0.085,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0.084,-0.18,0.095,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.095,-0.2,0.105,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0.105,-0.22,0.115,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0.114,-0.24,0.125,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0.125,-0.26,0.135,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0.135,-0.28,0.145,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.145,-0.3,0.155,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.155,-0.32,0.165,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.165,-0.34,0.175,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.175,-0.36,0.185,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.185,-0.38,0.195],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])

    
b=np.zeros(21)#membuat matriks b dengan nilai awal dan akhir diketahui
for row in range (21):
    if row==0:
        b[row]= 50
    elif row == 21-1:
        b[row]= 250
    else:
        b[row]= 0


## LINEAR ALGEBRA SOLUTION ##
# Using Gauss-Seidel
        
x = np.zeros(21) # initial solution

# Stopping Criteria
itermax = 1000 #jumlah iterasi maksimum
errmin = 0.0001 #jumlah error minimum

n = len(b)
D = np.zeros((n,n))
E = np.zeros((n,n))

for i in range(n): # loop per baris
  for j in range(n): # loop per kolom
    if i == j:
      D[i,j] = 1/A[i,j] # Masukkan elemen diagonal ke D-1
    else:
      E[i,j] = A[i,j] # Masukkan elemen off-digonal ke E

      
for i in range(itermax):
  xo = tuple(x) # Old vektor yang tidak diupdate
  xu = x # Vektor yang akan diupdate
  for k in range(len(x)):
    xu[k] = np.dot(D,(b-np.dot(E,xu)))[k]
  error = 0
  for j in range(len(x)):
    error = error + np.sqrt((xu[j]-xo[j])**2) # Norm antara updated value dengan old value
  
  # Tes konvergensi, jika nilai norm lebih kecil dari error minimum -> break.
  if error < errmin:
    x = xu # nilai x adalah nilai x yang terakhir diupdate
    break
  
  # Jika error masih besar, lanjut iterasi dengan nilai x terupdate
  x = xu

# Jika iterasi sudah mencapai maksimum tapi belum mencapai nilai error yang diinginkan, maka
if i == itermax:
  print ('Reached Maximum Iteration ', i)
else:
  print ('Convergence has been reached at iteration ', i)
  
print ('Solution:')
print (x)
