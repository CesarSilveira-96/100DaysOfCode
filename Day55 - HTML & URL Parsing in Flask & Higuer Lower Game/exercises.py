# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        results = function(*args)
        print(f"You called {function.__name__}{args}\n"
              f"it returned {results}")
        return results
    return wrapper

# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)