import random
import sys

strings_to_insert = ["${c1}", "${c2}", "${c3}", 
                     "${c4}", "${c5}", "${c6}"]
problematic = ["$", "{","}","c","1","2","3","4","5","6"]

file_path = sys.argv[1]
with open(file_path, "r") as f:
    text = f.read()

# Get the indices of all non-whitespace characters
indices = [i for i, char in enumerate(text) if char not in [" ", "\n", "\t"]]

# Randomly choose 6 indices to insert the strings
insert_indices = random.sample(indices, 6)

# Iterate through the insert indices and insert the strings
for i, index in enumerate(insert_indices):
        
    if text[index-1] in problematic or text[index+1] in problematic:
        continue
    text = text[:index] + strings_to_insert[i] + text[index:]
    # Update the indices of the remaining insertions to account for the added characters
    insert_indices = [x+len(strings_to_insert[i]) if x > index else x for x in insert_indices]

text = "${c1}" + text

with open(file_path, "w") as f:
    f.write(text)
