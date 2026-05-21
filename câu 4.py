a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b
print(f"Tổng (a + b) = {tong}")

chu_so_lon_nhat = 0
temp = tong
while temp > 0:
    chu_so = temp % 10
    if chu_so > chu_so_lon_nhat:
        chu_so_lon_nhat = chu_so
    temp //= 10

print(f"Chữ số lớn nhất trong tổng: {chu_so_lon_nhat}")
