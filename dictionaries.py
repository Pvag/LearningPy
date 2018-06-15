# In this file, many exercises to get to know Dictionaries in Python

d1 = dict() # (global) empty dictionary

def add_key_value_pair():
  d1["nome"] = "Lillo" # add a key-value pair
  print(d1)
  d1["eta"] = 19
  print(d1)

def get_value_using_key():
  print("Il nome e': " + d1["nome"]) # get a value using a key

def print_all_keys():
  print("All the keys in d1:"), # don't append \n
  print(d1.keys())

def print_all_values():
  print("All values in d1:"),
  print(d1.values())

def check_if_key_exists_in_dictionary():
  chiave = "nome"
  if (chiave in d1):
    print("La key 'nome' esiste in d1")

def check_if_value_exists_in_dictionary():
  valore = 19
  # nota: hai bisogno di fare diventare i values una list ?
  if (valore in list(d1.values())):
    print("Il valore " + str(valore) + " esiste in d1")

def occurrences_of_letters_in_string(the_string):
  resoconto = dict()
  for letter in the_string:
    if letter not in resoconto:
      resoconto[letter] = 1
    else:
      resoconto[letter] += 1

  print(resoconto)

def occurrences_of_letters_in_string_using_get(the_string):
  resoconto = dict()
  for letter in the_string:
  # get will return the value for the key 'letter' or 0 if the key does not exist in the 'resoconto' dictionary
    resoconto[letter] = resoconto.get(letter, 0) + 1

  print(resoconto)

import string

# Use this with romeo-full.txt
def count_words_in_file():
  fname = input("Insert input file name (in quotes if python2): ")
  try:
    fhand = open(fname)
  except:
    print("Invalid file name: " + str(fname))
    exit()
  
  word_occurrences = dict()

  for line in fhand:
    line = line.rstrip() # strips all white chars away from the end (r - right) of the string
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
      word_occurrences[word] = word_occurrences.get(word, 0) + 1

#  import pprint
#  pprint.pprint(word_occurrences)

  # print a chart with the 10 most recurring words
  word_chart = list()
  for k, v in list(word_occurrences.items()):
    word_chart.append((v, k))

  word_chart.sort(reverse=True)

  for v, k in word_chart[:10]:
    print(v, k)

  

def run_all():
#  add_key_value_pair()
#  get_value_using_key()
#  print_all_keys()
#  print_all_values()
#  check_if_key_exists_in_dictionary()
#  check_if_value_exists_in_dictionary()
#  occurrences_of_letters_in_string("uaosuperss")
#  occurrences_of_letters_in_string_using_get("uaosuperss")
  count_words_in_file()

if __name__ == '__main__':
  run_all()
