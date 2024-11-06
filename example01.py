MARGIN = 10
SYMBOL = "*"

height = 12

for num_spaces in range(height-1, -1, -1):
    print(" " * MARGIN, " " * num_spaces, end="")
    num_symbols = (height - num_spaces) * 2 - 1
    print(SYMBOL * num_symbols)
