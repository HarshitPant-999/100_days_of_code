class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticate_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticate_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")

new_user = User("HARSHIT")
create_blog_post(new_user)
