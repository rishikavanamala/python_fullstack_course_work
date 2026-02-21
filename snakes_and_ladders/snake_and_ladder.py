# The key is the 'Start' square, the value is the 'End' square
import random
import sys
jumps = {
    # Ladders (Start < End)
    1: 38, 
    4: 14, 
    9: 31, 
    21: 42, 
    28: 84, 
    36: 44, 
    51: 67, 
    71: 91, 
    80: 100,

    # Snakes (Start > End)
    16: 6, 
    47: 26, 
    49: 11, 
    56: 53, 
    62: 19, 
    64: 60, 
    87: 24, 
    93: 73, 
    95: 75, 
    98: 78
}

def roll_dice():
    return random.randint(1,6)
name1 = input("enter player 1 name")
name2 = input("player 2 name")
score1=0
score2 =0
while(score1<=100 and score2<=100):
    print(f"{name1} press c to continue press q to quit")
    ch = input("enter the choice")
    if ch=='q':
        print(f"{name2} won")
        break
    else:
        dice = roll_dice()
        print(f"{name1} rolled the dice and got {dice}")
        score1 = score1+dice
        if score1 in jumps:
            score1 =jumps[score1]
        if score1==100:
            print(f"{name1} won")
            break
        elif score1>100:
            print(f"sorry {name1} it is out of bound cant move u")
            score1 = score1-dice
        print(f"{name1} present score is {score1}")
    print(f"{name2} press c to continue press q to quit")
    ch = input("enter the choice")
    if ch=='q':
        print(f"{name1} won")
        break
    else:
        dice = roll_dice()
        print(f"{name2} rolled the dice and got {dice}")
        score2 = score2+dice
        if score2 in jumps:
            score2 = jumps[score2]
        if score2==100:
            print(f"{name2} won")
            break
        elif score2>100:
            print(f"sorry {name2} it is out of bound cant move u")
            score2 = score2-dice
        print(f"{name1} present score is {score1}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
