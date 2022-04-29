import collections

my_counter = collections.Counter()

def log_and_count(**dec_kwargs):
    def decorator(func):

        def wrapper(*args,**kwargs):

            print(f"called {func.__name__} with {args} and {kwargs}")

            counter = dec_kwargs['counts']

            key = dec_kwargs['key'] if 'key' in dec_kwargs.keys() else func.__name__
              
            try:
                counter[key] += 1
            except KeyError:
                counter[key] = 1

            return func(*args,**kwargs)
        
        return wrapper
    return decorator

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)

print(my_counter)


