n = int(input("nhập n:"))
dem = 0
i = 2

while n > 1:
    if n % i == 0:
        # i là ước số nguyên tố
        dem = dem + 1
        # chia hết n cho i đến khi không chia được nữa
        while n % i == 0:
            n = n // i  
    i = i + 1

print(f"Số lượng ước số nguyên tố của là:", dem)
