def serializer(origin_class):

    return typping(origin_class)

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
        elif isinstance(obj, (float, int, basestring)):
            return obj
        else:
            return typping(mapping(obj))

    def mapping(obj):
        return attr_dict(obj)

    def attr_dict(obj):
        return dict([[a, getattr(obj, a)] for a in dir(obj) if '__' not in a])
