# -*- coding: utf-8 -*-

__author__ = "Helge Helø Klemetsdal"
__email__ = "helge.helo@gmail.com"

from pieces import Pawn, Rook, Bishop, Knight, King, Queen


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
    def create_template_board(cls):
        """
        The aim of this classmethod is to set the board type to a default
        chess board. This will be initialised instantly when creating a
        new board. New functions are needed for creating custom boards,
        including fisher random and customised boards.
        :returns
        -------
        The basic chess board instance: list
        """
        letter_coordinates = ["a", "b", "c", "d", "e", "f", "g", "h"]
        board_coordinates = {value: index + 1 for index, value in enumerate(
            letter_coordinates)}
        board = [[] for i in range(len(board_coordinates))]

        return board, letter_coordinates, board_coordinates

    def set_default_board(cls):
        cls.board, cls.letters, cls.coordinates = cls.create_template_board()
        return cls.board, cls.letters, cls.coordinates

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
            self.board, self.letters, self.coordinates = self.set_default_board()

    def find_coordinate_at_board(self, coordinate):
        if coordinate[0] not in self.letters:
            raise TypeError("Coordinate must have a letter")

        if coordinate[1] not in range(1, 9):
            raise TypeError("Coordinate must have a number")

        row = self.letters.index(coordinate[0])
        column = self.coordinates(coordinate[1])
        return self.board[row*column]

    def kill_piece(self, coordinate):
        """
        Removes the piece from a given list.
        Parameters
        ----------
        coordinate:
            input coordinate in chess form. Ex: "h1"
        """
        index = self.find_coordinate_at_board(coordinate)
        self.board[index].pop()




if __name__ == "__main__":
    """
    """
