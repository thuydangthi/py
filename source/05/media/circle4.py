class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    radius = property(
        fget=_get_radius,
        doc="The radius property."
    )
