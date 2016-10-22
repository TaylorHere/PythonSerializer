def serializer(origin_instance, class_type='basic'):
    # class_type choice 'sqlalchemy', 'basic'
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
        elif instance is None:
            return None
        else:
            return typping(mapping(instance))

    def mapping(instance):
        if class_type == 'basic':
            return attr_dict_from_basic(instance)
        elif class_type == 'sqlalchemy':
            return attr_dict_from_sqlalchemy(instance)

    def attr_dict_from_basic(instance):
        # find out the members of the instance except function
        full = dict([[e, instance.__getattribute__(e)] for e in dir(instance) if not e.startswith('_') and not hasattr(
            instance.__getattribute__(e), '__call__')])
        # find out all the properties in the instance then get there's vaule
        proper = dict([[p, getattr(instance, e).__get__(instance, type(instance))]
                       for p in full if hasattr(full[p], 'fset')])
        # replace property's value into real value of the property
        full.update(proper)
        return full

    def attr_dict_from_sqlalchemy(instance):

        full = dict([[e, instance.__getattribute__(e)]
                     for e in instance.__mapper__.c.keys()])
        return full
    return typping(origin_instance)
