a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a <= 0 or b <= 0:
    print("a và b phải là số nguyên dương")
else:
    tong = a + b
    chu_so_lon_nhat = max(int(ch) for ch in str(tong))
    print(f"Tổng a + b = {tong}")
    print(f"Chữ số lớn nhất trong tổng là: {chu_so_lon_nhat}")