def is_prime(n, i):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

def rekursi_prima(n, current):
    if current <= n:
        if is_prime(current, 2):
            print(current)
        rekursi_prima(n, current + 1)

n = int(input("masukan nilai n: "))
rekursi_prima(n, 2)
