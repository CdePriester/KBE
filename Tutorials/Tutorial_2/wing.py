from parapy.core import *


class Wing(Base):
    span = Input(10.0)
    chord_root = Input(2.0)
    chord_tip = Input(3.0)

    @Attribute
    def taper_ratio(self):
        print(r"Calculating Taper Ratio")
        return self.chord_root/self.chord_tip

    @Attribute
    def aspect_ratio(self):
        print(r"Calculating Aspect Ratio")
        return self.span**2/self.area

    @Attribute
    def area(self):
        return (self.chord_root + self.chord_tip)*0.5*self.span


if __name__ == '__main__':
    from parapy.gui import display

    obj = Wing()
    display(obj)
