def la_so_nguyen_to(n):

    if n < 2:

        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            return False

    return True

n = int(input("Nhap so phan tu n (0 < n < 100): "))

while n <= 0 or n >= 100:

    n = int(input("Nhap lai n (0 < n < 100): "))

day_so = []

for i in range(n):

    x = int(input(f"Nhap phan tu thu {i+1}: "))

    day_so.append(x)

tong_nguyen_to = 0

for so in day_so:

    if la_so_nguyen_to(so):

        tong_nguyen_to += so



print(f"Tong cac so nguyen to: {tong_nguyen_to}")

if tong_nguyen_to % 2 != 0 and tong_nguyen_to > 50:

    print("Tong la so le va lon hon 50")

else:

    print("Tong KHONG thoa man dieu kien (so le va lon hon 50)")
