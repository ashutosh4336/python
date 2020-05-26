"""
LEGB
Local, Enclosing, Global, Built-in
"""
# Global and Local Scope
# x = 'global X'
import builtins


def test(z):
    global x
    x = f'local X {z}'
    # print(y)
    print(x)

# test('Z')
# print(x)
# Built-in Scope


print(dir(builtins))
m = min([5, 4, 8, 26, 3])
print(m)
