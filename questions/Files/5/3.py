while True:
    text = input("Input: ").strip()
    if text.lower() == "ende":
        break
    print("Output:", text.upper())
