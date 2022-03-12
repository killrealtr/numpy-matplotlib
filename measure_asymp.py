def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def ins_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        while j>0 and a[j-1]>a[j]:
            swap(a,j-1,j)
            j-=1

def sift_down(heap, i,j):
    n=len(heap)
    while i*2+1<j:
        if i*2+2<j and heap[i*2+1]<heap[i*2+2]:
            if heap[i]<heap[i*2+2]:
                swap(heap,i,i*2+2)
                i=i*2+2
                continue
        else:
            if heap[i]<heap[i*2+1]:
                swap(heap,i,i*2+1)
                i=i*2+1
                continue
        break

def build_heap(A):
    from math import ceil
    n=len(A)
    for i in range(ceil(n/2)-1,-1,-1):
        sift_down(A,i,n)

def heapsort(A):
    n=len(A)
    build_heap(A)
    for i in range(n):
        swap(A,0,n-1-i)
        sift_down(A,0,n-1-i)

def measure(a):
    start=time.time()
    a.sort()
    end=time.time()
    return end-start

def rand_arr(n):
    n=int(n)
    return np.array([random.random() for i in range(n)])

import time
import numpy as np
import random
import matplotlib.pyplot as plt
import os

#os.chdir('C:\\Users\\ACER\\Repos\\workdir')

x=np.linspace(2,10000, 10)
#k=float(input())
#print(measure(rand_arr(10000))/(1000*np.log(1000)))
plt.plot(x,[measure(rand_arr(i)) for i in x],label='Default Python sorting asymptotics' , color='blue')
plt.plot(x, [0.0000000025*i*np.log(i) for i in x],label='Linearithmic approximation', color='red')

plt.title('Asymptotics measurement')
plt.xlabel('Length of an array')
plt.ylabel('Working time, s')

plt.legend()

plt.savefig('default_sort.png')

