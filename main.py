with open("Mail Merge/invited_names.txt", "r") as f:
    name_list = f.readlines()

with open('Mail Merge/starting_letter.txt') as text_file:
    starting_letter = text_file.read()

for names in name_list:
    stripped_name = names.strip()
    new_letter = starting_letter.replace('[name]', stripped_name)
    with open(f'Mail Merge/ready_to_send/letter_for_{stripped_name}.txt', mode='w') as fp:
        fp.write(new_letter)



