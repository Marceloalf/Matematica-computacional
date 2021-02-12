def newton(f, d, x, b, tol, it):
    count = 0

    while abs(f(x)) > tol and count < it:
        print(f"x = {'%.4f'%x}, "
              f"fx = {'%.4f'%f(x)}, "
              f"dx = {'%.4f'%d(x)}")

        x = x - f(x)/d(x)
        count += 1

    print(f"x = {'%.4f' % x}, ",
          f"fx = {'%.4f' % f(x)}, ",
          f"dx = {'%.4f' % d(x)}")

    return x
