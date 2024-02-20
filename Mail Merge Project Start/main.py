# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as invite:
    invitees = invite.readlines()
    for person in invitees:
        new_person = person.strip()

        with open("./Input/Letters/starting_letter.txt") as letter:
            start_letter = letter.read()
            new_letter = start_letter.replace("[name]", new_person)

            with open(f"./Output/ReadyToSend/letter_for_{new_person}.txt", mode='w') as invite_letter:
                invite_letter.write(new_letter)


# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
