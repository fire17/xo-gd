#extras.py

# https://stackoverflow.com/questions/11291242/python-dynamically-create-function-at-runtime

# If you need to dynamically create a function from a certain template try this piece:

def create_a_function(*args, **kwargs):

    def function_template(*args, **kwargs):
        pass

    return function_template

my_new_function = create_a_function()
# Within function create_a_function() you can control, which template to chose. The inner function function_template serves as template. The return value of the creator function is a function. After assignment you use my_new_function as a regular function.

# Typically, this pattern is used for function decorators, but might by handy here, too.
