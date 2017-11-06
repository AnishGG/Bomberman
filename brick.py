#!/usr/bin/python
# -*- coding: utf-8 -*-
# /usr/bin/python

from random import randint
from unoccupied import unoccupied


class brick:

    # un is a list containing unoccupied places in our dic and oc is vice-versa
    def __init__(
        self,
        un,
        oc,
        dic,
    ):
        self._un = un
        self._oc = oc
        length = len(self._un)
        ran = randint(1, length - 1)
        i = self._un[ran][0]
        j = self._un[ran][1]
        self._un.remove([i, j])
        self._oc.append([i, j])
        for x in range(i, i + 2):
            for y in range(j, j + 4):
                dic[x, y] = '/'
