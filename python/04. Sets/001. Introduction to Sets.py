def average(array):
    sum=0
    a=set(array)
    for i in a:
        sum=sum+i
    avg=sum/len(a)
    return avg

