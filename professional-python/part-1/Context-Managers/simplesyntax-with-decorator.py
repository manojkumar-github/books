import contextlib
import subprocess

class ShellException(Exception):
    def __init__(self, code, stdout = '', stderr=''):
        self.code = code
        self.stdout = stdout
        self.stdder = stderr
    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stdder)

def run_command(command):
    # Run the command and wait for it to complete
    proc = subprocess.Popen(command.split(' '), stdout = subprocess.PIPE,
                                                stderr=subprocess.PIPE)
    proc.wait()

    # Get the stdout and stderr from the shell
    stdout, stderr = proc.communicate()

    # Sanity check; if the shell returned a non-zero exit status, raise an exception
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout, stderr)

    # Return stdout
    return stdout

@contextlib.contextmanager
def acceptable_error_codes(*codes):
    try:
        yield # yield a single value
    except ShellException as exc_instance:
        # If this error code is not in the list of acceptable codes
        # re-raise the exception
        if exc_instance.code not in codes:
            raise

        # This was an acceptable error; not required to do anything
        pass

with acceptable_error_codes(1):
    run_command('rm bogusfile')

with acceptable_error_codes(1):
    # raises an exception
    run_command('rm -m bogusfile')