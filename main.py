from importlib import import_module


if __name__ == '__main__':
    try:
        import_module('parser', 'this')
    except SyntaxError:
        print("new parser")
