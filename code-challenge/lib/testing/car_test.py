import pytest

from classes.car import Car
from classes.drive_in import DriveIn
from classes.movie_screen import MovieScreen

class TestCar:
    '''Car in car.py'''

    def test_has_passenger_count(self):
        '''has the passenger count passed into __init__().'''
        Car(passenger_count=5)

    def test_passenger_count_between_1_and_8(self):
        '''forces passenger_count to be between 1 and 8, inclusive.'''
        with pytest.raises(Exception):
            Car(passenger_count=0)
        with pytest.raises(Exception):
            Car(passenger_count=9)
        
    def test_sets_movie_screen(self):
        '''sets instance attribute movie_screen with method current_movie_screen().'''
        c = Car(passenger_count=5)
        di = DriveIn(name="Galaxy Drive In-n-Out Theatre")
        ms = MovieScreen(movie_title="Gigli", capacity=32, drive_in=di)
        c.current_movie_screen(ms)
        assert c.movie_screen == ms

    
