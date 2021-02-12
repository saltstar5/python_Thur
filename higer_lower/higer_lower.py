from game_data import data
from display import logo,vs
import random
import os 

def p_logo():
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)

def display_question(part, index):
    ret=0
    print(f"Compare {part} :",end="")
    for key, values in data[index].items():
        if key== 'follower_count':
            ret = values
        else:
            if key == 'country':
                print(f" from {values}")
            else:print(f" {values} ",end="")
    return ret

idx=random.sample(range(0,len(data)),len(data))
winindex=idx[0]
win, index=1,1
A1, A2,score= 0,0,0
while win :
    p_logo()
    
    A1 = display_question('A', winindex)
    print(vs)
    A2 = display_question('B',idx[index])
    index+=1;

    ans = input("Who has more floolwers? type 'A' or 'B':")
    ## check the answer and update winindex
    if A1>A2 and ans=='A' :
        score+=1
    elif A1<A2 and ans=='B' :
        winindex = index-1
        score+=1
    elif A1==A2:
        sleep(1)
        ## -> just repeat again(with another Q2 question)
    else:win=0

p_logo()
if not win :print(f"Sorry, that's worng. final score: {score}")
else: print(f"Congratulation !!  You've got a perfect score: {score}")

