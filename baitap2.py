# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:46:49 2024

@author: thuynhi_20033961
"""

# Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích,
#thương, chia lấy dư, chia lấy nguyên của 2 số trên và in kết quả ra màn 
#hình. Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm (ví dụ kết quả 3.333333 thì làm tròn 3.333).
import math
a = float(input(" Nhập số nguyên a:"))
b = float(input(" Nhập số nguyên b:"))
Tong = a + b
print(" Tổng hai số: =", Tong)
Hieu = a - b
print(" Hiệu hai số: =", Hieu)
Tich = a * b
print(" Tích hai số:=",Tich)
Thuong = a/b
print(" Thương hai số: =", Thuong)
Phandu = math.fmod(a,b)
print("Chia dư : =", Phandu)
Chia = a//b
print("Chia nguyên: =", Chia)
