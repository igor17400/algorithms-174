# -----------------------


def fibo_num_naive(n):
    """
    There's no need in saving all the numbers from fibonacci if we're
    only interest in the last digit.
    """
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def huge_fibo_num_naive(n, m):
    return fibo_num_naive(n) % m


# -----------------------
def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


# Calculate Fn mod m
def huge_fibo_num(n, m):

    # Getting the period
    pisano_period = pisanoPeriod(m)

    # Taking mod of N with period length
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == "__main__":
    lst = [(1, 239), (115, 1000), (2816213588, 239)]
    for n, m in lst:
        print(f"n = {n} --> n module m = {huge_fibo_num(n, m)}")
