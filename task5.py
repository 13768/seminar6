def find(word, letter, wheretostart):
  index = 0
  while index < len(word[wheretostart:]):
    if word[index] == letter:
      return index
    index = index + 1
  return -1 

print(find("computer", "p", 2))
