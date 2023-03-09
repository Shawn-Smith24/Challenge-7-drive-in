class MovieScreen:
    def __init__(self, movie_title, capacity, drive_in):
        self.movie_title = movie_title
        self.capacity = capacity
        self.drive_in = drive_in

        self.cars = []

    @property
    def movie_title(self):
        return self._movie_title
    
    @movie_title.setter
    def movie_title(self, movie_title):
        if type(movie_title) == str and len(movie_title) > 0:
            self._movie_title = movie_title
        else:
            raise Exception("Movie title should be a string greater than 0 characters!")
        

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) == int and capacity > 0:
            self._capacity = capacity
        else:
            raise Exception("Capacity should be an integer greater than 0!")
    
    

    # def number_of_viewer():
    #     pass

    # def at_capacity():
    #     pass

    # def available_spots():
    #     pass

    # def add_car(car):
    #     pass

    # def remove_car(car):
    # @property
    # def drive_in(self):
    #     return self._drive_in
    
    # @drive_in.setter
    # def drive_in(self, drive_in):
    #     from drive_in import DriveIn
    #     if isinstance(drive_in, DriveIn):
    #         self._drive_in = drive_in

    #         MovieScreen._drive_in.append(self)
    #     else:
    #         raise Exception("Must be an instance of drivin class!")