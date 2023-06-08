message = input(">")
words = message.split(' ') # splits string into words separated by spaces, creates list

emojis = {
    ":)": "happy",
    ":(": "sad",
    "-_-": "meh"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " " # get method: Return the value for key if key is in the dictionary, else default
print(output)

# emojis did not work, so I used words

