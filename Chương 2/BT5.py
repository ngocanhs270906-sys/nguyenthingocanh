toan = float(input("nhập điểm toán:"))
ly = float(input("nhập điểm lý:"))
hoa = float(input("nhập điểm hóa:"))
diemtb = (toan+ly+hoa)/3
print ("diemtb:",diemtb)
if diemtb < 5 :
    print("sếp loại yếu")
elif diemtb < 7:
    print("sếp loại tb")
elif diemtb < 9:
    print("sếp loại khá")
else:
    print("sếp loại giỏi")