# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:52:44 2024

@author: thuynhi_20033961
"""

N = float(input(" Nhập vào số nguyên dương 2 chữ số:"))
if 10 <= N <= 99:
    hangdonvi= N % 10
    hangchuc= N // 10
Tonghaisonguyen = hangchuc + hangdonvi
print("Tổng số nguyên:=", Tonghaisonguyen)