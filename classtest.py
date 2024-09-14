import time

def func():
    print("abc")

class abc():
    def __init__(self,a):
        self.function = a
    def runfunc(self):
        self.function()

s = abc(func)
time.sleep(5)
s.runfunc()
print('132')