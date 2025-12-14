paragraph = "cat dog mouse cat rat cat mouse"
p=paragraph.split()
count={}
for słowo in p:
    if słowo in count:
        count[słowo]+=1
    else:
        count[słowo]=1
print(count)