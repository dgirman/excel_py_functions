#py_functions.py


from pyxll import xl_func


@xl_func
def py_test_func_01(a, b, c):
	return f"a = {a}; b = {b} ; c = {c}"


def py_test_func_02(a, b, c):
	return a + b + c

@xl_func
def py_test_func(a,b, c):
	return [str(type(a)), str(type(b)), str(type(c))]


def test():
	"""
	:return:
	"""
	rtn = py_test_func(a=1,b=2)
	print(rtn)

if __name__ == "__main__":
    test()