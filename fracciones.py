#%%
#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
parametro =[-4,3,-9,0,4,1]

def frac(arr):
    positivos=0
    negativos=0
    ceros=0
    for num in arr:
        if num >0:
            positivos=positivos+1
        elif num<0:
            negativos=negativos+1
        elif num==0:
            ceros=ceros+1
    a=positivos/len(arr)
    b=negativos/len(arr)
    c=ceros/len(arr)
    
    print(a,b,c,sep='\n')

frac(parametro)