import functools
import logging
import time
logging.basicConfig()

def logged(decorated):
    """Cause the decorated method to be run and its results logged, along with some other diagnostic
       information"""
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        # record the start time
        start = time.time()
        # run the decoated method
        return_value = decorated(*args, **kwargs)
        # record our completion time and calculate the delta
        end = time.time()
        delta = start - end

        # log the method call and result
        logger = logging.getLogger('decorated.logged')
        logger.warn('Called method %s at %.02f; execution time %.02f'
                    'seconds; result %r.' % (decorated.__name__, start, delta, return_value))
        # return the decorated function original value
        return return_value
    return inner

@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value

print sleep_and_return(42)
