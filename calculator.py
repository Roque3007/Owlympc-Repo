import random


i=0;
moves=0;
while True:
    die=int(input("How many die are there? "));
    sides=int(input("How many sides on each die? "));
    while i<die:
        diceval=random.randint(1,sides);
        i+=1
        moves+=diceval;
    print("You have ", moves, " moves");
    reroll= input("Roll Again(y/n)? ");
    if reroll=="n":
        break
    
    
    
