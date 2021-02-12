def falsa_posicao(f, d, a, b, tol, it=100):
    x = (a * f(b) - b * f(a))/(f(b) - f(a))
    count = 0

    while abs(f(x)) > tol and count < it:
        print(f"a = {'%.4f' % a}, "
              f"b = {'%.4f' % b}, "
              f"x = {'%.4f' % x}, "
              f"fa = {'%.4f' % f(a)}, "
              f"fx = {'%.4f' % f(x)}")

        if f(a) * f(x) > 0:
            a = x
        else:
            b = x

        x = (a * f(b) - b * f(a))/(f(b) - f(a))
        count += 1

    print(f"a = {'%.4f' % a}, "
          f"b = {'%.4f' % b}, "
          f"x = {'%.4f' % x}, "
          f"fa = {'%.4f' % f(a)}, "
          f"fx = {'%.4f' % f(x)}")

    return x
