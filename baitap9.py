# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:32:00 2024

@author: DELL _ PC
"""
import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phantu1 = math. sqrt(a) - math.sqrt(b)
phanmau1 = 4* math. sqrt(a)- 4* math.sqrt(b)
phantu2 = math.sqrt(a) + (ab := math.sqrt(a * b)**0.25)
phanmau2 = 4* math.sqrt(a) + 4*math.sqrt(b)
B = (phantu1/phanmau1) - (phantu2/phanmau2)
if phanmau1 !=0 and phanmau2 !=0:
    print("Kết quả:=", B)
else:
    print("Mẫu số bằng 0, không thể thực hiện phép tính.")
