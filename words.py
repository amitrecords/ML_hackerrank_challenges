import sys
tot_word_cnt=0
word_list=[]

letter_cnt=[0]*26
line=sys.stdin.readline()
words=line.split(" ")
for w in words:
    w=w.strip()
    if(w.isalpha() and w.islower()):
        tot_word_cnt+=1
        word_list.append(w)
          
word_list.sort()
word_cnt=[0]*len(word_list)
ctr2=0
flag=0
word_list_unique=[]
for w in range(0,len(word_list)):
    for w2 in word_list:
        if word_list[w]==w2:
            word_cnt[w]+=1
            if word_cnt[w]>1:
                flag=1
    if flag==0:
        word_list_unique.append(word_list[w])

                

print(tot_word_cnt)
print("words")
ctr3=0
for w in word_list_unique:
    print(w," ",word_cnt[ctr3])
    ctr3+=1
ctr=0
for code in range(ord('a'), ord('z') + 1):
    c=chr(code)
    print(c.strip()," ", letter_cnt[ctr])
    ctr+=1