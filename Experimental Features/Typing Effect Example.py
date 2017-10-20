import sys
from time import sleep

words = """
you should use sys.stdout.flush() after each iteration

The problem is that stdout is flushed with the newline or manually with sys.stdout.flush()

So the result is

import sys
from time import sleep

words = "This is just a test :P"
for char in words:
    sleep(0.5)
    sys.stdout.write(char)
    sys.stdout.flush()
The reason why your output is buffered is that system call needs to be performed in order to do an output, system calls are expensive and time consuming (because of the context switch, etc). Therefore user space libraries try to buffer it and you need to flush it manually if needed.

Just for the sake of completeness ... Error output is usually non-buffered (it would be difficult for debugging). So following would also work. It is just important to realise that it is printed to the error output.

import sys
from time import sleep

words = "This is just a test :P"
for char in words:
    sleep(0.5)
    sys.stderr.write(char)

	"""
for char in words:
    sleep(0.00001)
    sys.stdout.write(char)
    sys.stdout.flush()