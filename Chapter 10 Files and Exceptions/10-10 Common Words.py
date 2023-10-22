def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File not found.")
    else:
        words = contents.lower().count("the ")
        print(f"The file {filename} has about {words} words.")


filenames = ['alice.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


##############################################################################
# Answer:

# def count_common_words(filename, word):
#     """Count how many times word appears in the text."""
#     # Note: This is a really simple approximation, and the number returned
#     #   will be higher than the actual count.
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         word_count = contents.lower().count(word)

#         msg = f"'{word}' appears in {filename} about {word_count} times."
#         print(msg)

# filename = 'alice.txt'
# count_common_words(filename, 'the')
