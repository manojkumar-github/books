def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func

def decoarated_by_syntax_no_method_signature(func):
    func.__doc__ += '\nDecoarated by syntax and no method signature'
    return func

def add(x,y):
    "Returns sum of two variables"
    return x + y
add = decorated_by(add)

@decoarated_by_syntax_no_method_signature
def subtract(x, y):
    "Returns differences of two variables"
    return x - y
help(add)
help(subtract)