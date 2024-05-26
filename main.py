import numpy as np
import pandas as pd

# NUMPY!!!!!!!!!!! macierze i wektory

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
#
# c = a-b
# print(c)
#
# print(b**2)
#
# print(a)
# a += b
# print(a)
# a -= b
# print(a)
# d=a*b
# print(d)
#
#
# b=np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c = np.array([2.,-1.,4.])
# print(np.add(b,c))
#
# a=np.arange(3)
# b=np.arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(np.dot(a,b))
#
# c=np.array([[1, 5], [2, 6],[7,4]])
# d=np.array([[2,5,4],[4,3,1]])
# print(c)
# print(d)
# print(np.dot(c,d))
# print(np.dot(d,c))


# a=np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.min(axis=1))
# print(a.cumsum(axis=1))


# a=np.arange(6).reshape((3,2))
# print(a)
# for b in a:
#     print(b)
#
# a=np.arange(6).reshape((3,2))
# print(a)
# for b in a.flat:
#     print(b)
#
# a=np.arange(6).reshape((3,2))
# print(a)
# for b in a:
#     for i in range(len(b)):
#         print(b[i],end=' ')
#         print(" ")
#
# print(a)
# print(a.shape)
# print(type(a.shape))
#
# # ??
# for i in range(0, a.shape[0]):
#     for j in range(0, a.shape[1]):
#         print(a[i][j], end=" ")
#         print(" ")
#
#
#
# a=np.arange(6)
# print(a)
# print(a.shape)
# print("")
# b=a.reshape((2,3))
# print(b)
# print(b.shape)
# print("")
# c=b.reshape((3,2))
# print(c)
# print(c.shape)
# print("")
#
#
# d=c.ravel()
# print(d)
# print(d.shape)
# print("")
#
# e=b.T
# print(e)
# print(e.shape)


# PANDAS!!!!!!!!!!

s=pd.Series([1,3,5,np.nan,6,8])
print(s)
s=pd.Series([10,12,8,14], index=['a','b','c','d'])
print(s)
data={'Kraj':['Belgia','Indie','Brazylia'],
      'Stolica':['Bruksela','New Delhi','Brasilia'],
      'Populacja':[11190846,1303171035, 207847528]}
df=pd.DataFrame(data)
print(df)
print(df.dtypes)

print(s['c'])
print(s.c)
print(df[0:1])
print("")
print(df['Populacja'])
print(df.iloc[2,0])

# podaj numer wiersza i nazwe kolumny
print(df.loc[0,"Kraj"])
print(df.at[0,"Kraj"])


# df=pd.read_csv('dane.csv', header=0,sep=";",decimal='.')
# print(df)
# df.to.csv('plik.csv',index=False)
