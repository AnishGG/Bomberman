class unoccupied:

    def __init__(self):
        self._unoccupied = {}
        self._un = []
        self._oc = []
        for i in range(1, 40):
            for j in range(1, 90):
                self._unoccupied[i, j] = 0
        for i in range(3, 36, 4):
            for j in range(5, 70, 4):
                self._un.append([i, j])
                # the starting of the blocks which are not
                self._unoccupied[i, j] = "1"
                # occupied
        for i in range(5, 36, 4):
            for j in range(5, 70, 8):
                self._un.append([i, j])
                self._unoccupied[i, j] = "1"
