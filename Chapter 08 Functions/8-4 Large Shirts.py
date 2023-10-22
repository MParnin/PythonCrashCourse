def make_shirt(text='i love python', size='large'):
    print(f"The size is {size} and the text is {text}")


make_shirt()
make_shirt(size='medium')
make_shirt('i love you', 'small')

##########################################################################
# Answer:

# def make_shirt(size='large', message='I love Python!'):
#     """Summarize the shirt that's going to be made."""
#     print(f"\nI'm going to make a {size} t-shirt.")
#     print(f'It will say, "{message}"')

# make_shirt()
# make_shirt(size='medium')
# make_shirt('small', 'Programmers are loopy.')
