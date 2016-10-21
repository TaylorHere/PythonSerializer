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
