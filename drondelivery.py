import sys

num_packages=4
delivered_packagecnt=0
seq= sys.stdin.readline()
seqlis=seq.split(',')
sequence=[]
grid=[]
house=[];g1houses2visit=[];g2houses2visit=[]
for s in seqlis:
    locid=s.split('-')
    grid.append(int(locid[0].strip()))
    house.append(int(locid[1].strip()))
#print(grid)
#print(house)
t=0;
ctr=0
drone1=[]
drone2=[]
d1_house=1;d2_house=1
first_grid=grid[0]
for g in range(0,len(grid)):
    if grid[g]!=grid[g+1]:
        second_grid=grid[g+1]
        break
for g in range(0,len(grid)):
    if grid[g]==first_grid:
        g1houses2visit.append(house[g])
    elif grid[g]==second_grid:
        g2houses2visit.append(house[g])
#print(first_grid,second_grid)
t=0;g2ctr=0;g1ctr=0;chkctr=0
#print(g1houses2visit,g2houses2visit)
while delivered_packagecnt != num_packages:
    #print(drone1,drone2); chkctr+=1
    if grid[ctr]==first_grid:
            if(house[ctr]==d1_house):
                drone1.append("deliver")
                delivered_packagecnt+=1
                g1ctr+=1
                if g2ctr >= len(g2houses2visit):
                    g2houses2visit.append(g2houses2visit[g2ctr-1])
                ctr=ctr+1
                if(g2houses2visit[g2ctr]>d2_house):
                    drone2.append("move")
                    d2_house+=1
                elif(g2houses2visit[g2ctr]<d2_house):
                    drone2.append("move")
                    d2_house-=1
                else:
                    drone2.append("stay")
                
            elif(house[ctr]>d1_house):
                drone1.append("move")
                d1_house+=1
                if(g2houses2visit[g2ctr]>d2_house):
                    drone2.append("move")
                    d2_house+=1
                elif(g2houses2visit[g2ctr]<d2_house):
                    drone2.append("move")
                    d2_house-=1
                else:
                    drone2.append("stay")
            elif(house[ctr]<d1_house):
                drone1.append("move")
                d1_house-=1
                if(g2houses2visit[g2ctr]>d2_house):
                    drone2.append("move")
                    d2_house+=1
                elif(g2houses2visit[g2ctr]<d2_house):
                    drone2.append("move")
                    d2_house-=1
                else:
                    drone2.append("stay")
    elif grid[ctr]==second_grid:
            if(house[ctr]==d2_house):
                drone2.append("deliver")
                delivered_packagecnt+=1
                ctr=ctr+1
                g2ctr+=1
                if g1ctr >= len(g1houses2visit):
                    g1houses2visit.append(g1houses2visit[g1ctr-1])
                if(g1houses2visit[g1ctr]>d1_house):
                    drone1.append("move")
                    d1_house+=1
                elif(g1houses2visit[g1ctr]<d1_house):
                    drone1.append("move")
                    d1_house-=1
                else:
                    drone1.append("stay")
                
            elif(house[ctr]>d2_house):
                drone2.append("move")
                d2_house+=1
                if(g1houses2visit[g1ctr]>d1_house):
                    drone1.append("move")
                    d1_house+=1
                elif(g1houses2visit[g1ctr]<d1_house):
                    drone1.append("move")
                    d1_house-=1
                else:
                    drone1.append("stay")
            elif(house[ctr]<d2_house):
                drone2.append("move")
                d2_house-=1
                if(g1houses2visit[g1ctr]>d1_house):
                    drone1.append("move")
                    d1_house+=1
                elif(g1houses2visit[g1ctr]<d1_house):
                    drone1.append("move")
                    d1_house-=1
                else:
                    drone1.append("stay")
    
    t=t+1

print("It takes",t,"minutes to deliver all packages") 
print(drone1,drone2)   