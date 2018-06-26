from django import forms

class CredentialForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


"""
If you do not what your fields are, a class factory becomes the perfect approach
"""

import csv
from django import forms

def get_credentail_form_classes(service):
    """
    Return a class representing a credential for a given service with attributes representing the expected keys
    :param service:
    :return:
    """
    # Open our database
    keys = []
    with open('creds.csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            # If this row does not correspond to the service we are looking for, skip this
            if row[0].lower() != service.lower():
                continue
            # Add the key to the list of expected keys
            keys.append(row[1])
    # Put together the appropriate credential fields
    attrs ={}
    for key in keys:
        field_kw = {}
        if 'password' in key:
            field_kw['widget'] = forms.PasswordInput
        attrs[key] = forms.CharField(**field_kw)

    # Return a form class with the appropriate credential fields
    metaclass = type(forms.Form)
    return metaclass('CredentialForm', (forms.Form), attrs)