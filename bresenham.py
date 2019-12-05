import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    tx = x2 - x1
    ty = y2 - y1
    m = ty / tx
    p0 = 2 * ty - tx
    newx1 = x1 + 1
    newy1 = y1 + 1
    newx2=newx1-x1
    k = 0
    print('k:', k, '   ', 'pk:', p0, "   ", 'newx0:', newx1, "   ", 'newy0:', newy1, "   ")
    newk = k + 1
    while newk < 10:
      newp01 = p0 + 2 * ty - 2 * tx * (newy1-y1)
      newp02 = newp01 + ((2 * ty) * (newx2)) - (2 * tx)
      if newp01 > 0:
        newx1 = newx1 + 1
        newy1 = newy1 + 1
        print('k:', newk, '   ', 'pk:', newp01 , "   ", 'newx1:', newx1, "   ", 'newy1:', newy1, "   ")
      elif newp02< 0:
        newx1 = newx1 + 1
        newy2 = newy1
        print('k:', newk, '   ', 'pk:', newp02, "   ", 'newx2:', newx1, "   ", 'newy2:', newy2, "   ")
        newy3 = newy2 - newy1
        newp03 = newp02 + 2 * ty + (2 * tx * (newy3))
      newk = newk + 1
      continue

DDA(20, 10, 30, 18)
