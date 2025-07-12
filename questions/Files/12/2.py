# Q2: Convert contents of automobil.txt to uppercase and write to result.txt
with open("automobil.txt", "r", encoding="utf-8") as infile:
    content = infile.read()

uppercase_content = content.upper()

with open("result.txt", "w", encoding="utf-8") as outfile:
    outfile.write(uppercase_content)
