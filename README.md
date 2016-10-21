# PythonSerializer
Python object serializer

python 对象序列化器 

~~~py
from serializer import serializer
class obj2():
	name = 'hi'
	my_list = ['this', 'is', 'python']
	m_attr = 'serializer'
class obj1():
	name = "I'm"
	my_list = ['object',obj2()]
	m_attr = {'I','can','mapping','the','object','to','dict',obj2()}

print serializer(obj1())
~~~

~~~python
//the print
{
	'my_list': [
        'object', 
        {
            'my_list': [
                'this',
                'is',
                'python'
            ],
            'name': 'hi',
            'm_attr': 'serializer'
        }
    ],
    'name': "I'm",
    'm_attr': [
        {
            'my_list': [
                'this',
                'is',
                'python'
            ],
            'name': 'hi',
            'm_attr': 'serializer'
        },
        'I',
        'object',
        'mapping',
        'to',
        'dict',
        'can',
        'the'
    ]
}
~~~

