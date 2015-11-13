#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module to help you win some Mega Millions. """

from random import randint

def generate_mega_millions(number_of_games=1):
    """ Generates a group of numbers to play Mega Millions.

        Generates number_of_games groups of numbers to play
        Mega Millions where the first five numbers of a tuple
        are the regular numbers and the last number is the
        Mega Ball.

        Args:
            number_of_games (int, optional): Number of games to
		generate. Defaults to 1.

        Returns:
            A list of tuples. Each integer tuple represents a game.

        Examples:
            $ generate_mega_millions()
            $ [(5, 23, 50, 22, 13, 14)]

            $ generate_mega_millions(2)
            $ [(12, 23, 60, 35, 71, 4), (11, 5, 20, 45, 75, 10)]
    """
    dummy_games = []
    for game in range(number_of_games):
        current_game = []
        while len(current_game) < 5:
            number = randint(1, 75)
            if number not in current_game:
                current_game.append(number)
        current_game.append(randint(1, 15))
        dummy_games.append(tuple(current_game))
    return dummy_games

if __name__ == '__main__':
    print 'Generating 1 game: {}\n'.format(generate_mega_millions())
