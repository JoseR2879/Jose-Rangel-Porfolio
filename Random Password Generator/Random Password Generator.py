# RANDOM PASSWORD GENERATOR: REQUESTS CHARACTER COUNT FROM THE USER (LETTERS, NUMBERS, AND SPECIAL CHARACTERS)
# AND RETURNS A RANDOMIZED PASSWORD MEETING THAT CRITERIA.
##########################################################################################################
import random
import string

def random_pass_generator():
    '''REQUESTS INPUT FROM USER THEN USES DIFFERNT METHODS TO GENERATE A RANDOM PASSOWORD'''
    
    new_generated_pass = []
    rand_choice_upper = [0,1]

    final_pass = ''

    u_input_letter_count = int(input('How many letters do you want for your password?'))
    u_input_number_count = int(input('Thank you, and how many numbers?'))
    u_input_special_count = int(input("Let's add special characters for an extra layer of security. How many special characters do you want?"))

    for i in range(u_input_letter_count):
        #USES THE LOWERCASE STRING LIBRARY AND RANDOM CHOICE METHOD TO GENERATE RANDOM LETTERS FROM ALPHABET (A-Z)
        rand_choice = random.choice(string.ascii_lowercase)   
        rand_upper = random.choice(rand_choice_upper)
        #USES RANDOM CHOICE FROM A LIST TO DETERMINE IF TO CAPITALIZE LETTER OR LEAVE LOWERCASE (50% CHANCE)
        # THEN APPENDS EACH LETTER TO A LIST (NEW_GENERATED_PASS)
        if rand_upper == 1:
            rand_choice = rand_choice.upper()
        new_generated_pass.append(rand_choice)
    #ADDED CODE LINE TO ENSURE PASSWORD WILL ALWAYS CONTAIN AN UPPER LETTER REGARDLESS OF RANDOM CHOICES ABOVE
    new_generated_pass[0].upper()

    for i in range(u_input_number_count):
        #USES THE STRING DIGITS LIBRARY AND RANDOM CHOICE METHOD TO GENERATE RANDOM NUMBERS (FROM 0-9)
        # THEN APPENDS EACH NUMBER TO A LIST (NEW_GENERATED_PASS)
        rand_choice = random.choice(string.digits)
        new_generated_pass.append(rand_choice)

    for i in range(u_input_special_count):
        #USES THE STRING PUNCTUATION LIBRARY AND RANDOM CHOICE METHOD TO GENERATE RANDOM SPECIAL CHARACTERS
        # THEN APPENDS EACH CHARACTER TO A LIST (NEW_GENERATED_PASS)
        rand_choice = random.choice(string.punctuation)
        new_generated_pass.append(rand_choice)
    #SHUFFLES ALL ITEMS IN NEW PASSWORD LIST TO FURTHER RANDOMIZATION OF PASSWORD ORDER
    random.shuffle(new_generated_pass)
    #EXTRACTS ALL ITEMS IN LIST INTO A STRING TO SERVE AS THE FINAL PASSWORD PROVIDED TO USER
    for i in new_generated_pass:
        final_pass = final_pass + i

    print('Thank you for your input!','\n')
    print('All set. Your new password is:')
    print(final_pass)

#######################################################################################################
def main():
    ''' CALLS MAIN TO BEGIN EXECUTING PROGRAM FUNCTION AND GENERATE PASS TO USER'''
    
    print("Hello! Welcome to Jose's Random Password Generator!", '\n')
    random_pass_generator()

main()
