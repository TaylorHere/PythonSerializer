# PythonSerializer
Python object serializer

东半球最好用的 python 对象序列化器 

~~~python
from serializer import serializer


class obj2():
    name = 'hi'
    my_list = ['this', 'is', 'python']
    m_attr = 'serializer'

    def hi():
        pass

    def __init__(self):
        self.__x = 'hi'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x


class obj1():
    name = "I'm"
    my_list = ['object', obj2()]
    m_attr = {'I', 'can', 'mapping', 'the', 'object', 'to', 'dict', obj2()}

print serializer(obj1())

~~~

~~~python
//the output
{
    'my_list': [
        'object',
        {
            'x': 'hi',
            'my_list':
            [
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
        'I',
        'object',
        'mapping',
        {
            'x': 'hi',
            'my_list': [
                'this',
                'is',
                'python'
            ],
            'name': 'hi',
            'm_attr': 'serializer'
        },
        'to',
        'dict',
        'can',
        'the'
    ]
}
~~~

发送至锤子手机
