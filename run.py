""" gspread is a Python API for Google Sheets. """
import gspread
from google.oauth2.service_account import Credentials
from collections import Counter
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Enviro')

"""
Survey starts here. The questions are in a group list.
I used https://realpython.com/python-quiz-application/ to help me understand how to build this survey.
"""
print("\nPlease answer the following questions by choosing one of the provided answers.\n")
q_list = [
        ["question 1", "Do you commute most often by ", "a: car", "b: bicycle", "c: public transport", "d: other", ],
        ["question 2", "Where do you most often learn about climate change ", "a: internet", "b: radio/tv", "c: newspaper", "d: other", ],
        ["question 3", "Which of the following do you think affects you the most ", "a: air pollution", "b: water pollution", "c: soil pollution", "d: other", ],
        ["question 4", "What is your age ", "a: under 18", "b: 19-30", "c: 31-49", "d: 50+", ]
            ]
"""
Get answer input from the user.
Run a while loop to collect a valid string of answers from the user via the terminal.
The loop will repeatedly request an answer until it is valid.
"""

# save list of answers
answers_list = []

# Try except ressource used from here:
# https://avidpython.com/python-basics/when-to-use-try-except-instead-of-if-else/#:~:text=We%20can%20use%20try%2Dexcept%20for%20exception%20handling%20(handling%20system,exceptions%20or%20system%2Dgenerated%20errors.

for q in q_list[0:5]:
    answer = input(f"{q[1]}:\n - {q[2]} \n - {q[3]} \n - {q[4]} \n - {q[5]} \nplease type your answer here: \n")
    print("")
    while True:
        if answer == "a" or answer == "b" or answer == "c" or answer == "d":
            answers_list.append(answer)
            break
        else:
            print(f"You must choose one answer from the list above. You provided:\n" f"{(answer)}\n")
            answer = input("Please type your answer here: \n")
            print("")

print('Thank you for completing the survey. \n')

# Add all answers from the answers list to the google worksheet
worksheet_to_update = SHEET.worksheet('count')
# add to the worksheet
worksheet_to_update.append_row(answers_list)

# x = SHEET.worksheet('count').col_values(1)
# print('These were the most popular answers out of the', len(x)-8, 'participants: \n')

# I used this to help me: https://stackoverflow.com/questions/47271232/use-of-try-except-for-input-validation

def endMessage():
    x = SHEET.worksheet('count').col_values(1)
    try:
        if len(x) <= 9:
            raise (KeyError)
        else:
            print('These were the most popular answers out of the', len(x)-8, 'participants:')
    except KeyError:
        print("You are the first participant! Come back later to see more results.")
        sys.exit()


endMessage()

# I used the https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list to help me build the next section.

yellow_col_1 = (SHEET.worksheet('count').col_values(5))
green_col_1 = (SHEET.worksheet('count').col_values(1))
del green_col_1[0:8]
mostPopular_1 = [green_col_1 for green_col_1, word_count in Counter(green_col_1).most_common(1)]

yellow_col_1_int = []
for item in yellow_col_1:
    if item != '':
        item = int(item)
        yellow_col_1_int.append(item)

if mostPopular_1 == ['a']:
    print(max(yellow_col_1_int), 'participants answered "car" for question 1')
elif mostPopular_1 == ['b']:
    print(max(yellow_col_1_int), 'participants answered "bicycle" for question 1')
elif mostPopular_1 == ['c']:
    print(max(yellow_col_1_int), 'participants answered "public transport" for question 1')
elif mostPopular_1 == ['d']:
    print(max(yellow_col_1_int), 'participants answered "other" for question 1')

yellow_col_2 = (SHEET.worksheet('count').col_values(6))
green_col_2 = (SHEET.worksheet('count').col_values(2))
del green_col_2[0:8]
mostPopular_2 = [green_col_2 for green_col_2, word_count in Counter(green_col_2).most_common(1)]

yellow_col_2_int = []
for item in yellow_col_2:
    if item != '':
        item = int(item)
        yellow_col_2_int.append(item)

if mostPopular_2 == ['a']:
    print(max(yellow_col_2_int), 'participants answered "internet" for question 2')
elif mostPopular_2 == ['b']:
    print(max(yellow_col_2_int), 'participants answered "radio/tv" for question 2')
elif mostPopular_2 == ['c']:
    print(max(yellow_col_2_int), 'participants answered "newspaper" for question 2')
elif mostPopular_2 == ['d']:
    print(max(yellow_col_2_int), 'participants answered "other" for question 2')

yellow_col_3 = (SHEET.worksheet('count').col_values(7))
green_col_3 = (SHEET.worksheet('count').col_values(3))
del green_col_3[0:8]
mostPopular_3 = [green_col_3 for green_col_3, word_count in Counter(green_col_3).most_common(1)]

yellow_col_3_int = []
for item in yellow_col_3:
    if item != '':
        item = int(item)
        yellow_col_3_int.append(item)

if mostPopular_3 == ['a']:
    print(max(yellow_col_3_int), 'participants answered "air pollution" for question 3')
elif mostPopular_3 == ['b']:
    print(max(yellow_col_3_int), 'participants answered "water pollution" for question 3')
elif mostPopular_3 == ['c']:
    print(max(yellow_col_3_int), 'participants answered "soil pollution" for question 3')
elif mostPopular_3 == ['d']:
    print(max(yellow_col_3_int), 'participants answered "other" for question 3')

yellow_col_4 = (SHEET.worksheet('count').col_values(8))
green_col_4 = (SHEET.worksheet('count').col_values(4))
del green_col_4[0:8]
mostPopular_4 = [green_col_4 for green_col_4, word_count in Counter(green_col_4).most_common(1)]

yellow_col_4_int = []
for item in yellow_col_4:
    if item != '':
        item = int(item)
        yellow_col_4_int.append(item)

if mostPopular_4 == ['a']:
    print(max(yellow_col_4_int), 'participants answered "under 18" for question 4')
elif mostPopular_4 == ['b']:
    print(max(yellow_col_4_int), 'participants answered "19-30" for question 4')
elif mostPopular_4 == ['c']:
    print(max(yellow_col_4_int), 'participants answered "31-49" for question 4')
elif mostPopular_4 == ['d']:
    print(max(yellow_col_4_int), 'participants answered "50+" for question 4')
