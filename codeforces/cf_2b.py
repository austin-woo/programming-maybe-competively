def count_factor(num: int, factor: int) -> int:
    c = 0
    while num > 0 and num % factor == 0:
        c += 1
        num //= factor
    return c