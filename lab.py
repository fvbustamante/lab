#%%
parametro=[[1,2,3],[4,5,6],[7,8,9]]

def diagonal(arr):
    k=0
    i=0
    abajo=0
    arriba=0
    largo= len(arr)
    while k<largo:
        abajo=abajo+arr[k][k]
        arriba=arriba+arr[largo-i-1][largo-i-1]
        i=i+1
        k=k+1    
    return abs(abajo-arriba)



                