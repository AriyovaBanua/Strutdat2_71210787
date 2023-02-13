def is_prime(n, i):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

def rekursi_prima(n, current, benar):
    if benar < n:
        if is_prime(current, 2):
            print(current, end=", ")
            benar = benar+1
        rekursi_prima(n, current + 1, benar)

n = int(input("masukan nilai n: "))
rekursi_prima(n, 2, 0)
