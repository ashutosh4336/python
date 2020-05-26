"""
LEGB
Local, Enclosing, Global, Built-in
"""
# Global and Local Scope
import builtins
x = 'global X'


def test(z):
    global x
    x = f'local X {z}'
    # print(y)
    print(x)

# test('Z')
# print(x)
# Built-in Scope


# print(dir(builtins))
# m = min([5, 4, 8, 26, 3])
# print(m)

# Enclosing
def outer():
    x = 'Outer X'

    def inner():
        nonlocal x
        x = 'inner X'
        print(x)
    inner()
    print(x)


outer()
print(x)
