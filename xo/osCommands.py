import sys, subprocess, shlex

class Popen2(subprocess.Popen):
    "Context manager for Python2"
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        if self.stdout:
            self.stdout.close()
        if self.stderr:
            self.stderr.close()
        if self.stdin:
            self.stdin.close()
        # Wait for the process to terminate, to avoid zombies.
        self.wait()


def os_command(command, print_output=True, shell=False):
    """
    Run an OS command (utility function) and returns a generator
    with each line of the stdout.

    In case of error, the sterr is forwarded through the exception.

    For the arguments, see run_os_command.
    If you are not sur between os_command and run_os_command,
    then the second is likely for you.
    """
    ENCODING = 'UTF-8'
    if isinstance(command, str):
        # if a string, split into a list:
        command = shlex.split(command)
    # we need a proper context manager for Python 2:
    if sys.version_info < (3,2):
        Popen = Popen2
    else:
        Popen = subprocess.Popen
    # Process:
    with Popen(command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=shell) as process:
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                # check error:
                process.poll()
                errno = process.returncode
                if errno:
                    # get the error message:
                    stderr_msg = str(process.stderr.read(), ENCODING)
                    errmsg = "Call of '%s' failed with error %s\n%s" % \
                                            (command, errno, stderr_msg)
                    raise OSError(errno, errmsg)
                break
            # Python 3: converto to unicode:
            if sys.version_info > (3,0):
                line = str(line, ENCODING)
            if print_output:
                print(line)
            yield line

def run_os_command(command, print_output=True, shell=False):
    """
    Execute a command, printing as you go (unless you want to suppress it)

    Arguments:
    ----------
        command: eithr a string, a list containing each element of the command
            e.g. ['ls', '-l']
        print_output: print the results as the command executes
            (default: True)
        shell: call the shell; this activates globbing, etc.
            (default: False, as this is safer)

    Returns:
    --------
        A string containing the stdout
    """
    r = list(os_command(command, print_output=print_output, shell=shell))
    return "\n".join(r)


def os_get(command, shell=False):
    """
    Execute a command as a function

    Arguments:
    ----------
        command: a list containing each element of the command
            e.g. ['ls', '-l']
        shell: call the shell; this activates globbing, etc.
            (default: False)

    Returns:
    --------
        A string containing the output
    """
    return run_os_command(command, print_output=False, shell=shell)
