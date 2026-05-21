n = int(input("Nhập số phần tử n (0 < n < 100): "))
x = []
for i in range(n):
    val = float(input(f"Nhập x{i+1}: "))
    x.append(val)

tong = 0
dem = 0
for val in x:
    if 0 < val < 1000:
        tong += val
        dem += 1

if dem > 0:
    print(f"Trung bình cộng: {tong / dem:.2f}")
else:
    print("Không có phần tử nào thỏa mãn.")