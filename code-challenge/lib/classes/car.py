class Car:
    def __init__(self,passenger_count):
        self.passenger_count = passenger_count

        # self.current_movie_screen(movie_screen=None)

    @property
    def passenger_count(self):
        return self._passenger_count
    
    @passenger_count.setter
    def passenger_count(self, passenger_count):
        if type(passenger_count) == int and 0 < passenger_count < 8:
            self._passenger_count = passenger_count
        else:
            raise Exception("Passenger count should be an integer between 1 and 8!")
    
  
    # def current_movie_screen(self, movie_screen=None):
    #     return movie_screen == self._current_movie_screen
    # # def set_current_movie_screen(self, movie_screen):
        
    #     if isinstance(movie_screen, MovieScreen):
    


   
    
  