
print('start!')

f = open('untitled', 'r')
list = []
print "hoge"
i=0
x=0
for line in f:
    #print line
    i=i+1
    list.append(float(line))
    x = x+int(line)
    if i == 24:
        print max(list)
        #print(list)
        list=[]
        i=0
        #print(x)
        x=0
f.close()

print('end')


