class User(object):
    """A representation of a user in our application"""
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AnonymousUser(User):
    """
    An anonymous user; a stand-in for an actual user that nonetheless is not an actual user
    """
    def __init__(self):
        self.username = None
        self.email = None
    def __nonzero__(self):
        return False

import functools

def requires_user(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        """
        Verify that the user is truthy; if so, run the decorated method
        and if not, raise ValueError
        """
        # Ensure that user is truthy, and of the correct type
        # The "truthy" check will fail on anonymous users, since the
        # AnonymousUser subclass has a '__nonzero__' method that returns False
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        elif user and isinstance(user, AnonymousUser):
            raise ValueError('This is an anonymous user')
        else:
            raise ValueError('A valid user is required to run this:')
    return inner

user = User('Manoj','dhoni')
anuser = AnonymousUser()

class Test(object):
    user = User('one', 'two')
    @requires_user
    def foo(user):
        "Validate the user authentication"
        print "User is valid"
        return

    @requires_user
    def bar(anuser):
        "Validate user authentication"
        print 'User is invalid'
        return

obj = Test()
obj.foo(user)
