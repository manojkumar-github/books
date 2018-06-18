"""
Sending values to generator using "send" method - allows communication back to generator
"""

def squares():
    cursor = 1
    while True:
        yield cursor ** 2
        cursor += 1

sq_obj = squares()
print next(sq_obj)
print next(sq_obj)

def squares_with_send(cursor = 1):
    while True:
        response = yield cursor ** 2
        if response:
            cursor = int(response)
        else:
            cursor += 1

sq_send_obj = squares_with_send()
print next(sq_send_obj) # prints 1
print next(sq_send_obj) # prints 4
print sq_send_obj.send(7) # prints 49
print next(sq_send_obj) # prints 64

def squares_one_off(cursor =1):
    """
    this generator uses sent cursor value as one-off and then return to its
    previous spot
    :param cursor:
    :return:
    """
    response = None
    while True:
        if response:
            response = yield cursor ** 2
            continue
        response = yield  cursor ** 2
        cursor += 1

sq_one_off_obj = squares_one_off()
print next(sq_one_off_obj) # prints 1
print next (sq_one_off_obj) # prints 4
print sq_one_off_obj.send(7) # prints 49
print next(sq_one_off_obj) # prints 64

"""
The purpose of send is to provide a mechanism for two-way communication with a generator
It is the resposbility of the generator to determine whether(and how) it handles values sent to it.
"""
