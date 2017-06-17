import sys
sys.path.append("../helloworld/")

from hello_world import hello, sum, TODAY
#from hello_world import *
import time

def app():
    print("This is my app")
    hello()
    print(sum("Over","Watch"))

app()
print(TODAY)
print(time.clock())
