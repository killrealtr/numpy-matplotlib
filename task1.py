def average(line):
    val=list(map(float, line.split()))
    s=0
    k=0
    for i in val:
        s+=i
        k+=1
    return str(s/k)



import os

os.chdir('/home-local/student/Downloads/')
av_val=[]
with open('task1.txt', 'r') as text:
    for line in text:
        av_val.append(average(line)+'\n')

with open('out.txt', 'w') as out:
    out.writelines(av_val)

