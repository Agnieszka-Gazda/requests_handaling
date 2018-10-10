import json
import string

def is_question(words, tags):
    for word in words:
        if word.endswith('?'):
            tags.append('need answer')

def make_word_list(words):
    # to strip from interpunction
    for i, word in enumerate(words):
        words[i] = word.strip(string.punctuation)
    #to extract unique values
    words = set(words)
    words = list(words)
    return words


with open("request.json", "r") as read_file:
    data = json.load(read_file)

msg = data["message"]
tags = data["tags"]
words = msg.split(" ")
is_question(words, tags)
words = make_word_list(words)

data["words"] = words
data["tags"] = tags

with open("output.json", "w") as output:
    json.dump(data, output)





