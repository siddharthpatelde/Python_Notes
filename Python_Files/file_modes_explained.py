# File Access Modes – What They Mean

# --------------------------------------------
# Common Text File Modes
# --------------------------------------------

# 'r'  = Read mode (default); file must exist
# 'w'  = Write mode; creates file if it doesn't exist, overwrites if it does
# 'a'  = Append mode; writes to end of file, creates it if it doesn’t exist
# 'x'  = Create mode; creates file, fails if it already exists

# Example:
file = open('example.txt', 'r')  # Read
file.close()

file = open('example.txt', 'w')  # Write (overwrites)
file.close()

file = open('example.txt', 'a')  # Append
file.close()

file = open('new_file.txt', 'x')  # Create (raises error if exists)
file.close()

# --------------------------------------------
# Binary File Modes (for non-text data like images or audio)
# --------------------------------------------

# 'rb' = Read binary
# 'wb' = Write binary (overwrite)
# 'ab' = Append binary
# 'xb' = Create binary

# Example:
with open('image.jpg', 'rb') as file:
    data = file.read()

with open('audio.mp3', 'wb') as file:
    file.write(bytes([1, 2, 3]))
