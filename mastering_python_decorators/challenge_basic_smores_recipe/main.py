def chocolate(func):
    def wrapper(*args, **kwargs):
        # print("               1=chocolate=1")
        func(*args, **kwargs)
        print("               =chocolate=")
    return wrapper

def crackers(func):
    def wrapper(*args, **kwargs):
        print("               ~~cracker~~")
        func(*args, **kwargs)
        print("               ~~cracker~~")
    return wrapper

@crackers
@chocolate
def basic_smores():
    print("-roasted-------marshmallow-")

# Test the recipe
basic_smores()