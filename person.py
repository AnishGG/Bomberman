class person:

    def _make_person(self):
        if (self._disguise == "B" and
                self._dic[self._x, self._y + 1] in ("S", "L", "I", "W")):
            self._super_power = self._dic[self._x, self._y + 1]
        self._previous = " "
        if self._dic[self._x, self._y + 1] == "*":
            self._previous = "*"
        for i in range(self._x, self._x + 2):
            for j in range(self._y, self._y + 4):
                self._dic[i, j] = self._disguise

    def _destruct_person(self):
        if self._dic[self._x, self._y + 1] in ('0', '1', '2', '3', "O"):
            var = self._dic[self._x, self._y + 1]
        elif self._previous == "*":
            var = "*"
        elif self._dic[self._x, self._y + 1] == 'e':
            var = 'e'
        else:
            var = ' '
        for i in range(self._x, self._x + 2):
            for j in range(self._y, self._y + 4):
                self._dic[i, j] = var

    def __init__(self, x, y, dic, disguise, user):
        self._x = x
        # Here self.x represents the y-coordinate of the person
        self._y = y
        # and self.y represents the x-coordinate of the person
        self._dic = dic
        self._disguise = disguise
        self._user = user
        # stores the element which was there on bomberman position before he
        # came here
        self._previous = " "
        self._make_person()
        self._wallpass = False
        self._super_power = None

    def move_up(self, immortal):
        int_helper = 4
        check_dic = (" ", "B", "S", "L", "I", "W")
        if self._wallpass:
            int_helper = 2
            check_dic = (" ", "B", "*", "S", "L", "I", "W")
        # We know at
        if (self._x > int_helper and
                self._dic[self._x - 2, self._y] in check_dic):
            # a time only one person is present on the board, hence(" ","B")
            self._destruct_person()
            self._x = self._x - 2
            self._make_person()
        elif (self._x > 4 and self._dic[self._x - 2, self._y] in
                ("E") and self._dic[self._x, self._y] in ("B")):
            self._destruct_person()
            self._x -= 2
            if immortal is False:
                self._user[2] = 0

    def move_down(self, immortal):
        int_helper = 35
        check_dic = (" ", "B", "S", "L", "I", "W")
        if self._wallpass:
            int_helper = 37
            check_dic = (" ", "B", "*", "S", "L", "I", "W")
        if (self._x < int_helper and self._dic[self._x + 2, self._y] in
                check_dic):
            self._destruct_person()
            self._x += 2
            self._make_person()
        elif (self._x < 35 and self._dic[self._x + 2, self._y] in
                ("E") and self._dic[self._x, self._y] in ("B")):
            self._destruct_person()
            self._x += 2
            if immortal is False:
                self._user[2] = 0

    def move_right(self, immortal):
        int_helper = 69
        check_dic = (" ", "B", "S", "L", "I", "W")
        if self._wallpass:
            int_helper = 73
            check_dic = (" ", "B", "*", "S", "L", "I", "W")
        if (self._y < int_helper and self._dic[self._x, self._y + 4] in
                check_dic):
            self._destruct_person()
            self._y += 4
            self._make_person()
        elif (self._y < 69 and self._dic[self._x, self._y + 4] in
                ("E") and self._dic[self._x, self._y] in ("B")):
            self._destruct_person()
            self._y += 4
            if immortal is False:
                self._user[2] = 0

    def move_left(self, immortal):
        int_helper = 8
        check_dic = (" ", "B", "S", "L", "I", "W")
        if self._wallpass:
            int_helper = 4
            check_dic = (" ", "B", "*", "S", "L", "I", "W")
        if (self._y > int_helper and self._dic[self._x, self._y - 4] in
                check_dic):
            self._destruct_person()
            self._y -= 4
            self._make_person()
        elif (self._y > 8 and self._dic[self._x, self._y - 4] in
                ("E") and self._dic[self._x, self._y] in ("B")):
            self._destruct_person()
            self._y -= 4
            if immortal is False:
                self._user[2] = 0
