def serializer(origin_instance):

    def cycling(instance):
        if isinstance(instance, (set, list)):
            m_list = []
            for item in instance:
                value = typping(item)
                m_list.append(value)
            return m_list
        if isinstance(instance, dict):
            m_dict = {}
            for item in instance:
                value = typping(instance[item])
                m_dict.update({item: value})
            return m_dict

    def typping(instance):

        if isinstance(instance, set):
            return cycling(instance)
        elif isinstance(instance, list):
            return cycling(instance)
        elif isinstance(instance, dict):
            return cycling(instance)
        elif isinstance(instance, (float, int, basestring, bool)):
            return instance
        else:
            return typping(mapping(instance))

    def mapping(instance):
        return attr_dict(instance)

    def attr_dict(instance):

        full = dict([[e, getattr(instance, e)] for e in dir(instance) if '__' not in e and not hasattr(
            getattr(instance, e), '__call__')])
        proper = dict([[p, getattr(instance, e).__get__(instance, type(instance))]
                       for p in full if hasattr(full[p], 'fset')])
        full.update(proper)
        return full
    return typping(origin_instance)
