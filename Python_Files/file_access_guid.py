# Lesson 25: File Access in Python

# --------------------------------------------
# 1. Opening and Closing Files
# --------------------------------------------

# Open a text file for reading
txtfile = open('file.txt', 'r')

# Open a binary file for writing
binfile = open('file.bin', 'wb')

# Open with encoding (e.g., for German umlauts)
file_with_umlauts = open('umlauts.txt', 'r', encoding='utf-8')

# Always close files after use
txtfile.close()
binfile.close()

# --------------------------------------------
# 2. Recommended: Using `with` for safer file handling
# --------------------------------------------

with open('file.txt', 'r') as file:
    content = file.read()
print(content)  # file is automatically closed after this block

# --------------------------------------------
# 3. Reading Entire File vs. Line-by-Line
# --------------------------------------------

# Read all lines into a list
with open('file.txt', 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}: {line}", end='')

# Read file line by line using readline()
with open('file.txt', 'r') as file:
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()

# Even shorter with iterator
with open('file.txt', 'r') as file:
    for line in file:
        print(line, end='')

# --------------------------------------------
# 4. Writing to a Text File
# --------------------------------------------

with open('file.txt', 'w') as file:
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')
    file.write('This is the third line.\n')

# --------------------------------------------
# 5. Reading from a Binary File
# --------------------------------------------

with open('file.bin', 'rb') as file:
    bytes_data = file.read(10)  # read 10 bytes

for byte in bytes_data:
    print(byte)

# --------------------------------------------
# 6. Writing to a Binary File
# --------------------------------------------

with open('file.bin', 'wb') as file:
    file.write(bytes([0, 1, 2, 3, 4, 5]))
