# Alters are changes to the properties of a character.  They can
# be either permanent or temporary, and be either positive or negative
class Alter:
    def __init__(self, permanent, duration, positive):
        self.permanent = permanent
        self.duration = duration
        self.positive = positive

    # Ticks down the duration of each alter, returns duration
    def tick_down(self):
        if (self.permanent == False):
            self.duration -= 1
        print("inside tick down of alter")
        return self.duration

# Speed alter, found on Boots of Speed or speed boosts
class Speed(Alter):
    pass
