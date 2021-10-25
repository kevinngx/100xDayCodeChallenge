class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def requires_authentication(function):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user.is_logged_in == True:
            function()
        else:
            print("User is not logged in")
    return wrapper

@requires_authentication
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("Kevin")
create_blog_post(new_user)


