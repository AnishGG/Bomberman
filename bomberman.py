from person import person
from bomb import bomb


class bomberman(person):

    def __init__(self, x, y, dic, user, ene, bomb_effect):
        self._ene = ene
        self._powerup = None
        self._bomb_effect = bomb_effect
        disguise = 'B'
        person.__init__(self, x, y, dic, disguise, user)
        self._bom = bomb(999, 999, self._dic, user, ene,
                         'normal')  # garbage large number
        self._bom._timer = -2

    def drop_bomb(self):
        if self._bom._timer < -1:
            self._bom = bomb(self._x, self._y, self._dic,
                             self._user, self._ene, self._bomb_effect)
        else:
            pass
            # means bomb already there

    def dead(self):
        for i in range(self._x, self._x + 2):
            for j in range(self._y, self._y + 4):
                self._dic[i, j] = 'X'
