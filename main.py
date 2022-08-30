import json
from collections import Counter

data = json.load(open ('dictionary_compact.json'))
user = input('what is the word?')
new = []

for i in data:
    if Counter(user) == Counter(i) and i != user:
        new.append(i)
    else:
        continue

if len(new) > 0:
  print(f"Anagrams for {user} : {new} ")
else:
    print('Sorry, no anagrams for this word!')