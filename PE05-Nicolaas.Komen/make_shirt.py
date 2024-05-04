#defining function called 'make_shirt'
def make_shirt(size = 'large', message = 'I love Python!'):
    """Summarize the shirt thats going to be made"""
    print(f"\nI'm going to make a {size} shirt.")
    print(f"It will say, ""{message}")

make_shirt()
make_shirt(size = 'medium')
make_shirt(message = "I love my children", size = 'x-large')
make_shirt('x-large', 'I love my children!')
    