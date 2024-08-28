import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

print("Dizinin Boyutu (ndim):", array.ndim)
print("Dizinin Boyutu (shape):", array.shape)
print("Dizinin Boyutu (dtype):", array.dtype)

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 10, 11, 14]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 10, 11])

a * b

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)

np.random.randint(10, size=10)
np.random.randint(20, size=15)
np.random.randint(0, 20, size=15)
np.random.normal(10, 4, (3, 4))
                 ## mean,  standard sapması , 3 satır  4 sütundan oluşan np array.


#numpy array özellikleri

#ndim. boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(10, size=10)
a.ndim
a.shape
a.size # toplam eleman sayısı
a.dtype

#### reshaping methodu....

np.random.randint(0, 20, size = 9)
np.random.randint(0, 20, size = 9).reshape(3, 3)

ar = np.random.randint(0, 20, size = 9)

ar.reshape(3, 3)

#### index seçimiii  index işlemleri önemli bir yeri vardır...

a = np.random.randint(5, 10, size=10)
a[0]
a[0:5] #### slicing denir....

m = np.random.randint(100, size=(3, 5))


m[0, 0]
m[1, 1]
m[2, 3] = 1200
m[2, 3] = 222.9 ### tek tip tutar ve verimli bilgi sağlar...

m[:, 0]
m[1, :]

m[0:2, 0:2]


### Fancy indexleri

v = np.arange(0, 30, 3) ### 0 dan 30 a kadar sayı üret sayıları 3 er 3 er arttır.

v[1]
v[4]

catch = [1, 2, 3, 4, 5]
v[catch]

#### numpy koşullu işlemler...

import numpy as np

v = np.array ([1, 2, 3, 4, 5])
ab = []
for i in v:
    if i < 3:
    ab.append(i)

#### numpy ile nasıl gerçekleştiririz...

v < 3

v[v < 3]  ### u şekilde döngü yazmadan çağırabiliriz...

v[v != 3]

### arka planda çalışan fancy kavramı....

#### matematiksel işlemlerrr numpy erray...

v = np.array([1, 2, 3, 4, 5])

v / 5

v * 5 / 10

v ** 2


np.mean(v)
np.min(v)
np.max(v)
np.var(v)

np.fives(10)

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])








