with open('Input/Letters/starting_letter.txt') as starting_letter:
    letter_contents = starting_letter.read()
with open('Input/Names/invited_names.txt') as invitees:
    names = invitees.readlines()

for name in names:
    new_name = name.strip()
    new_letter = letter_contents.replace('[name]', new_name)
    with open(f"Output/ReadyToSend/letter_to_{new_name}", mode='w') as letter:
        letter.write(new_letter)
