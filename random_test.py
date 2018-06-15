def sep_line(separator, n):
  print(' ', end='')
  for i in range(n):
    print(separator, sep='', end='')
  print()

def sep_end(separator):
  sep_line(separator, 24)
  print()

def random_example(n):
# example using the random.random() function
  print(' * Example using random.random() *')
  print(' random() was called with:', n)
  sep_line('-', 24)
  import random
  for i in range(n):
    print(' call', i, ':', random.random())

def randint_example(low, high):
# example using the random.randint() function
  import random
  print(' * Example using random.randint() *')
  print(' randint() was called with min:', low, '; high:', high)
  sep_line('-', 24)
  print(' Result:', random.randint(low, high))

def choice_example(values):
# example using the random.choice() function
  import random
  print(' * Example using random.choice() *')
  print(' choice() was called with:', values)
  sep_line('-', 24)
  print(' Result:', random.choice(values))

def print_char_times(c, n):
  print(' ', end='')
  for i in range(n):
    print(c, end='')

def print_end_message():
  end_message = '* All functions executed with no errors. *'
  print_char_times('*', len(end_message))
  print('\n', end_message, '\n * END *')
  print(' *******')

if __name__ == '__main__':
  random_example(9)
  sep_end('')
  randint_example(6, 12)
  sep_end('')
  choice_example(['Koh Lanta', 'Koh Phangan', 'Krabi'])
  sep_end('')
  
  print_end_message()
