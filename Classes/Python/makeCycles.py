
# 1. Ask the user to enter some text (any).
print("Please enter text you'd like to have repeated on the screen:")
userText = input()

# 2. Then ask the user to enter how many times they want to print it (eg 10).
print("How many times would you like to have it repeated on the screen?")
repeatRequest = int(input())

for i in range(repeatRequest):
    print(userText)

print("The text [" , userText , "] was repeated", repeatRequest , "times as requested.")
# Remember that the program must print the text entered the requested number of times, and finish.
