m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
if m <= 0 or n <= 0:
    print("m và n phải là số nguyên dương")
else:
    tong_chu_so_n = sum(int(ch) for ch in str(n))
    if tong_chu_so_n == 0:
        print("Tổng các chữ số của n bằng 0, không thể chia")
    elif m % tong_chu_so_n == 0:
        print(f"{m} chia hết cho {tong_chu_so_n}")
    else:
        print(f"{m} không chia hết cho {tong_chu_so_n}")