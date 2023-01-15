# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
# В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более, чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import random
from itertools import cycle


def take_candys(max_candys):
    while True:
        raw_candys = input('возьмите конфеты[{}..{}] '.format(1, max_candys))
        try:
            candys = int(raw_candys)
            if not 1 <= candys <= max_candys:
                raise ValueError()
        except ValueError as ex:
            print('неверные данные')
        else:
            return candys


def game(candys, players):
    players = random.sample(players, len(players))

    for player in cycle(players):
        print('{} ходит'.format(player))
        candys -= take_candys(min(28, candys))
        print('осталось {} конфет'.format(candys))
        if candys == 0:
            print('{} победил'.format(player))
            break


if __name__ == '__main__':
    game(candys=221, players=['игрок 1', 'игрок 2'])
