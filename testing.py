import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

pose_keypoints = np.array([16, 14, 12, 11, 13, 15, 24, 23, 25, 26, 27, 28])

def read_keypoints(filename):
    fin = open(filename, 'r')

    kpts = []
    while True:
        line = fin.readline()
        if line == '':
            break

        line = line.split()
        line = [float(s) for s in line]

        line = np.reshape(line, (len(pose_keypoints), -1))
        kpts.append(line)

    kpts = np.array(kpts)
    return kpts

def update(frame):
    ax.cla()

    for bodypart, part_color in zip(body, colors):
        for c in bodypart:
            ax.plot(
                xs=[p3ds[frame, c[0], 0], p3ds[frame, c[1], 0]],
                ys=[p3ds[frame, c[0], 1], p3ds[frame, c[1], 1]],
                zs=[p3ds[frame, c[0], 2], p3ds[frame, c[1], 2]],
                linewidth=4,
                c=part_color
            )

    ax.scatter(p3ds[frame, :, 0], p3ds[frame, :, 1], p3ds[frame, :, 2], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

if __name__ == '__main__':
    p3ds = read_keypoints('kpts_3d.dat')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    torso = [[0, 1], [1, 7], [7, 6], [6, 0]]
    armr = [[1, 3], [3, 5]]
    arml = [[0, 2], [2, 4]]
    legr = [[6, 8], [8, 10]]
    legl = [[7, 9], [9, 11]]
    body = [torso, arml, armr, legr, legl]
    colors = ['red', 'blue', 'green', 'black', 'orange']

    ani = FuncAnimation(fig, update, frames=len(p3ds), interval=100)
    plt.show()
