n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương")
else:
    tong = sum(int(ch) for ch in str(n))
    if tong % 3 == 0:
        print(f"Tổng các chữ số ({tong}) chia hết cho 3")
    else:
        print(f"Tổng các chữ số ({tong}) không chia hết cho 3")