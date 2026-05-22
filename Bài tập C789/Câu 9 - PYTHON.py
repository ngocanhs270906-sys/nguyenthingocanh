a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))

tong = a + b + c
print("Tổng {} + {} + {} = {}".format(a, b, c, tong))

dem_chan = 0
temp = tong

while temp > 0:
    chu_so = temp % 10

    if chu_so % 2 == 0:
        dem_chan += 1

    temp //= 10

print(f"Trong tổng có {dem_chan} chữ số chẵn")
