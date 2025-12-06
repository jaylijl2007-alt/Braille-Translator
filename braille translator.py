from turtle import *

# Question 1 --------------------------------------------------------------------------------

def addLetters(bd):
    '''
    Adds Braille representations for all Grade-1 representations 
    of Braille for the English alphabet. 
    return: None
    '''
    bd['a'] = [1, 0, 0, 0, 0, 0]
    bd['b'] = [1, 1, 0, 0, 0, 0]
    bd['c'] = [1, 0, 0, 1, 0, 0]
    bd['d'] = [1, 0, 0, 1, 1, 0]
    bd['e'] = [1, 0, 0, 0, 1, 0]
    bd['f'] = [1, 1, 0, 1, 0, 0]
    bd['g'] = [1, 1, 0, 1, 1, 0]
    bd['h'] = [1, 1, 0, 0, 1, 0]
    bd['i'] = [0, 1, 0, 1, 0, 0]
    bd['j'] = [0, 1, 0, 1, 1, 0]

    bd['k'] = [1, 0, 1, 0, 0, 0]
    bd['l'] = [1, 1, 1, 0, 0, 0]
    bd['m'] = [1, 0, 1, 1, 0, 0]
    bd['n'] = [1, 0, 1, 1, 1, 0]
    bd['o'] = [1, 0, 1, 0, 1, 0]
    bd['p'] = [1, 1, 1, 1, 0, 0]
    bd['q'] = [1, 1, 1, 1, 1, 0]
    bd['r'] = [1, 1, 1, 0, 1, 0]
    bd['s'] = [0, 1, 1, 1, 0, 0]
    bd['t'] = [0, 1, 1, 1, 1, 0]

    bd['u'] = [1, 0, 1, 0, 0, 1]
    bd['v'] = [1, 1, 1, 0, 0, 1]
    bd['x'] = [1, 0, 1, 1, 0, 1]
    bd['y'] = [1, 0, 1, 1, 1, 1]
    bd['z'] = [1, 0, 1, 0, 1, 1]

    bd['w'] = [0, 1, 0, 1, 1, 1]

# ---- Upgrade braille_dictionary from a grade 1 dictionary to a grade 2 ----

def addWords(bd):
    '''Expands the dictionary to include Grade-2 braille words.
    return: None'''
    bd['but'] = [1, 1, 0, 0, 0, 0]
    bd['can'] = [1, 0, 0, 1, 0, 0]
    bd['do'] = [1, 0, 0, 1, 1, 0]
    bd['every'] = [1, 0, 0, 0, 1, 0]
    bd['from'] = [1, 1, 0, 1, 0, 0]
    bd['go'] = [1, 1, 0, 1, 1, 0]
    bd['have'] = [1, 1, 0, 0, 1, 0]
    bd['just'] = [0, 1, 0, 1, 1, 0]
    bd['knowledge'] = [1, 0, 1, 0, 0, 0]
    bd['like'] = [1, 1, 1, 0, 0, 0]
    bd['more'] = [1, 0, 1, 1, 1, 0]
    bd['not'] = [1, 0, 1, 1, 1, 0]
    bd['people'] = [1, 1, 1, 1, 0, 0]
    bd['quite'] = [1, 1, 1, 1, 1, 0]
    bd['rather'] = [1, 1, 1, 0, 1, 0]
    bd['so'] = [0, 1, 1, 1, 0, 0]
    bd['that'] = [0, 1, 1, 1, 1, 0]
    bd['us'] = [1, 0, 1, 0, 0, 1]
    bd['very'] = [1, 1, 1, 0, 0, 1]
    bd['it'] = [1, 0, 1, 1, 0, 1]
    bd['you'] = [1, 0, 1, 1, 0, 1]
    bd['as'] = [1, 0 , 1, 0, 1, 1]
    bd['will'] = [0, 1, 0, 1, 1, 1]

braille_dictionary = {}
addLetters(braille_dictionary)
addWords(braille_dictionary)

#braille_dictionary: "keyword": [list of # for braille]
# ==============================================================
# Question 2
# ------------------ You're to modify this one... ---------------------------

def translator(sentence, bd):
    '''Using the provided dictionaries of common words and characters 
    of the English alphabet from above, translates an inputted English sentence 
    in the form of a string into braille, in the form of a list of 1s and 0s
    (with 1s representing a bump and 0's)'''
    braille_output = []
    # Prepares the sentence for iterating.
    sentence = sentence.lower()
    list_of_words = sentence.split()
    print (list_of_words)
        
    for word in list_of_words:
        if word in bd:          # Common grade 2 words are simply appended to the output list. 
            braille_output.append(bd[word])
    else:                       # Detects if a word is not stored in braille_dictionary. 
        list_of_chars = []
        for char in word:
            if char not in bd:
                    continue
            list_of_chars.append(bd[char])
        braille_output.append(list_of_chars)
    return braille_output

def print_braille(lst):
    line1 = ''
    line2 = ''
    line3 = ''
    for item in lst:
        if isinstance(item[0], list):
            for next in item:
                line1 = line1 + str(next[0]) + ' '
                line2 = line2 + str(next[1]) + ' '
                line3 = line3 + str(next[2]) + ' '
                line1 = line1 + str(next[3]) + ' '
                line2 = line2 + str(next[4]) + ' '
                line3 = line3 + str(next[5]) + ' '
        elif isinstance(item[0], int):
            line1 = line1+ str(item[0]) + ' '
            line2 = line2+ str(item[1]) + ' '
            line3 = line3+ str(item[2]) + ' '
            line1 = line1+ str(item[3]) + ' '
            line2 = line2+ str(item[4]) + ' '
            line3 = line3+ str(item[5]) + ' '
        else:
            assert 'Error in braille string'
    print(line1)
    print(line2)
    print(line3)

# ==============================================================
# Question 3

def draw_word(lst):
    '''
    Iterates over the given list of words 
    and in the case of an uncommon word, 
    iterates over that list of characters. 
    Any symbols or numbers produce 
    an Error string output
    return: None
    '''
    for item in lst:
        if isinstance(item[0], list):
            for next in item:
                draw_braille_character(next)
        elif isinstance(item[0], int):
            draw_braille_character(item)
        else:
            assert 'Error in braille string'

def draw_braille_character(bc):
    '''
    Creates a 2 x 6 grid of a singular braille 
    character/word
    Acts as a helper function for draw_word() 
    in case an uncommon word is encountered
    return: True 
    '''
    penup()
    x,y = position()
    positions = [(0,0),(0,-15),(0, -30),(15,0),(15,-15),(15,-30)]

    for i in range(6):
        penup()
        new_x, new_y = positions[i]
        goto(x + new_x, y + new_y)
        pendown()

        if bc[i] == 1:
            begin_fill()
            circle(5)
            end_fill()
        else:
            circle(5)
        penup()
    goto(x + 40, y)
    return True

# Testing calls here

if __name__ == '__main__':
    print('My tests:')
    
    ## Put test calls to Question 2 here
    print_braille(translator('every computer', braille_dictionary))

    ## Put test calls to Question 3 here
    draw_word(translator('every computer', braille_dictionary))
