"""
File: hangman.py
Name: Karen Wong
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7



def main():
    """
    This program used to guess random words. Users have seven chances at the beginning stage,
    each wrong guess will costs a chance. Users who figure out all will character of the word
    within given lives will win the game.
    """
   print('========')
    for i in range(6):
        print('|')
    print('')

    ans = random_word()
    n_turns = N_TURNS
    # count total character of the word
    ans_now = ''
    for i in range(len(ans)):
        ans_now += '-'
    print('The word looks like: ' + ans_now)
    print('You have ' + str(n_turns) + ' guesses left.')

    while ans_now != ans:
        if n_turns == 0:
            print('========')
            print('|    |')
            print('|  (0.0)')
            print('|  ¬ # ¬')
            print('|    #  ')
            print('|   / \\ ')
            print('|     ')
            print('')
            print('You are completely hang :(')
            break
        else:
            input_ch = input('Your guess: ').upper()
            # check input format
            while input_ch.isalpha() == False or len(input_ch) != 1:
                print('"Illegal format."')
                input_ch = input('Your guess: ').upper()
            # main function
            if input_ch in ans:
                temp = ''
                print('You are correct!')
                for i in range(len(ans)):
                    if input_ch == ans[i]:
                        temp += ans[i]
                    elif ans_now[i].isalpha():
                        temp += ans_now[i]
                    else:
                        temp += ans_now[i]
                ans_now = temp
                if ans_now != ans:
                    print('The word looks like: ' + ans_now)
                else:
                    print('You win!!')
            else:
                n_turns-=1
                if n_turns == N_TURNS-1:
                    print('========')
                    print('|    |')
                    print('|   ')
                    print('|  ')
                    print('|  ')
                    print('|  ')
                    print('|  ')
                    print('')
                elif n_turns == N_TURNS - 2:
                    print('========')
                    print('|    |')
                    print('|   ( )')
                    print('|  ')
                    print('|  ')
                    print('|  ')
                    print('|  ')
                    print('')
                elif n_turns==N_TURNS-3:
                    print('========')
                    print('|    |')
                    print('|   ( )')
                    print('|    #  ')
                    print('|  ')
                    print('|  ')
                    print('|  ')
                    print('')

                elif n_turns == N_TURNS - 4:
                    print('========')
                    print('|    |')
                    print('|   ( )')
                    print('|    #  ')
                    print('|    #  ')
                    print('|  ')
                    print('|  ')
                    print('')
                elif n_turns == N_TURNS - 5:
                    print('========')
                    print('|    |')
                    print('|   ( )')
                    print('|  ¬ # ¬ ')
                    print('|    #  ')
                    print('|  ')
                    print('|  ')
                    print('')
                elif n_turns == N_TURNS - 6:
                    print('========')
                    print('|    |')
                    print('|   ( )')
                    print('|  ¬ # ¬ ')
                    print('|    #  ')
                    print('|   / \\ ')
                    print('|  ')
                    print('')
                print('There is no ' + input_ch + '\'s' + ' in the word.')
                print('The word looks like: ' + ans_now)
                print('You have ' + str(n_turns) + ' guesses left.')
                
    print('The word was: ' + ans)




def random_word():
    """
    This function used to generate the random word.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
