def createGrid(m: int, n: int) -> list[str]:
    grid = []
    grid.append("." * n)

    for i in range(1, m):
        grid.append('#' * (n - 1) + '.')

    return grid

print(createGrid(2, 3)) 