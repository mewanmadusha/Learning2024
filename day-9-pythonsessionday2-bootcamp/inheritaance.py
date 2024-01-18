class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)
# The output of the code above is shown below:
# → Documents python rockets.py
# simple rocket has reached till stratosphere mars_rover has reached till Mars mars_rover Launched by ISRO


class MarsRover(Rocket): # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker
    def get_maker(self) :
        return "%s Launched by %s" % (self.name, self.maker)

if __name__ == "__main__":
    x = Rocket ("simple rocket", "till stratosphere")
    y = MarsRover ("mars_rover", "till Mars", "ISRO")
    print (x. launch())
    print (y. launch())
    print (y.get_maker())