#This is the python program to learn english vocabulary with fun
#In this program i have downloaded the JSON file that already contains the word and meaning of more than 100K words.
#I have retreive the worwd from the JSON file using the RANDOM module. The program tells user to guess the word by
#providing the meaning. ...
import random
import json

def option1():

    data = json.load(open("word.JSON"))
    key, value = random.choice(list(data.items()))

    spaces = ['_']* len(key)

    def get_letter_position(key, word, spaces):
        index = -2
        while index != -1:
            if key in word:
                index = word.find(key)
                removed_character ='*'
                word = word[:index]+removed_character+word[index+1:]
                spaces[index] = key
            else:
                index = -1
        return (word, spaces)

    def win_check():
        for i in range(0, len(spaces)):
            if spaces[i] == '_':
                return -1
        return 1
    num_turns = len(word)
    for i in range(-1, num_turns):
        key = input('Guess a character:')
        if key in word:
            word, spaces = get_letter_position(key, word, spaces)
            print(spaces)
        else:
            print('Sorry that letter is not in the word.')
            
        if win_check() == 1:
            print('Congratulations you won')
            break
        
        print('you have '+str(num_turns - i)+' turns left.')
        print()

def check_type(ans):
    try:
        ans = int(ans)
        return ans
    except Exception as exception:
        print('-'*50+'\n')
        print('Exception:' + str(exception))
        print('-'*50+'\n')

def main():
    print("*"*20)
    print("Welcome to Learn_Vocab app....")
    print("*"*50)

    while True:
        print("1.Start learning\n2.View History\n3.Exit")
        ans = input("Select any one option[1,2,3]")
        ans = check_type(ans)

        if ans == 1:
            option1()
        elif ans == 2:
            print("-"*50)
            print("Closing the program.....")
            print("Keep learning.....")
            print("-"*50)
        else:
            print("Please choose the number in between 1-3")

if __name__ == '__main__':
    main()