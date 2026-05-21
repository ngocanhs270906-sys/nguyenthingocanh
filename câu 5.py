m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong_chu_so_n = 0
temp = n
while temp > 0:
    tong_chu_so_n += temp % 10
    temp //= 10

print(f"Tổng các chữ số của n = {tong_chu_so_n}")

if tong_chu_so_n == 0:
    print("Tổng chữ số bằng 0, không thể chia.")
elif m % tong_chu_so_n == 0:
    print(f"{m} chia hết cho {tong_chu_so_n}.")
else:
    print(f"{m} không chia hết cho {tong_chu_so_n}.")