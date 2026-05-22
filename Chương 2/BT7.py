n = int(input("nhap so phan tu cua day so:"))


for i in range(1, n + 1):
    k = int(input("nhap phan tu thu " + str(i) + ":"))
    danh_sach.append(k) 
tong = 0 
for i in danh_sach:
    tong = tong + i

print("tong cua day so la: " + str(tong)) 