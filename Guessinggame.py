import random
import json

data = json.load(open("word.JSON"))
key, value = random.choice(list(data.items()))

word = key

spaces = ['_']* len(word)

def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character ='*'
            word = word[:index]+removed_character+word[index+1:]
            spaces[index] = guess
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
    print("Meaning:"+str(value))
    guess = input('Guess the word:')
 
    if guess in word:
        word, spaces = get_letter_position(guess, word, spaces)
        print(spaces)
    else:
        print('Sorry that letter is not in the word.')
        print('The word is'+key)
     
    if win_check() == 1:
        print('Congratulations you won')
        break
     
    print('you have '+str(num_turns - i)+' turns left.')
    print()