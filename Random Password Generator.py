# RANDOM PASSWORD GENERATOR: REQUESTS CHARACTER COUNT FROM USER (LETTERS, NUMBERS, AND SPECIAL CHARACTERS)
# AND RETURNS A RANDOMIZED PASSWORD MEETING THAT CRITERIA.
##########################################################################################################
import random
import string

def random_pass_generator():

    new_generated_pass = []
    rand_choice_upper = [0,1]

    final = ''

    u_input_letter_count = int(input('How many letters do you want for your password?'))
    u_input_number_count = int(input('Thank you, and how many numbers?'))
    u_input_special_count = int(input("Let's add special characters for an extra layer of security. How many special characters do you want?"))

    for i in range(u_input_letter_count):
        rand_choice = random.choice(string.ascii_lowercase)
        rand_upper = random.choice(rand_choice_upper)
        if rand_upper == 1:
            rand_choice = rand_choice.upper()
        new_generated_pass.append(rand_choice)

    new_generated_pass[0].upper()

    for i in range(u_input_number_count):
        rand_choice = random.choice(string.digits)
        new_generated_pass.append(rand_choice)

    for i in range(u_input_special_count):
        rand_choice = random.choice(string.punctuation)
        new_generated_pass.append(rand_choice)

    random.shuffle(new_generated_pass)
    
    for i in new_generated_pass:
        final = final + i

    print('Thank you for your input!','\n')
    print('All set. Your new password is:')
    print(final)

#######################################################################################################
def main():
    print("Hello! Welcome to Jose's Random Password Generator!", '\n')
    random_pass_generator()

main()
