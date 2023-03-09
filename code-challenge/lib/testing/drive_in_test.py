import pytest

from classes.car import Car
from classes.drive_in import DriveIn
from classes.movie_screen import MovieScreen

class TestDriveIn:
    '''DriveIn in drive_in.py'''

    def test_has_name(self):
        '''has an attribute "name", set in __init__().'''
        DriveIn(name="Netflix in the Car Park")
    
    def test_name_is_string_of_more_than_zero_length(self):
        '''requires "name" to be string of >0 characters.'''
        with pytest.raises(Exception):
            DriveIn(name=1)
        with pytest.raises(Exception):
            DriveIn(name='')
    
    def test_tells_whats_playing(self):
        '''has method "whats_playing()" that returns a list of movie titles from all screens.'''
        di = DriveIn("Mr. Drive In")
        movie_titles = ['A', 'B', 'C', 'D']
        di.screens = [MovieScreen(
            movie_title=m,
            capacity=24,
            drive_in=di
        ) for m in movie_titles]

        assert di.whats_playing() == ['A', 'B', 'C', 'D']