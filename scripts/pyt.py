import sys
import subprocess


def py_test():
    subprocess.run(
        ['python', '-u', '-m', 'pytest'] + sys.argv[1:]
    )
