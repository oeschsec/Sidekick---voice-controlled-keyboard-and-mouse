

class B:
    def __init__(self,foo):
        self.foo = foo 
        print(id(self.foo))

    def add(self,foo):
        foo += 3
        print(foo)
        print(id(self.foo))

class A:
    foo = 3
    print(id(foo))

a = A()
b = B(a.foo)
b.add(a.foo)
print(b.foo)
print(a.foo)