class Wing(object):

    span = 10.0
    chord_root = 2.0
    chord_tip = 3.0

    def get_taper_ratio(self):
        print(r"Calculating Taper Ratio")
        return self.chord_root/self.chord_tip

    def get_aspect_ratio(self):
        print(r"Calculating Aspect Ratio")
        return self.span**2/self.area

    @property
    def area(self):
        return (self.chord_root + self.chord_tip)*0.5*self.span


wing = Wing()

print(wing.get_taper_ratio())
print(wing.get_aspect_ratio())
print(wing.area)
wing.span = 20
print(wing.area)
