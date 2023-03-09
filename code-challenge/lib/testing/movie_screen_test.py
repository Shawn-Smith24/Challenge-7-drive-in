import pytest

from classes.car import Car
from classes.drive_in import DriveIn
from classes.movie_screen import MovieScreen

class TestMovieScreen:
    '''MovieScreen in movie_screen.py'''

    def test_has_movie_title_capacity_drive_in(self):
        '''initializes with movie_title, capacity, and drive_in'''
        di = DriveIn(name="Name")
        MovieScreen(movie_title="Title", capacity=5, drive_in=di)

    def test_requires_movie_title_nonempty_string(self):
        '''requires "movie_title" to be a string of >0 characters.'''
        di = DriveIn(name="Name")
        with pytest.raises(Exception):
            MovieScreen(movie_title=1, capacity=5, drive_in=di)
        with pytest.raises(Exception):
            MovieScreen(movie_title='', capacity=5, drive_in=di)

    def test_requires_capacity_positive_int(self):
        '''requires "capacity" to be an integer above 0.'''
        di = DriveIn(name="Name")
        with pytest.raises(Exception):
            MovieScreen(movie_title="Title", capacity='1', drive_in=di)
        with pytest.raises(Exception):
            MovieScreen(movie_title="Title", capacity=0, drive_in=di)

    def test_drive_in_adds_self_to_drive_in_screens(self):
        '''"drive_in" setter appends self to DriveIn instance's screens.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=5, drive_in=di)
        assert ms in di.screens

    def test_shows_number_of_viewers(self):
        '''has method "number_of_viewers" that returns total of cars' passengers at the screen.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=50, drive_in=di)
        cars = [Car(passenger_count=2) for i in range(20)]
        ms.cars = cars
        assert ms.number_of_viewers() == 40

    def test_at_capacity(self):
        '''has method "at_capacity" that returns True if the screen has reached capacity and False if not.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=50, drive_in=di)
        cars = [Car(passenger_count=2) for i in range(20)]
        ms.cars = cars
        assert not ms.at_capacity()
        cars = [Car(passenger_count=2) for i in range(30)]
        ms.cars += cars
        assert ms.at_capacity

    def test_shows_available_spots(self):
        '''has method "available_spots" that returns the number of spots under capacity at the screen.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=50, drive_in=di)
        cars = [Car(passenger_count=2) for i in range(20)]
        ms.cars = cars
        assert ms.available_spots() == 30

    def test_adds_car(self):
        '''has a method "add_car" that adds a car if under capacity and returns "Sold Out!" if at capacity.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=50, drive_in=di)
        cars = [Car(passenger_count=2) for i in range(20)]
        ms.cars = cars
        new_car = Car(passenger_count=1)
        ms.add_car(new_car)
        assert new_car in ms.cars
        ms.cars += [Car(passenger_count=2) for i in range(29)]
        assert ms.add_car(Car(passenger_count=1)) == "Sold Out!"

    def test_removes_car(self):
        '''has a method "remove_car" that removes a car from the screen's cars.'''
        di = DriveIn(name="Name")
        ms = MovieScreen(movie_title="Title", capacity=50, drive_in=di)
        new_car = Car(passenger_count=1)
        ms.cars.append(new_car)
        ms.remove_car(new_car)
        assert new_car not in ms.cars
