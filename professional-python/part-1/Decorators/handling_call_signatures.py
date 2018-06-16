import functools
import json

class JSONOutpuError(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return self._message

def json_output(is_decorated = False, indent = None, sort_keys = False):
    """
    Run the decorated function, serialize the result of that function to JSON
    and return JSON string
    """
    # Raise Error if we get both decorated function and arguments
    if is_decorated and (indent or sort_keys):
        raise RuntimeError('Unexpected arguments')

    # Define the actual decorator function
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except JSONOutpuError as e:
                result = {'status':'fail', 'message': str(e)}
            return json.dumps(result, indent = indent, sort_keys = sort_keys)
        return inner
    # Return either the actual decorator or the result of applying
    if is_decorated:
        return actual_decorator(is_decorated)
    else:
        return actual_decorator

@json_output(indent=4)
def do_nothing():
    return  {'status': 'done'}

@json_output()
def do_something():
    return  {'status': 'done'}

@json_output
def do_NOT_error_without_call_signature():
    return {'status': 'done'}