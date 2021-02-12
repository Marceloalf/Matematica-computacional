def bisseccao(f, d, a, b, tol, it=100):
    x = (a + b)/2
    count = 0

    while abs(f(x)) > tol and count < it:
        print(f"a = {'%.4f'%a}, "
              f"b = {'%.4f'%b}, "
              f"x = {'%.4f'%x}, "
              f"fa = {'%.4f'%f(a)}, "
              f"fx = {'%.4f'%f(x)}")

        if f(a) * f(x) > 0:
            a = x
        else:
            b = x

        x = (a + b)/2
        count += 1

    print(f"a = {'%.4f' % a}, "
          f"b = {'%.4f' % b}, "
          f"x = {'%.4f' % x}, "
          f"fa = {'%.4f' % f(a)}, "
          f"fx = {'%.4f' % f(x)}")

    return x
