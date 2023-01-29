words = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
MISTAKES_LIMIT = 5
MASK_SYMBOL = "*"

hidden_word = words.pop()
print(hidden_word)

word_mask = [MASK_SYMBOL for _ in range(len(hidden_word))]
mistakes = 0
stars_count = 0

while mistakes < MISTAKES_LIMIT:
    print("> The word: ", "".join(word_mask))
    print(">")
    print("> Guess a letter: ")

    input_letter = input("< ")

    stars_count = word_mask.count(MASK_SYMBOL)
    for index, letter in enumerate(hidden_word):
        if input_letter == letter:
            word_mask[index] = letter

    if word_mask.count(MASK_SYMBOL) == stars_count:
        mistakes += 1
        print("> Missed, mistake", mistakes, "out of 5.")
        print(">")
    elif word_mask.count(MASK_SYMBOL) == 0:
        print("> The word: ", "".join(word_mask))
        print(">")
        print("> You won!")
        break
    else:
        print("> Hit!")
        print(">")

if mistakes == 5:
    print("> The word: ", "".join(word_mask))
    print(">")
    print("> You lost!")
