# -*- coding: utf-8 -*-

__author__ = "Helge Helø Klemetsdal"
__email__ = "helge.helo@gmail.com"

#from pieces.py import Pawn,Rook,Bishop,Knight,King,Queen
#

class Board:
    """ Class for the chessboard which should contain the pieces, and
        where to simulate the game events

        Parameters
        ----------
        ----------
            Value describing the animals fitness
        a: int
            Initial age of the animal.
        weight: float
             Weight drawn from the Gaussian distribution if not assigned a value.
        parameters : dict
            Values that describe the behaviour of the animals.

        Raises
        ------
        ValueError
            If age is below 0 or if weight is below, 0 or None.

        """

    @classmethod
    def set_default_board(cls):
        """
        The aim of this classmethod is to set the board type to a default
        chess board. This will be initialised instantly when creating a
        new board. New functions are needed for creating custom boards,
        including fisher random and customised boards.
        :returns
        -------
        The basic chess board instance: list
        """
        letter_coordinates = ["a","b","c","d","e","f","g","h"]
        board_cordinates = {value:index+1 for index, value in enumerate(
            letter_coordinates)}

 #       board =
        return 
    @classmethod
    def set_fisher_random_board(cls):
     """
     :parameter
     ----------

     :raises
     -------

     :returns
     -------
     A fisher random chess board instance: list
     """
    @classmethod
    def set_custom_board(cls):
        """
        :parameter
        ----------

        :raises
        -------


        :returns
        --------


        """
    def __init__(self, board_type=None):
        if board_type is None:
            self.set_default_board()




if __name__=="__main__":
    """
    """