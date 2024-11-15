# TODO решите задачу
def task() -> float:
    a = 0
    sch = 0
    sm = 0
    x = 0
    y = 0
    f = open("input.json", "r")
    a = f.readlines()
    for i in range(len(a)):
        if a[i].find("score") != -1:
            x = float(a[i][((a[i].find("score")) + 8):len(a[i]) - 2])
        elif (a[i].find("weight")) != -1:
            y = float(a[i][((a[i].find("weight")) + 9):len(a[i]) - 1])
        if (x != 0) and (y != 0):
            sm += x * y
            x, y = 0, 0
    f.close()
    return round(sm, 3)
print(task())
