"""game target"""
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    vowels = ['A', 'E', 'I', 'O','U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J','K','L','M','N','P','Q','R',\
                  'S','T','V','W','X','Y','Z']
    vowels = random.choices(vowels, k=3)
    consonants = random.choices(consonants, k=6)
    letters = vowels + consonants
    random.shuffle(letters)
    grid = [letters[i:i+3] for i in range(0, len(letters), 3)]
    return grid

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f"week7/{f}", "r", encoding="utf-8") as file:
        content = file.read()
        words = content.splitlines()
        words = [el for el in words if letters[4] in el and len(el)>=4 and el.islower()]
        words_set = set(words)
        words = list(words_set)
        checked_words = []
        for word in words:
            check = True
            for el in word:
                count_letters = letters.count(el)
                count_letters_in_word = word.count(el)
                if count_letters == 0:
                    check = False
                    break
                if count_letters_in_word > count_letters:
                    check = False
                    break
            if check is True:
                checked_words.append(word)
        return sorted(checked_words)


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    arr = []
    try:
        while True:
            user_words = input()
            arr.append(user_words)
    except EOFError:
        pass
    return arr


def get_pure_user_words(user_words: list[str], letters: list[str],\
                         words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    words = [el for el in user_words if letters[4] in el and len(el)>=4 and el.islower()]
    words = [el for el in words if el not in words_from_dict]
    return words


def main():
    """
    Main function
    """
    letters = generate_grid()
    print(f'Your board is {letters}')
    letters = [el.lower() for row in letters for el in row]
    print('Please, suggest your words here:')
    user_words = get_user_words()
    words_from_dict = get_words('en.txt',letters)
    right_words = [word for word in user_words if word in words_from_dict]
    print(f"Number of the right words: {len(right_words)}")
    print("All possible words:")
    print(words_from_dict)
    missed_words = [word for word in words_from_dict if word not in user_words]
    print('You missed the followind words:')
    print(missed_words)
    print("You suggest, but we don't have them in the dictionary:")
    print(get_pure_user_words(user_words, letters, words_from_dict))

main()