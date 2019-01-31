from time import time
def timer(func):
    def f(*args, **kwargs):
        before=time()
        rv=func(*args,**kwargs)
        
