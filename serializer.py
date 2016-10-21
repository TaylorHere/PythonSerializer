def serializer(origin_class):

    def cycling(obj):
        if isinstance(obj, (set, list)):
            m_list = []
            for item in obj:
                value = typping(item)
                m_list.append(value)
            return m_list
        if isinstance(obj, dict):
            m_dict = {}
            for item in obj:
                value = typping(obj[item])
                m_dict.update({item: value})
            return m_dict

    def typping(obj):

        if isinstance(obj, set):
            return cycling(obj)
        elif isinstance(obj, list):
            return cycling(obj)
        elif isinstance(obj, dict):
            return cycling(obj)
        elif isinstance(obj, (float, int, basestring, bool)):
            return obj
        else:
            return typping(mapping(obj))

    def mapping(obj):
        return attr_dict(obj)

    def attr_dict(obj):
        full = dict([[e, obj.__dict__[e]]
             for e in obj.__dict__ if '__' not in e and not hasattr(obj.__dict__[e], '__call__')])
        proper = dict([[p, obj.__dict__[p].__get__(obj, type(obj))]
               for p in full if hasattr(full[p], 'fset')])
        full.update(proper)
        return full
    return typping(origin_class)
