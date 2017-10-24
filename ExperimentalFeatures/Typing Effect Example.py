import sys
from time import sleep

words = """

	"""
for char in words:
    sleep(0.00001)
    sys.stdout.write(char)
    sys.stdout.flush()

    #https://stackoverflow.com/questions/20302331/typing-effect-in-python