class Tower(object):
    def __init__(self, n = 0):
        self.Disks = [k for k in range(n)] if n > 0 else []

    def addDisk(self, d):
        self.Disks.append(d)

    def moveTopDisk(self, t):
        if len(self.Disks) > 0:
            t.add(self.Disks.pop())

    def moveDisks(self, n, destination, buffer):
        if n == 0: return
        self.moveDisks(n-1, buffer, destination)
        self.moveTopDisk(destination)
        buffer.moveDisks(n-1, destination, self)

    def add(self, d):
        self.Disks.append(d)

def hanoi(n):
    t1, t2, t3 = Tower(n), Tower(), Tower()
    print(f"T1 = {t1.Disks}, T2 = {t2.Disks}, T3 = {t3.Disks}")
    t1.moveDisks(n, t3, t2)
    print(f"T1 = {t1.Disks}, T2 = {t2.Disks}, T3 = {t3.Disks}")

hanoi(10)