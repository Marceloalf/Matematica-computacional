def secante(f, d, x1, x2, tol, it=50):
    x = x2 - (f(x2) * (x1 - x2))/(f(x1) - f(x2))
    count = 0

    while abs(f(x)) > tol and count < it:
        print(f"a = {'%.4f' % x1}, "
              f"b = {'%.4f' % x2}, "
              f"x = {'%.4f'%x}, "
              f"fa = {'%.4f'%f(x1)}, "
              f"fb = {'%.4f'%f(x2)}, "
              f"fx = {'%.4f'%f(x)}, ")

        x = x2 - (f(x2) * (x1 - x2))/(f(x1) - f(x2))
        x1 = x2
        x2 = x

        count += 1

    print(f"a = {'%.4f' % x1}, "
          f"b = {'%.4f' % x2}, "
          f"x = {'%.4f' % x}, "
          f"fa = {'%.4f' % f(x1)}, "
          f"fb = {'%.4f' % f(x2)}, "
          f"fx = {'%.4f' % f(x)}, ")

    return x
