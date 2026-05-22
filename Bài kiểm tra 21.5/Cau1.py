n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
if n <= 0 or n >= 100:
    print("n không hợp lệ")
else:
    ds = []
    for i in range(n):
        x = float(input(f"Nhập x_{i+1}: "))
        ds.append(x)

    tong = 0
    dem = 0
    for x in ds:
        if 0 < x < 1000:
            tong += x
            dem += 1

    if dem > 0:
        tbc = tong / dem
        print(f"Trung bình cộng các số dương trong (0,1000) là: {tbc}")
    else:
        print("Không có số nào thỏa mãn")