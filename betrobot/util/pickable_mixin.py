class PickableMixin(object):

    def __getstate__(self):
        self._on_pickle()

        pick_names = set()
        for class_ in self.__class__.__mro__:
            class_pick_names = getattr(class_, '_pick', [])
            pick_names.update(class_pick_names)

        state = { pick_name: getattr(self, pick_name) for pick_name in pick_names }

        return state


    def __setstate__(self, state):
        for name, value in state.items():
            setattr(self, name, value)

        self._on_unpickle()


    def _on_pickle(self):
        pass


    def _on_unpickle(self):
        pass
