from random import randint

difficulty = str(input('Easy, Medium, or Hard difficulty?')).lower()

WhiteList = [
    'easy',
    'medium',
    'hard',
]

if not difficulty in WhiteList:
    print('Please enter a valid difficulty next time!')

def random_number_generator(min, max):
    return randint(min, max)

def number_check(num):
    if num in range(1, 11):
        return True
    else:
        return False

difficulty_details = {
    'easy': [1, 11, 3],
    'medium': [1, 11, 2],
    'hard': [1, 11, 1],
}

ranges = list(difficulty_details.get(difficulty))

lives = int(ranges[-1])

random_number = random_number_generator(ranges[0], ranges[1])

while lives > 0:
    try:

        guess = int(input('You have {} lives. Enter a number between 1 and 10.'.format(lives)))
        
        if number_check(guess) == True:
            if guess == random_number:
                print('You Win! Congratulations!')
                break
            else:
                print('Incorrect')
                lives -= 1
                if lives == 0:
                    print('You Lose.')

    except ValueError:
        print('You must enter a number between 1 and 10.')