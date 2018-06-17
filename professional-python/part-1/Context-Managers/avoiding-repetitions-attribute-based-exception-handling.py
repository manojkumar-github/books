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

#run_command('rm bogusfile')
"""
The above command will raise below exception
Traceback (most recent call last):
  File "file path/filename.py", line 27, in <module>
    run_command('rm bogusfile')
  File "filepath/filename.py", line 22, in run_command
    raise ShellException(proc.returncode, stdout, stderr)
__main__.ShellException: exit code 1 - rm: bogusfile: No such file or directory
"""
"""
Handling generic Shell Exception is easy
Imagine a situation where you receive a ShellException but only want to
handle a particular exit code --> can be achieved using context-manager
"""
"""
Consider a scenario where a file has to be removed which is already removed beforehead (ignoring os.remove)
We are fine with return code 0 - which indicates successful removal of file if present
We are also fine with return code 1 - which indicates the file was already absent
However, an exit code of 64 is not acceptable, as it would indicate an usage error of some kind
"""

class AcceptableErrorCodes(object):
    def __init__(self, *error_codes):
        self.error_codes = error_codes
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Sanity check: If this is not an exceptional situation, then just be done
        if not exc_type:
            return True

        # Sanity check: If this is anything other than a ShellException
        # then we do not actually know what to do with it
        if not issubclass(exc_type, ShellException):
            return False
        # Return True if and only if the ShellException has a code that
        # matches one of the codes on our error_codes list
        return exc_val.code in self.error_codes

with AcceptableErrorCodes(1):
    # trying to remove non-existent file
    run_command('rm bogusfile')

with AcceptableErrorCodes(1):
    # -m is not a switch available to rm (at least in Mac OS X)
    # this will raise an exception with exit code 64 on Mac OS X
    run_command('rm -m bogusfile')

with AcceptableErrorCodes(64):
    # this will not raise a traceback as now 64 is handled
    # __exit__ method returned False
    run_command('rm -m bogusfile')


