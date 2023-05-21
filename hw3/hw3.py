# ******** HW3 ******** #
## part A Warm-up

def sudoku_is_legal(board):
    # horizontal check:
    for hori_line in board:
        if sorted(hori_line) != list(range(1,10)):
            return False

    # vertical check:
    for verti_i in range(9):
        verti_line = []
        for hori_line in board:
            verti_line.append(hori_line[verti_i])
        if sorted(verti_line) != list(range(1,10)):
            return False

    # boxes check:
    for row in [0,3,6]:
        for col in [0,3,6]:
            box = []
            for line in board[row:row+3]:
                box.extend(line[col:col+3])
            if sorted(box) != list(range(1,10)):
                return False

    return True


## part B string manipulation
# function 1 change_tone
def change_tone(phrase, new_tone):
    # identifing tone
    # (index of punctuation with be used later when the algorithm will slice the original phrase)
    if phrase[-2:] == '!?':
        punc, index = '!?', -2
    elif phrase[-1:] == '!' or phrase[-1:] == '?':     # index "-1:" prevents problems with empty strings
        punc, index = phrase[-1], -1
    elif phrase[-1:].isalpha():
        punc, index = 'other', len(phrase)
    else:
        punc, index = 'other', -1

    # a dictionary where {key=phrase ending punctuation: value=(same tone punctuation, opposite tone punctuation)}
    punc_dict = {'!':('!?', '?'),
                   '?':('', '!'),
                   '!?':('!', ''),
                   'other':('?','!?')}

    if new_tone:
        new_phrase = phrase[:index] + punc_dict[punc][1]
    else:
        new_phrase = phrase[:index] + punc_dict[punc][0]

    return new_phrase



# function 2 be_polite
def be_polite(paragraph):
    # splits sentences by the dot, changes tone for every sentence, and rejoins them to a paragraph.
    sentences = paragraph.split('.')
    polite_sentences = []
    for sentence in sentences:
        new_sentence = change_tone(sentence, True)
        polite_sentences.append(new_sentence)
    return '.'.join(polite_sentences)




## part C data structures


# function 1 print_chars(phrase, reapeat)
def print_chars(phrase, repeat):
    # collects all characters into a list and sorts them
    char_list = []
    for char in phrase:
        if not repeat and char in char_list: # if repeat is false, don't include duplicates
            continue
        char_list.append(char)
    return sorted(char_list)



# function a1 - orientation_day_registery
def orientation_day_registery(all_listed_students):

    # function: changes names into the right format
    def fix_name(name):
        fixed_name = name[0].upper() + name[1:].lower()
        return fixed_name

    new_database = {}

    for string in all_listed_students:
        record = string.split()
        full_name = fix_name(record[0]) + " " + fix_name(record[1]) # fixing first and last names
        if record[2].isdigit():  # checks if grade is a number
            SAT = int(record[2])
            if SAT < 200 or SAT > 800:
                SAT = 200
        else:
            SAT = 200
        new_database[full_name] = SAT

    return new_database





# function b1 - get_number_of_honorary
def get_number_of_honors(students):
    # counts students based on grade
    count = 0
    for grade in students.values():
        if grade >= 750:
            count += 1
    return count


# function b2 - get_with_honors
def get_honors(students, min_grade):
    honorary_list = []

    # sort the dictionary by values (grades)
    students_sorted = sorted(students, key=students.get, reverse=True)

    for name in students_sorted:
        if students[name] >= min_grade:
            honorary_list.append(name)

    return honorary_list



# function b3 - get_with_honors_by_avg
def get_with_honors_by_avg(students_list):
    # organize input
    student_records = orientation_day_registery(students_list)

    average = sum(student_records.values()) / len(student_records.values())
    above_avg_list = get_honors(student_records, average)

    return (average, above_avg_list)



# ******** GOOD LUCK ******** #