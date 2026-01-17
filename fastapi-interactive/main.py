def example():
    print("before")
    yield "hello"
    print("after")

gen = example()
next(gen)   # prints "before", returns "hello"
next(gen)   # prints "after", StopIteration