"""
The primary reason to write a class factory is when it is necessary to create a class based on the execution-time
knowledge such as user input. The "class" keyword assumes that you know the attributes you wish to assign to the class at coding time
If you do not know the attributes to be assigned to the class at coding time, a class factory function can be convenient alternative
"""
"""
Consider following function that creates a class, but this time, the attributes of that class can vary based on parameters
sent to the function
"""

def get_credential_class(use_proxy = False, tfa = False):
    """
    Return a class representing a credential for the given service with an attribute representing the expected keys.
    :param use_proxy: keyword boolean value
    :param tfa: keyword boolean value
    :return:
    """
    # If a proxy, such as facebook connect, is being used, we just
    # need the service name and the email-address
    if use_proxy:
        keys={'service_name', 'email_address'}
    else:
        # For the purpose of this example, all other services use
        # username and password

        keys = {'username', 'password'}
        # If two-factor auth is in play, then we need an authenticatior token also
        if tfa:
            keys.append('tfa_token')

    # Return a class with a proper __init__ method which expects all expected keys

    class Credential(object):
        expected_keys = set(keys)

        def __init__(self, **kwargs):
            # Sanity check : Do our keys match
            if self.expected_keys != set(kwargs.keys()):
                raise ValueError('Keys do not match.')

            # write the keys to the credential object
            for k, v in kwargs.items():
                setattr(self, k, v)

    return Credential

