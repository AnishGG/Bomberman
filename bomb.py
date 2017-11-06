class bomb:

    # user[0] will have score and user[1] will have number of lives left
    def __init__(self, x, y, dic, user, ene, explosion_effect):
        self._ene = ene
        # user[2] will contain 1 if user is alive and 0 if he is dead
        self._timer = 3
        self._dic = dic  # ene is the enemy list needed to destruct them
        self._x = x
        self._y = y
        self._user = user
        self._effect = explosion_effect
        self._previous = " "
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                if j == y or j == y + 3:
                    self._dic[i, j] = "B"
                else:
                    self._dic[i, j] = "O"

    def give(self):
        return self._dic

    def tick(self, immortal):
        if self._timer > 0:
            self._timer = self._timer - 1
            for i in range(self._x, self._x + 2):
                for j in range(self._y, self._y + 4):
                    self._dic[i, j] = str(self._timer)
        elif self._timer >= -1:
            if self._effect == 'normal':
                self.explosion(immortal)
            elif self._effect == 'large':
                self.super_large_explosion(immortal)
            self._timer = self._timer - 1
        else:
            self._previous = " "
            pass

    def stop_this_enemy(self, n, m):
        for i in self._ene:
            print(i)
            if i._x == n and i._y == m:
                i.stopme()

    def explode(self, n, m, immortal):
        # This function will be used to allot points whenever enemy dies or
        # brick falls
        if(self._timer == 0):
            if self._dic[n, m] == '/':
                self._user[0] = self._user[0] + 20
            elif self._dic[n, m] == 'E':
                self.stop_this_enemy(n, m)
                self._user[0] = self._user[0] + 100
            elif self._dic[n, m] == 'B':
                if immortal:
                    self._previous = "B"
                else:
                    self._user[2] = 0
            # user contains the information whether bomberman will die if it is
            # standing on bomb
            elif self._user[4]._x == n and self._user[4]._y == m:
                if immortal:
                    self._previous = "B"
                else:
                    self._user[2] = 0
            for i in range(n, n + 2):
                for j in range(m, m + 4):
                    self._dic[i, j] = "e"
        else:
            var = self._previous
            if var == "B":
                # checking if bomberman has run away in that 1 second time
                # period
                if (self._user[4]._x == n and self._user[4]._y == m) is False:
                    var = " "
            for i in range(n, n + 2):
                for j in range(m, m + 4):
                    self._dic[i, j] = var

    def explosion(self, immortal):
        # e is in the newDic so as to clear the impacted area afterwards
        self.explode(self._x, self._y, immortal)
        bombDic = (" ", "B", "E", "e", "/")
        if self._x > 4 and self._dic[self._x - 2, self._y] in bombDic:
            self.explode(self._x - 2, self._y, immortal)
        if self._x < 35 and self._dic[self._x + 2, self._y] in bombDic:
            self.explode(self._x + 2, self._y, immortal)
        if self._y < 69 and self._dic[self._x, self._y + 4] in bombDic:
            self.explode(self._x, self._y + 4, immortal)
        if self._y > 8 and self._dic[self._x, self._y - 4] in bombDic:
            self.explode(self._x, self._y - 4, immortal)

    def large_explosion(self, immortal):
        bombDic = (" ", "B", "E", "e", "/")
        self.explosion(immortal)        # This is to always happen
        # left-up
        if (self._x > 4 and self._y > 8 and
                self._dic[self._x - 2, self._y - 4] in bombDic):
            self.explode(self._x - 2, self._y - 4, immortal)
        # right-up
        if (self._x > 4 and self._y < 69 and
                self._dic[self._x - 2, self._y + 4] in bombDic):
            self.explode(self._x - 2, self._y + 4, immortal)
        # right-down
        if (self._x < 35 and self._y < 69 and
                self._dic[self._x + 2, self._y + 4] in bombDic):
            self.explode(self._x + 2, self._y + 4, immortal)
        # left-down
        if (self._y > 8 and self._x < 35 and
                self._dic[self._x + 2, self._y - 4] in bombDic):
            self.explode(self._x + 2, self._y - 4, immortal)

    def super_large_explosion(self, immortal):
        bombDic = (" ", "B", "E", "e", "/")
        self.large_explosion(immortal)
        # double-up
        if self._x > 6 and self._dic[self._x - 4, self._y] in bombDic:
            self.explode(self._x - 4, self._y, immortal)
        # double-down
        if self._x < 33 and self._dic[self._x + 4, self._y] in bombDic:
            self.explode(self._x + 4, self._y, immortal)
        # double-right
        if self._y < 65 and self._dic[self._x, self._y + 8] in bombDic:
            self.explode(self._x, self._y + 8, immortal)
        # double-left
        if self._y > 12 and self._dic[self._x, self._y - 8] in bombDic:
            self.explode(self._x, self._y - 8, immortal)
