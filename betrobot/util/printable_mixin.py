class PrintableMixin:

    def __str__(self):
        init_strs = []
        runtime_strs = []
        descriptions = []

        for class_ in self.__class__.__mro__:
            if '_get_init_strs' in class_.__dict__:
                init_strs += class_._get_init_strs(self)
            if '_get_runtime_strs' in class_.__dict__:
                runtime_strs += class_._get_runtime_strs(self)
            if '_get_description' in class_.__dict__:
                description_ = class_._get_description(self)
                if description_ is not None:
                    self.descriptions.append(description_)

        init_str = ', '.join(init_strs)
        runtime_str = ', '.join(runtime_strs) if len(runtime_strs) > 0 else None
        description_str = '; '.join(descriptions) if len(descriptions) > 0 else None

        result = ''
        result += '%s(%s)' % (self._get_printable_mixin_name(), init_str)
        if runtime_str is not None:
            result += '[%s]' % (runtime_str,)
        if description_str is not None:
            result += '{%s}' % (description_str,)

        return result


    def _get_printable_mixin_name(self):
        return self.__class__.__name__


    def _get_init_strs(self):
        return []


    def _get_runtime_strs(self):
        return []


    def _get_description(self):
        return None
