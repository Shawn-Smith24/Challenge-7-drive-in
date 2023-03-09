class DriveIn:
    def __init__(self,name):
        self.name = name
        # self.screen = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise Exception("Name should be a string of 1 or more character!")

    def whats_playing():
        pass

    def full_house():
        pass
    

