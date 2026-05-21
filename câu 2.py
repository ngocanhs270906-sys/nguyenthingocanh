n = int(input("Nhập số nguyên dương n: "))

tong_chu_so = 0
temp = n
while temp > 0:
    tong_chu_so += temp % 10
    temp //= 10

if tong_chu_so % 3 == 0:
    print(f"Tổng các chữ số = {tong_chu_so} → Chia hết cho 3.")
else:
    print(f"Tổng các chữ số = {tong_chu_so} → Không chia hết cho 3.")
