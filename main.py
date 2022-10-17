test = int(input("Please enter a number:"))


def test_is_valid(test):
  return isinstance(test, int) and (1 <= test <= 3)


print(f"Result: {test_is_valid(test)}")