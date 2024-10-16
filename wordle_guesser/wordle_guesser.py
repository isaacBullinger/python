import pyautogui
import json
from collections import defaultdict
import time

# import word list
file_path = './wordle_words.json'

with open(file_path, 'r') as file:
  wordle_words = json.load(file)

words = list(wordle_words)

letter_freq = {}

# analyze list and rank letters based on frequency
def add_letter(letter):
  if letter in letter_freq:
    letter_freq[letter] += 1
  else:
    letter_freq[letter] = 1

for word in words:
  for letter in word:
    add_letter(letter)

# sort letters by frequency
sorted_letters = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)

# for letter, count in sorted_letters:
#   print(f"{letter}: {count}")
 
# assign scores to letters by position in the words
letter_pos = defaultdict(lambda: defaultdict(int))

for word in words:
  for index, letter in enumerate(word):
    letter_pos[index][letter] += 1

for position, freq in letter_pos.items():
  sorted_pos = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  # print(f"Position {position}:")
  # for letter, count in sorted_pos:
    # print(f"  {letter}: {count}")

# define colers
green=(75, 140, 82)
yellow=(186, 157, 69)
gray=(58, 58, 60)

# TODO let user calibrate position using cursor (see locate_pixel.py)
# define coordinates for the game board
square = 52
gap = 10
grid_space = square + gap

# print("Move mouse to any corner inside of the top left square in the game. You have 5 seconds.")

# time.sleep(5)

start_x_coord = 340
start_y_coord = 570

# start_x_coord, start_y_coord = pyautogui.position()

coords = []

# print(coords)

# filter words based on pixel colors
def filter_words(words, guess, green_indices, yellow_letters, gray_letters):
  matching_words = []

  for word in words:
    match = True

    for index in green_indices:
      if word[index] != guess[index]:
        match = False
        break

    for letter, indices in yellow_letters.items():
      if letter not in word or any(word[i] == letter for i in indices):
        match = False
        break
    
    letter_counts = {}
    for letter in word:
      letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in gray_letters:
      if letter_counts.get(letter, 0) > 0:
        for i, char in enumerate(word):
          if letter in word and letter not in yellow_letters and all(word[i] != letter for i in green_indices):
            match = False
            break

    if match:
      matching_words.append(word)
  
  return matching_words

def score_word(word):
  score = 0
  for index, letter in enumerate(word):
    score += letter_pos.get(index, {}).get(letter, 0)
  return score

def type_guess(guess):
    print(f"Typing guess: {guess}")
    pyautogui.write(guess)
    time.sleep(0.5)
    pyautogui.press('enter')

turn = 1
guess = 'arise'
green_indices = []
yellow_letters = defaultdict(list)
gray_letters = set()
used_letters = set()

time.sleep(3)

while turn <= 5 and len(words) > 1:
  print(f"Turn {turn}: Guessing '{guess}'")

  type_guess(guess)
  time.sleep(2)

  y_coord = start_y_coord + (turn - 1) * grid_space
  coords = [(start_x_coord + j * grid_space, y_coord) for j in range(5)]

  for i, coord in enumerate(coords):
    pixel = pyautogui.pixel(coord[0], coord[1])

    if pixel == green:
      if i not in green_indices:
        green_indices.append(i)

    elif pixel == yellow:
      if i not in yellow_letters[guess[i]]:
        yellow_letters[guess[i]].append(i)

    else:
      gray_letters.add(guess[i])

  if len(green_indices) == 5:
    print("All green! Stopping guesses.")
    break

  words = filter_words(words, guess, green_indices, yellow_letters, gray_letters)

  words = sorted(words, key=score_word, reverse=True)
  print(words)

  if words:
    guess = words[0]
    print(f"Next guess: {guess}")

    used_letters.update(set(guess))
  else:
    break

  turn += 1

print("End of game.")