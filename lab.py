#%%
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

parametro=[[11,2,4],[4,5,6],[10,8,-12]]

def diagonal(arr):
    k=0
    i=0
    abajo=0
    arriba=0
    largo= len(arr)
    while k<largo:
        abajo=abajo+arr[k][k]
        arriba=arriba+arr[k][largo-i-1]
        i=i+1
        k=k+1    
    return abs(abajo-arriba)

