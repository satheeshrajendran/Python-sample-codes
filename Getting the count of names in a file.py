

fo=open("C:/Users/s.c.kumar.rajendran/Desktop/Namelist1.txt", "r+")
wordcount={}
for word in fo.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word]+=1
for k,v in wordcount.items():
    print k,v
#print wordcount







