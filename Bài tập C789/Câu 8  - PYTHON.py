x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
z = int(input("Nhập z: "))

tich = x * y * z
tich_str = str(tich)

so_chu_so = len(tich_str)
chu_so_lon_nhat = max(tich_str)

print(f"Tích {x} * {y} * {z} = {tich}")
print(f"Số chữ số của tích: {so_chu_so}")
print(f"Chữ số lớn nhất trong tích: {chu_so_lon_nhat}")