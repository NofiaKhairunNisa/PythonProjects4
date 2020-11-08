#Latihan

#nomor satu
print ("menentukan triple pythagoras")
a = int(input("Masukkan nilai a = "))
b = int(input("Masukkan nilai b = "))
c = int(input("Masukkan nilai c = "))


def isPythagoras (a, b, c):
    if (a % 3 == 0 and b % 4 == 0 and c % 5 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 5 == 0 and b % 12 == 0 and c % 13 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 7 == 0 and b % 24 == 0 and c % 25 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 8 == 0 and b % 6 == 0 and c % 10 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 9 == 0 and b % 40 == 0 and c % 41 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    else :
        print ('False, nilai tersebut adalah bukan triple pythagoras')
isPythagoras (a,b,c)

print ()

#nomor dua
print('formasi  1')
def starFormation1 (n):
    i = 0
    while (i < n):
        i += 1
        print ('* ' * i)
starFormation1 (4)
print('')
print("\n")
print('formasi 2')

def starFormation2 (n):
    print ('* ' * n) 
    while (n > 0):
        n -= 1
        print ('* ' * n)
starFormation2(4)

print("\n")
print("formasi gabungan")

def starFormation3 (n):
    i = 0
    while ( i < n/2 ):
        i += 1
        print ('* ' * i)
    while ( i >= n/2 or i > 0):
        i -= 1
        print ('* ' * i)
        
starFormation3 (7)

print()

#nomor tiga
def faktorial(n):
    if (n==1):
        return 1
    elif (n==0):
        return 1
    else :
        return (n * faktorial(n-1))
def kombinasi (a, b):
    hasil = faktorial(a)/(faktorial(a-b) * faktorial(b))
    print ('Kombinasi dari ', a,'C', b, 'yaitu ',hasil)

def permutasi (a, b):
    hasil = faktorial(a)/ faktorial(a-b)
    print ('Kombinasi dari ', a,'P', b,'yaitu ',hasil)
kombinasi(5,3)
permutasi(10,7)

print()

#nomor lima
from statistik import*
data=5,10,4,9,30,16,2,11

print('a. 5,10,4,9,30,16,2,11')
print('Rata-rata:',avarage(data))
print('Nilai Maksimum:',max(data))
print('Nilai Minimum:',min(data))

from statistik import*
data=81,98,12,83,45,77,69,30,56
print('b. 81,98,12,83,45,77,69,30,56')
print('Rata-rata:',avarage(data))
print('Nilai Maksimum:',max(data))
print('Nilai Minimum:',min(data))

    
