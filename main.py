# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(first_word, second_word):
    # [assignment] Add your code here

    first_word = first_word.lower()
    second_word = second_word.lower()
    
    if(len(first_word) != len(second_word)):
        return False

    while len(first_word) > 0:
        k = 0
        while len(second_word) > 0:
            if(first_word[0] == second_word[k]):
                # deleting matching characters
                first_word = first_word.replace(first_word[0], '')
                second_word = second_word.replace(second_word[k], '')
                break

            k += 1

            # if it did not find the matching character
            if(k >= len(second_word)):
                return False

    return True


print(find_anagrams('creative', 'reactive'))