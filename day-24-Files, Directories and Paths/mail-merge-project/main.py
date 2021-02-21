# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# invited_names = []
with open("input/Names/invited_names.txt") as file:
    invited_names = file.readlines()
for i in range(len(invited_names)):
    invited_names[i] = invited_names[i].strip()
print(invited_names)

# Replace the [name] placeholder with the actual name.
with open("input/Letters/starting_letter.txt") as file:
    text = file.readlines()

for i in range(len(invited_names)):
    # Replace [name] with the actual name.
    new_text = text[:]
    new_text[0] = new_text[0].replace("[name]", invited_names[i])

    # Save the letters
    file_path = f"Output/ReadyToSend/letter_for_{invited_names[i]}.txt"
    with open(file_path, mode="w") as f:
        f.writelines(new_text)


# Save the letters in the folder "ReadyToSend".


    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp