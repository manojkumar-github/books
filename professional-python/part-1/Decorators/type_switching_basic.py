class Task(object):
    """
    A trivial task class. Task classes have a 'run' method which runs the task
    """
    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement "run" method')
    def identify(self):
        return 'I am a task'

def task(decorated):
    """
    Return a class that runs the given function if its run method is called
    """
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass


@task
def foo():
    return 2 + 3

f = foo()
print f
print f.run()
print f.identify()