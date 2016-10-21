# PythonSerializer
Python object serializer

python 对象序列化器 

~~~py
from serializer import serializer
class obj1():
	name = 'hi'
	my_list = ['this', 'is', 'python']
	m_attr = 'serializer'
class obj2():
	name = "I'm"
	my_list = ['object']
	m_attr = {'I','can','mapping','the','object','to','dict'}

print serializer(obj1())
~~~

