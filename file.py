poem = "I never saw a man who looked\n"
poem += "With such a wistful eye\n"
poem += "Upon that little tent of blue\n"
poem += "Which prisoners call the sky\n"

file = open("poem.txt", "w")

file.write(poem)
file.close()

file = open("poem.txt", "r")

print("\nReading in lines:")
for line in file:
    print(line, end="")
file.close()

file = open("poem.txt", "a")
file.write("(Oscar Wilde)")
file.close()

print("\nReading in chunks:")
with open("poem.txt", "r") as file:
    while True:
        chunk = file.read(30)  # Read 30 characters
        if not chunk:  # Evaluates to True when chunk == ''
            break  # EOF reached
        print(chunk, end="")
file.close()
print("\nFinished reading in chunks.")
