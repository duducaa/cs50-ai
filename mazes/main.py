import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

maze = cv.imread("./maze2.png")
gray = cv.cvtColor(maze, cv.COLOR_BGR2GRAY)

coef = 2.6 * 1.5
gray = cv.resize(gray, (int(gray.shape[0] // coef), int(gray.shape[1] // coef)))

mask = cv.inRange(gray, 126, 255)
maze = np.where(mask > 0, "#", " ")
df = pd.DataFrame(maze)
df.to_csv("maze2.csv", header=None, index=None)

print(gray.shape)

# df = pd.DataFrame(maze)
# print(df)
# df.to_csv("maze2.csv", header=None, index=None)


cv.imwrite("edited-maze2.png", mask)

# cv.imwrite("maze2.csv")