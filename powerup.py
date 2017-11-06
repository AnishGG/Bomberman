from unoccupied import unoccupied
from random import randint


class powerup:

    def make(self):
        for i in range(self._x, self._x + 2):
            for j in range(self._y, self._y + 4):
                self._dic[i, j] = self._disguise

    def __init__(self, bomber):
        # speedUp, largeExplosion, Immortality, WallPass
        arr = ["S", "L", "I", "W"]
        ran = randint(0, 3)
        disguise = arr[ran]
        self._bomber = bomber
        self._timer = 3
        self._dic = bomber._dic
        self._disguise = disguise
        x = unoccupied()
        un = x._un
        print(un[0])
        for i in un:
            if self._dic[i[0], i[1]] != " ":
                un.remove(i)
        ran = randint(1, len(un) - 1)
        x = un[ran][0]
        y = un[ran][1]
        self._x = x
        self._y = y
        self.make()

    def destruct(self):
        for i in range(self._x, self._x + 2):
            for j in range(self._y, self._y + 4):
                self._dic[i, j] = " "

    def tick(self):
        if self._timer > 0:
            self._timer -= 1
        elif self._timer > -1:
            self._timer -= 1
            self.destruct()
        else:
            self._timer -= 1

    def status(self):
        if self._timer < 0:
            return True
        else:
            return False
