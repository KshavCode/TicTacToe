import random

# def display(arr:list)->None :
#     x = 0
#     for i in range(3, 10, 3) :
#         print(arr[x:i])
#         x = i
#     print()

def game(x="X") :
    c = 0
    play1 = x
    play2 = 0
    guesslis = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random_list = list(range(9))

    play1 = x
    if play1 == "X" : 
        play2 = "O"
    else : 
        play2 = "X"

    while True : 
        # display(guesslis)
        player1 = random.choice(random_list)
        random_list.remove(player1)
        guesslis[player1] = play1
        c += 1
        if guesslis[0]==guesslis[1]==guesslis[2] or guesslis[3]==guesslis[4]==guesslis[5]   or guesslis[6]==guesslis[7]==guesslis[8] or guesslis[0]==guesslis[3]==guesslis[6]     or guesslis[1]==guesslis[4]==guesslis[7] or guesslis[2]==guesslis[5]==guesslis[8]   or guesslis[0]==guesslis[4]==guesslis[8] or guesslis[2]==guesslis[4]==guesslis[6] : 
            return 1
        if c > 8 :
            return 0
        
        player2 = random.choice(random_list)
        random_list.remove(player2)
        guesslis[player2] = play2
        c += 1
        if guesslis[0]==guesslis[1]==guesslis[2] or guesslis[3]==guesslis[4]==guesslis[5] or guesslis[6]==guesslis[7]==guesslis[8] or guesslis[0]==guesslis[3]==guesslis[6] or guesslis[1]==guesslis[4] ==guesslis[7] or guesslis[2]==guesslis[5]==guesslis[8] or guesslis[0]==guesslis[4]==guesslis[8]  or guesslis[2]==guesslis[4]==guesslis[6] : 
            return 2
        if c > 8 :
            return 0
        

result_list = [0, 0, 0]
for i in range(20) :
    result = game()
    result_list[result] += 1

print("Ties :", result_list[0])
print("Player 1 Wins :", result_list[1])
print("Player 2 Wins :", result_list[2])
