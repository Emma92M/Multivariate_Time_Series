import numpy as np



def make_grid(nx: int, ny: int) -> np.ndarray:
    ans = np.ndarray((nx * ny, 2))
    for x in range(nx):
        for y in range(ny):
            ans[x + ny * y][0] = float(x)
            ans[x + ny * y][1] = float(y)
    return ans


def randomly_rotated_versor() -> np.ndarray:
    angle = np.random.uniform(0, np.pi * 2)

    m = np.asarray([np.sin(angle), np.cos(angle)])

    return m
#geometric correction algorithm

def random_factor(low: float = 0.25, high: float = 4.) -> float:
    v = np.random.uniform(np.log(low), np.log(high))
    return np.exp(v)


def random_matrix() -> np.ndarray:
    v1 = randomly_rotated_versor()
    while True:
        v2 = randomly_rotated_versor()
        if not np.isclose(np.dot(v1, v2), 0):
            break

    return np.asarray([v1 * random_factor(), v2 * random_factor()])


def make_random_grid(nx: int, ny: int) -> tuple[np.ndarray, np.ndarray]:
    grid = make_grid(nx, ny)

    m = random_matrix()
    grid_rot = np.matmul(grid, m)

    center = np.mean(grid_rot, 0)
    stdev = np.std(grid_rot, 0)

    def filt(p: np.ndarray) -> bool:
        val = (p - center) / stdev
        return max(abs(val)) < 1

    points = grid_rot[[filt(p) for p in grid_rot]]
    return points, m


def get_mean(grid):
    return np.mean(grid, 0)


def get_grid_mean(grid):
    """
    :param grid:
    :return: The coordinates of the grid point that is closest to the center of mass of the whole grid
    """
    m = get_mean(grid)
    dist = [np.linalg.norm(m - el) for el in grid]
    return grid[np.argmin(dist), :]


def get_closest(grid, center, i):
    dist = np.asarray([np.linalg.norm(center - el) for el in grid])
    return grid[dist.argsort()][i]


def get_closest_fun(P1, P2):
    P = P2 - P1
    a = P[0] * P1[1] - P[1] * P1[0]
    m = np.linalg.norm(P)

    def fun(Point):
        if len(Point.shape) == 2:
            Point = np.transpose(Point, (1, 0))

        l = P[1] * Point[0] - P[0] * Point[1] + a
        return l / m

    return fun


def get_perpendicular(grid):
    center = get_grid_mean(grid)
    first = get_closest(grid, center, 1)
    second = get_closest(grid, center, 2)
    dist1 = np.linalg.norm(center - first)
    dist2 = np.linalg.norm(center - second)
    jitter = np.abs(dist1 - dist2) * 100
    avg = (first + second) / 2
    if (not np.isclose(avg[0], center[0], jitter) or not np.isclose(avg[1], center[1], jitter)):
        assert "Two closest aren't in line!"
    dist_fun = get_closest_fun(first, second)
    filter_on_the_line = np.isclose(np.abs(dist_fun(grid)), 0., jitter)
    new_grid = grid[np.logical_not(filter_on_the_line)]
    first_perp = get_closest(new_grid, center, 0)
    second_perp = get_closest(new_grid, center, 1)
    return first, second, first_perp, second_perp, center


def transpose(grid):
    first, second, first_perp, second_perp, center = get_perpendicular(grid)
    v1 = center - second
    v2 = center - second_perp
    m = np.asarray([v1, v2])
    m_inv = np.linalg.inv(m)
    # print(m_inv)
    return np.matmul(grid - center, m_inv), m_inv
    #return v1, v2, m

if __name__ == '__main__':
    grid,_ = make_random_grid(40, 40)




    m = random_matrix()
    print(grid)
    m2 = np.matmul(grid, m)


    print(transpose(grid))
