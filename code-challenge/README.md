# Object Relations Code Challenge - DriveIn

For this challenge, we will be working with a drive-in movie domain.

We have three models: `DriveIn`, `MovieScreen`, and `Car`.

For this challenge, a `DriveIn` has many `MovieScreen`s, a `MovieScreen` has
many `Car`s, and a `Car` belongs to a `MovieScreen`.

A `DriveIn` has many `Car`s through its `MovieScreen`s. A `Car` is only at one
`DriveIn`.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

***

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

***

## Instructions

To get started, run `pipenv install; pipenv shell` while inside of this
directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has `pytest` tests available to you. Run
`pytest` at any time from within your virtual environment.

We've provided you with another tool that you can use to test your code. To use
it, run `python debug.py` from the command line. This will start a `ipdb`
session with your classes defined. You can test out the methods that you write
here. You can add code to the `debug.py` file to define variables and create
sample instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

***

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

> **Note: all setters should raise `Exception` if their criteria are not met.**

### Initializers, Readers, and Writers

#### DriveIn

- `DriveIn __init__(name)`
  - A drive-in should be initialized with a `name` as a string.
- `DriveIn property name()`
  - should return the name of the `DriveIn`
  - must be a string of greater than zero characters

#### MovieScreen

- `MovieScreen __init__((movie_title, capacity, drive_in)`
  - A movie screen should be initialized with a movie title as a string,
    capacity (as an integer), and a `drive_in` object.
- `MovieScreen property movie_title()`
  - should return the movie title
  - must be a string of greater than zero characters
- `MovieScreen capacity()`
  - should return the `MovieScreen`'s capacity
  - must be an integer greater than zero
- `MovieScreen property drive_in()`
  - should return the `DriveIn` instance associated with this `MovieScreen`
  - adds `MovieScreen` instance to `DriveIn` instance's screens

#### Car

- `Car __init__(passenger_count)`
  - A car should be initialized with a `passenger_count` (as an integer).
- `Car property passenger_count()`
  - returns the number of passengers in the car
  - must be an integer between 1 and 8

### Object Relationship Methods and Attributes

#### Car

- `Car current_movie_screen(movie_screen=None)`
  - returns the current movie screen that a particular car is associated with
  - can be passed a movie screen instance as an optional argument
    - creates an instance attribute `movie_screen`

#### MovieScreen

- `MovieScreen cars`
  - returns an list of all cars currently at this movie screen

#### DriveIn

- `DriveIn screens`
  - returns an list of all movie screens at this drive-in

### Aggregate Methods

#### MovieScreen

- `MovieScreen number_of_viewers()`
  - returns the total number of passengers viewing the movie, from all the cars
    currently at this movie screen
- `MovieScreen at_capacity()`
  - returns a boolean. If the number of cars at this movie screen is equal to or
    above the capacity of the movie screen, returns `True`. Otherwise, returns
    `False`
- `MovieScreen available_spots()`
  - returns the number of spots for cars available at this movie screen. This
    should be the capacity minus the number of cars currently at this movie
    screen
- `MovieScreen add_car(car)`
  - takes in a `Car` instance as the argument
  - depending on the available capacity of the movie screen, associates the
    `Car` with this movie screen.
    - if the movie screen is _not_ at capacity, updates the car's current movie
      screen and returns the string `"Enjoy!"`.
    - if the movie screen is at capacity, it should return the string `"Sold
      Out!"`, and should not associate the car to the movie screen.
- `MovieScreen remove_car(car)`
  - takes in a `Car` instance as the argument
  - removes the `Car` instance from the screen's cars if present

#### DriveIn

- `DriveIn whats_playing()`
  - returns an list of all the names of the **unique** movies playing at the
  movie screens at this drive-in.
- `DriveIn full_house()`
  - returns `True` if all movie screens at _this_ drive-in are at capacity.
    Otherwise, returns `False`.
