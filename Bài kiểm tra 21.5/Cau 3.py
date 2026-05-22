n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương")
else:
    tich = 1
    for ch in str(n):
        tich *= int(ch)

    if tich % 2 == 0 and tich > 20:
        print(f"Tích các chữ số ({tich}) là số chẵn và lớn hơn 20")
    else:
        print(f"Tích các chữ số ({tich}) không thỏa mãn")