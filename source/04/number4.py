from decimal import * # lấy toàn bộ nội dung của thư viện Decimal

getcontext().prec = 6
print(Decimal(1) / Decimal(7))  # lấy tối đa 6 chữ số phần thập phân Decimal

getcontext().prec = 28
print(Decimal(1) / Decimal(7))  # lấy tối đa 28 chữ số phần thập phân Decimal
