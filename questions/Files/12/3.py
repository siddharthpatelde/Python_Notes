# Q3: Compare two binary files and count differing bytes
with open("test1.bin", "rb") as f1, open("test2.bin", "rb") as f2:
    data1 = f1.read()
    data2 = f2.read()

min_len = min(len(data1), len(data2))
diff = sum(b1 != b2 for b1, b2 in zip(data1[:min_len], data2[:min_len]))
diff += abs(len(data1) - len(data2))  # Count extra bytes in longer file

print("Differences:", diff)
