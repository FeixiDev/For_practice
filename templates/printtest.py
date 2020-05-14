 # -*- coding: UTF-8 -*- 
import unittest
import io
import sys
def stub_stdin(inst, inputs):
	stdin = sys.stdin
	def cleanup():
		sys.stdin = stdin
    #清理函数
	inst.addCleanup(cleanup)
	# 开辟可操作空间
	sys.stdin = io.BytesIO(inputs)


# def stub_stdout():
# 	# stdout = sys.stdout

# 	# def cleanup():
# 	# 	sys.stdout = stdout

# 	# inst.addCleanup(cleanup)
# 	sys.stdout = io.BytesIO()


def fun():
	print('5')
	# print("out")


class UnitTest(unittest.TestCase):
	def test_fun(self):
		sys.stdout = io.StringIO()
		fun()
		self.assertEqual(str(sys.stdout.getvalue()), '5\n')
		# print(sys.stdout.getvalue())
		# stub_stdout(self) 
		# fun()
		# self.assertEqual(str(sys.stdout.getvalue()), '9\n')


if __name__ == '__main__':
	unittest.main(verbosity=2)
