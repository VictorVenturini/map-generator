import random

SIZE = 20

def printWorld(world):
    colors = ["🟪", "🟨","🟧","🟩", "🟦"]
    for line in world:
        for chunk in line:
            print(colors[chunk -1], end="\t")
        print()

def createWorld():
    world = []
    for _ in range(SIZE):
        line = []
        for _ in range(SIZE):
           line.append(0)
        world.append(line)
    return world

def insertDiagonalBiom(world):
    for i in range(SIZE):
        if i == 0:
            world[i][i] = random.choice([1,2,3,4,5])
        else:
            sorted_ = random.choice([1,2,3,4,5,6,7,8]) in [1,2,4,6]
            if sorted_:
                numeber_sorted =  random.choice([1,2,3,4,5])
                if numeber_sorted == world[i-1][i-1]:
                    option = [1,2,3,4,5]
                    option.remove(numeber_sorted)
                    newnumeber_sorted =  random.choice(option)
                    world[i][i] = newnumeber_sorted
                else:
                    world[i][i] = numeber_sorted
            else:
                world[i][i] = world[i-1][i-1]

def insertPositiveBiom(world, size, j):
    for i in range(size - j):
        sorted_ = random.choice([1,2,3,4,5,6,7])
        sorted_1 = sorted_ in [1,2,3]
        sorted_2 = sorted_ in [4,5,6]
        sorted_3 = sorted_ in [7]
        sorted_0 = random.choice([1,2,3,4,5,6,7])
        sorted_01 = sorted_0 in [1,2,3]
        sorted_02 = sorted_0 in [4,5,6]
        sorted_03 = sorted_0 in [7]
        if sorted_1:
            world[i][i+j] = world[i][i+j-1]
        if sorted_2:
            world[i][i+j] = world[i+1][i+j]
        if sorted_3:
            world[i][i+j] = random.choice([1,2,3,4,5])
        if sorted_01:
            world[i+j][i] = world[i-1+j][i]
        if sorted_02:
            world[i+j][i] = world[i+j][i+1]
        if sorted_03:
            world[i+j][i] = random.choice([1,2,3,4,5])
    j += 1
    if j != size:
        insertPositiveBiom(world, size, j)

world = createWorld()
insertDiagonalBiom(world)
j = 1
insertPositiveBiom(world, SIZE, j)
printWorld(world)
