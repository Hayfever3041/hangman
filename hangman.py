# hangman

import random
from sys import exit

def listToStringSpaces(s):
    str1 = ', '
    return (str1.join(s))

def listToString(s):
    str1 = ' '
    return (str1.join(s))

def listToStringNoSpaces(s):
    str1 = ''
    return (str1.join(s))

def split(word):
    return [char for char in word]

def startup():
    print('''
Welcome to Hangman!
You will try to guess a word.
You have 6 guesses.
'''.format(GUESSES))

def get_word(WORDS):
    return random.choice(WORDS)

def setup(word):
    word_player = []
    for i in range(len(word)):
        word_player.append('_')
    word_list = split(word)
    return [word_player, word_list, [], ]
    


def ask(GUESSES, guesses, incorrect, word_visible):

    while True:
        print('Press ENTER to view what is wrong.')
        print('What do you want to guess?:')
        guess = input('>>> ')

        if guess == '':
            print('You have gotten wrong', listToStringSpaces(incorrect).upper(), sep = ': ')
            continue
        elif guess in word_visible or guess in incorrect:
            print('Uh-oh, looks like you have already guessed that!')
            continue
        elif len(guess) > 1:
            print('That is more than one character!')
            continue
        else:
            break
        

    return [guess,  guesses]
    
    

def checking(guess, word_player, guesses):

    if int(guesses) >= GUESSES:
        return 'OutGuessError'
    
    word_visible = word_player[0]
    word_list = word_player[1]
    incorrect = word_player[2]
    matched_indexes = []
    l = 0

    if guess in word_list:
        while l < len(word_list):
            if guess == word_list[l]:
                matched_indexes.append(l)
            l += 1
        for i in matched_indexes:
            word_visible[i] = guess
                
    else:
        print('That letter is not in the word.')
        incorrect.append(guess)
        guesses += 1
        

    return [word_visible, word_list, incorrect, guesses]

def hangman(guesses):
    if guesses == 0:
        print('''
|----|
|    |
|
|
|
|
------
''')
    elif guesses == 1:
        print('''
|----|
|    |
|    O
|
|
|
------''')
    elif guesses == 2:
        print('''
|----|
|    |
|    O
|    |
|
|
------''')
    elif guesses == 3:
        print('''
|----|
|    |
|    O
|   /|
|
|
------''')
    elif guesses == 4:
        print('''
|----|
|    |
|    O
|   /|\\
|
|
------''')
    elif guesses == 5:
        print('''
|----|
|    |
|    O
|   /|\\
|   /
|
------''')
    elif guesses == 6:
        print('''
|----|
|    |
|    O
|   /|\\
|   / \\
|
------''')
        print('You lost!')
        exit()

# words
WORDS = ['chase', 'lip', 'wander', 'crop', 'payment', 'wedding', 'unlikely', 'redeem', 'consider', 'immune',
         'official', 'expenditure', 'sword', 'flash', 'orthodox', 'baseball', 'ostracize', 'collar', 'plant',
         'cereal', 'graphic', 'public', 'disagree', 'theft', 'electron', 'absorption', 'burial', 'season',
         'inhabitant', 'bedroom', 'lead', 'contract', 'spell', 'gasp', 'swim', 'conception', 'archive', 'state',
         'convulsion', 'recommend', 'greeting', 'future', 'concrete', 'layer', 'fragment', 'hot',
         'cancel', 'god', 'experiment']
# number of guesses
GUESSES = 6

# setup of game
startup()
word = get_word(WORDS)
word_player = setup(word)
guess = ['', 0]
check = [word_player[0], word_player[1], word_player[2], guess[0]]
guesses = 0


# run game
while True:
    guess = ask(GUESSES, guess[1], word_player[2], check[0])
    
    check = checking(guess[0], word_player, guesses)

    if guess == 'OutGuessError':
        print('You lost')
        print('The word was {}.'.format(word))
        exit()
        
    word_player = check
    guesses = check[3]
    print(listToString(check[0]))
    hangman(guesses)
    if listToStringNoSpaces(check[0]) == word:
        print('You win!')
        print('The word was ', listToStringNoSpaces(check[0]), '!', sep = '')
        exit()
