import csv

def get_credential_class(service):
    """
    Return a class representing a credential for the given service, with an attribute
    representing the expected keys
    :param service:
    :return:
    """
    # Open your database
    keys =[]
    with open('creds,csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            # If this row does not correspond to the service we are actually asking for , skip it.
            if row[0].lower() != service.lower():
                continue
            # Add the key to the list of expected keys
            keys.append(row[1])

    # Return a class with a proper __init__ method which expects all expected keys

    class Credential(object):
        expected_keys = keys
        def __init__(self, **kwargs):
            # Sanity check; Do our keys match
            if set(self.expected_keys) != set(i for i in kwargs.keys()):
                raise ValueError('Keys do not match')

            # Write the keys to the credential object
            for k, v in kwargs.items():
                setattr(self, k, v)
    return Credential


