import json

word_list = []
five_words = []

with open('words_dictionary.json') as words:
  word_list = json.load(words)

for word in word_list:
  if len(word) == 5:
    five_words.append(word)

with open('5_letter_words.json', 'w') as words:
  json.dump(five_words, words)
