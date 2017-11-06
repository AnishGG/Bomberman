from person import person
from random import randint


class enemy(person):

    # note un is a list of unoccupied places in the dic and oc is vice-versa
    def __init__(self, un, oc, dic, user):
        disguise = 'E'
        length = len(un)
        # 2 is taken as at position 1 bomberman spawns
        ran = randint(2, length - 1)
        x = un[ran][0]
        y = un[ran][1]
        un.remove([x, y])
        oc.append([x, y])
        person.__init__(self, x, y, dic, disguise, user)
        self._dir = {}
        self._user = user
        self._stop = 0

    def stopme(self):
        self._stop = 1

    def give_status(self):
        if self._stop == 0:  # means not stoped
            return True
        else:
            return False

    def direction(self):
        #   l,u,r,d
        if self._y > 8 and self._dic[self._x, self._y + 4] in (" ", "B"):
            self._dir[0] = 1
        else:
            self._dir[0] = 0
        if self._x > 4 and self._dic[self._x - 2, self._y] in (" ", "B"):
            self._dir[1] = 1
        else:
            self._dir[1] = 0
        if self._y < 69 and self._dic[self._x, self._y + 4] in (" ", "B"):
            self._dir[2] = 1
        else:
            self._dir[2] = 0
        if self._x < 35 and self._dic[self._x + 2, self._y] in (" ", "B"):
            self._dir[3] = 1
        else:
            self._dir[3] = 0

    def give(self):
        return self._dic

    def random_move(self, immortal):
        self.direction()
        count = 0
        ret = -1
        helper = {}
        for i in self._dir:
            if self._dir[i] == 1:
                count = count + 1
                helper[count] = i
        if count is not 0:
            x = randint(1, count)
            ret = helper[x]
        if ret == -1:
            pass
        else:
            if ret == 0:
                if self._dic[self._x, self._y - 4] in ("B"):
                    if immortal is False:
                        self._user[2] = 0
                self.move_left(immortal)
            elif ret == 1:
                if self._dic[self._x - 2, self._y] in ("B"):
                    if immortal is False:
                        self._user[2] = 0
                self.move_up(immortal)
            elif ret == 2:
                if self._dic[self._x, self._y + 4] in ("B"):
                    if immortal is False:
                        self._user[2] = 0
                self.move_right(immortal)
            else:
                if self._dic[self._x + 2, self._y] in ("B"):
                    if immortal is False:
                        self._user[2] = 0
                self.move_down(immortal)
