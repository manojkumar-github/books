'''Program 1'''
import functools
import json

def json_output(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        """
        download the value returned by decorated function as json output
        :param args:
        :param kwargs:
        :return:
        """
        result = decorated(*args, **kwargs)
        return json.dumps(result)
    return inner

@json_output
def do_nothing():
    return {'status': 'pass'}

# when printed in python console, it outputs a sting of dict instead of dict
print do_nothing()

'''Program 2'''

import functools
import json

class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return self._message

def json_output_exception_handling(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        try:
            result = decorated(*args, **kwargs)
        except JSONOutputError as e:
            result = {'status': 'error', 'message': str(e)}
        return json.dumps(result)
    return inner

@json_output_exception_handling
def error_function():
    raise JSONOutputError('This is a erratic function')

@json_output_exception_handling
def other_function():
    raise ValueError('This function is not trapped in JSON output and will result in traceback instead')