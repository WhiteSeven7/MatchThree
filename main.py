from game.game import Game


def main(wall_):
    connect_set = set()
    for pos in wall_:
        a, a_1, a_2 = wall_[pos], wall_[pos + (1, 0)], wall_[pos + (2, 0)]
        a__1, a__2 = wall_[pos + (0, 1)], wall_[pos + (0, 2)]
        if a and a_1 and a_2 and a.color == a_1.color == a_2.color:
            for a_ in (a, a_1, a_2):
                if a_.g:
                    a_.g.add(a, a_1, a_2)
                    break
            else:
                connect_set.add({a, a_1, a_2})
        if a and a__1 and a__2 and a.color == a__1.color == a__2.color:
            for a__ in (a, a__1, a__2):
                if a__.g:
                    a__.g.add(a, a__1, a__2)
                    break
            else:
                connect_set.add({a, a__1, a__2})

    return connect_set


if __name__ == '__main__':
    game = Game()
    game.run()
