import sys
from time import sleep

# Reference: https://stackoverflow.com/questions/20302331/typing-effect-in-python (Accessed: 24/10/17)
for char in words:
    sleep(0.00001)
    sys.stdout.write(char)
    sys.stdout.flush()
# End of Referenced material