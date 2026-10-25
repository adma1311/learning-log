"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
      number_of_layers (int) : The amount of layers added in the lasagna.

    Returns:
      int: The total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the actual number of layers as an argument and returns how many minutes will be spent preparing them based on the 'PREPARATION_TIME'.
    
    """
    time_for_layers = PREPARATION_TIME * number_of_layers
    return time_for_layers
    
    
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time in minutes.

    Paramaters:
      number_of_layers (int): The number of layers added to the lasagna
      elapsed_baking_time (int): The number of minutes the lasagna has spent baking in the oven already

    Returns:
      int: Total time (in minutes) spent in the kitchen
    
    Function that returns the total minutes spent in the kitchen cooking including the preparation time and the time the lasagna has spent baking in the oven.

"""
    total_time_in_kitchen = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_time_in_kitchen



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)