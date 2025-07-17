import random
x=100000000
count_k=0
count_s=0
y=1
for each in range(x):
        y= each/1000000
        print(int(y),"%")
        data =random.randint(0, 1)
        if(data==0):
            count_k+=1
        else:
            count_s+=1        
count_k=(count_k/x)*100
count_s=(count_s/x)*100
print("count_k",count_k)
print("count_s",count_s)
print("end")
