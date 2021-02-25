from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    changeX = x0 - x1
    changeY = y1 - y0

    if changeY == 0:  # if horizontal line
        while x0 < x1:
            plot(screen, color, x0, y0)
            x0 += 1
        return
    if changeX == 0:  # if vertical line
        while y0 < y1:
            plot(screen, color, x0, y0)
            y0 += 1
        return

    slope = -1 * changeY / changeX

    if (slope > 0) and (slope < 1):  # octants 1 and 5
        dv = 2 * changeY + changeX

        while x0 <= x1:
            plot(screen, color, x0, y0)
            if dv > 0:
                y0 += 1
                dv += 2 * changeX
            x0 += 1
            dv += 2 * changeY
        return

    if slope >= 1:  # octants 2 and 6
        dv = 2 * changeX + changeY

        while y0 <= y1:
            plot(screen, color, x0, y0)
            if dv < 0:
                x0 += 1
                dv += 2 * changeY
            y0 += 1
            dv += 2 * changeX
        return

    if (slope < 0) and (slope > -1):  # octants 4 and 8
        dv = 2 * changeY + changeX

        while x0 <= x1:
            plot(screen, color, x0, y0)
            if dv < 0:
                y0 -= 1
                dv -= 2 * changeX
            x0 += 1
            dv += 2 * changeY
        return

    if slope <= -1:  # octants 3 and 7
        dv = 2 * changeX + changeY

        while y0 >= y1:
            plot(screen, color, x0, y0)
            if dv > 0:
                x0 += 1
                dv += 2 * changeY
            y0 -= 1
            dv -= 2 * changeX
        return
