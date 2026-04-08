#py_functions.py


from pyxll import xl_func

@xl_func
def py_test_func(a,b):
	return f"a = {a}; b = {b}"


def test():
	rtn = py_test_func(a=1,b=2)
	print(rtn)
if __name__ == "__main__":
    test()