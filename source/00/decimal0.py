from decimal import * # lấy toàn bộ nội dung của thư viện Decimal

getcontext().prec = 6
Decimal(1) / Decimal(7)  # lấy tối đa 7 chữ số phần nguyên và phần thập phân Decimal

getcontext().prec = 28
Decimal(1) / Decimal(7)  # lấy tối đa 28 chữ số phần nguyên và phần thập phân Decimal
