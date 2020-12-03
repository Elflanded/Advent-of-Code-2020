valid_passwords = 0

with open('input.py', 'r') as f:
    for line in f:
      min_max, letter_colon, password = line.split()
      pmin, pmax = [int(c) for c in min_max.split('-')]
      letter = letter_colon[0:1]

      num_letters = password.count(letter)
      if pmin <= num_letters and num_letters <= pmax:
        valid_passwords += 1

print(valid_passwords)
