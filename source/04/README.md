# Python Datatypes

## Python Numbers
### Python Numeric Data Type
Python hỗ trợ rất nhiều kiểu dữ liệu số.
Có ba loại số trong Python:
- int
- float (chính xác tới 15 chữ số thập phân)
- complex (số phức)

Các biến số được tạo khi chúng ta tạo biến và gán giá trị số cho chúng, ví dụ:

    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

Để xác định kiểu dữ liệu của một object trong python, chúng ta sử dụng hàm type():

    print(type(x))
    print(type(y))
    print(type(z))

### Hệ thống số

Những con số chúng ta xử lý hàng ngày thuộc hệ thống số thập phân (cơ số 10).

Nhưng các lập trình viên máy tính đôi khi cần làm việc với các hệ thống số khác như hệ thống số nhị phân (cơ số 2), thập lục phân (cơ số 16) và bát phân (cơ số 8).

Trong Python, chúng ta có thể biểu diễn các số này bằng cách đặt một tiền tố thích hợp trước số đó. Các tiền tố tương ứng như sau:

- Nhị phân: 0b hoặc 0B
- Bát phân: 0o hoặc 00
- Thập lục phân: 0x hoặc 0X

Xem xét ví dụ dưới đây:

    print(0b1101011)  # prints 107

    print(0xFB + 0b10)  # prints 253

    print(0o15)  # prints 13

### Số nguyên
Số nguyên bao gồm các số nguyên dương (1, 2, 3,...), các số nguyên âm (-1, -2, -3,...) và số 0.

Hãy xem xét ví dụ sau:

    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))
    print(type(y))
    print(type(z))

Trong Python 3.X, kiểu dữ liệu số nguyên là vô hạn. Điều này cho phép chúng ta tính toán với những số cực kì lớn.
### Float
Float, là một số dương hoặc âm, chứa một hoặc nhiều số sau dấu thập phân.

Ví dụ:

    x = 1.10
    y = 1.0
    z = -35.59

    print(type(x))
    print(type(y))
    print(type(z))

Lưu ý: Thường khi chúng ta viết số thực, phần nguyên và phần thập phân được tách nhau bởi dấu phẩy ( , ). Thế nhưng trong Python, dấu phẩy ( , ) này được thay thế thành dấu chấm ( . ).

Số float trong python có độ chính xác là 15 chữ số thập phân, nên nếu muốn độ chính xác cao hơn, chúng ta có thể sử dụng Decimal.

Ví dụ:

    from decimal import * # lấy toàn bộ nội dung của thư viện Decimal

    getcontext().prec = 6
    print(Decimal(1) / Decimal(7))  # lấy tối đa 6 chữ số phần thập phân Decimal

    getcontext().prec = 28
    print(Decimal(1) / Decimal(7))  # lấy tối đa 28 chữ số phần thập phân Decimal

Tuy Decimal có độ chính xác cao hơn so với float tuy nhiên nó lại khá rườm rà so với float. Do đó, cần cân bằng sự tiện lợi và chính xác để chọn kiểu dữ liệu phù hợp.

### Số phức
Số phức gồm 2 thành phần :

    <Phần thực> + <Phần ảo> j

Trong đó

- <Phần thực>, <Phần ảo> là số thực
- j là đơn vị ảo trong toán học với  j^2 = -1

Cách tạo số phức:
- Cách 1: tạo trực tiếp, ví dụ:

        x = 3+5j
        y = 5j
        z = -5j

        print(type(x))
        print(type(y))
        print(type(z))

- Cách 2: dùng hàm complex, ví dụ:

        x = complex(1, 2)
        print(x)
        print(type(x))

Cách truy cập vào phần thực của một số phức:

    <tên_biến>.real
Cách truy cập vào phần ảo của một số phức:

    <tên_biến>.imag

Ví dụ:

    x = complex(1, 2)
    print(x)
    print(type(x))
    print(x.real)
    print(x.imag)

### Python Random Module
Python không có hàm random() tạo số ngẫu nhiên, nhưng Python có một module tích hợp được gọi là `random` có thể được sử dụng để tạo số ngẫu nhiên:

Ví dụ
Import module `random` và hiển thị một số ngẫu nhiên trong khoảng từ 1 đến 9:

    import random

    print(random.randrange(1, 10))

Để tìm hiểu thêm về module random, hãy tìm hiểu trong tài liệu của python: https://docs.python.org/3/library/random.html

### Python Mathematics
Python cung cấp module math để thực hiện các phép toán khác nhau như lượng giác, logarit, xác suất và thống kê, v.v. Ví dụ:

    import math

    print(math.pi)

    print(math.cos(math.pi))

    print(math.exp(10))

    print(math.log10(1000))

    print(math.sinh(1))

    print(math.factorial(6))

Để tìm hiểu thêm về module math trong python, hãy đọc thêm tài liệu của python: https://docs.python.org/3/library/math.html
## Python List
Trong python, list là một tập hợp các dữ liệu có loại dữ liệu giống nhau hoặc khác nhau.
Giả sử chúng ta cần ghi tuổi của 5 học sinh. Thay vì tạo 5 biến riêng biệt, chúng ta chỉ cần tạo một list:
    
    [17, 18, 19, 20]

### Tạo một Python List
Một list trong Python được tạo bằng cách đặt các item bên trong dấu `[]`, và phân tách bằng dấu phẩy. Ví dụ:

    # A list with 3 integers
    numbers = [1, 2, 5]

    print(numbers)

    # Output: [1, 2, 5]

Một list cũng có thể có 0 hoặc nhiều item, các item có thể có các kiểu dữ liệu khác nhau. Ví dụ:

    # empty list
    my_list = []

    # list with mixed data types
    my_list = [1, "Hello", 3.4]

### Truy cập các phần tử của Python List
Một item trong một python được liên kết với một số chỉ mục (index) tương ứng. Vì vậy chúng ta có thể truy cập vào các phần tử của một list bằng cách sử dụng index.
Ví dụ:

    languages = ["Python", "Swift", "C++"]

    # access item at index 0
    print(languages[0])   # Python

    # access item at index 2
    print(languages[2])   # C++

Lưu ý: index luôn bắt đầu từ 0

### Index âm trong Python
Python cho phép có các index âm cho dữ liệu dạng chuỗi, mảng của nó. Trong đó index -1 tương ứng với phần tử cuối cùng, index -2 tương ứng với phần tử cuối thứ 2.
Ví dụ:

    languages = ["Python", "Swift", "C++"]

    # access item at index 0
    print(languages[-1])   # C++

    # access item at index 2
    print(languages[-3])   # Python

Lưu ý: Nếu index được chỉ định không tồn tại trong list, Python sẽ đưa ra exception IndexError.

### Cắt một Python List
Cắt list và việc chúng ta truy cập chỉ một phần của list. Để làm vậy chúng ta có thể sử dụng toán tử `:`. Ví dụ:

    # List slicing in Python

    my_list = ['p','r','o','g','r','a','m','i','z']

    # items from index 2 to index 4
    print(my_list[2:5])

    # items from index 5 to end
    print(my_list[5:])

    # items beginning to end
    print(my_list[:])

### Thêm phần tử vào Python List
Đôi khi chúng ta cũng cần thêm phần tử vào một list đã được tạo trước đó.
Python cung cấp một số method sau:
#### append()
Method append() thêm một mục vào cuối list. Ví dụ:

    numbers = [21, 34, 54, 12]

    print("Before Append:", numbers)

    # using append method
    numbers.append(32)

    print("After Append:", numbers)

#### extend()
Method extend() được dùng để thêm tất cả các item của list này vào một list khác.
Ví dụ:

    prime_numbers = [2, 3, 5]
    print("List1:", prime_numbers)

    even_numbers = [4, 6, 8]
    print("List2:", even_numbers)

    # join two lists
    prime_numbers.extend(even_numbers)

    print("List after append:", prime_numbers)

### Sửa giá trị item trong list
Chúng ta có thể thay đổi giá trị của một item trong list.
Cùng xem xét ví dụ sau:

    languages = ['Python', 'Swift', 'C++']

    # changing the third item to 'C'
    languages[2] = 'C'

    print(languages)  # ['Python', 'Swift', 'C']

### Xóa một Item khỏi một List
Đôi khi chung ta cần xoa một item ra khỏi một list. Python cung cấp một số method sau:

#### del()
Trong Python, chúng ta có thể sử dụng câu lệnh del để xóa một hoặc nhiều item khỏi list. Ví dụ:

    languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

    # deleting the second item
    del languages[1]
    print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

    # deleting the last item
    del languages[-1]
    print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

    # delete first two items
    del languages[0 : 2]  # ['C', 'Java', 'Rust']
    print(languages)
#### remove()
Chúng ta cũng có thể sử dụng method remove() để xóa một item khỏi list. Ví dụ:

    languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

    # remove 'Python' from the list
    languages.remove('Python')

    print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

#### pop()
Chúng ta có thể sử dụng method pop() để trả về và xóa một phần tử tại vị trí đã chỉ định.

Ví dụ:

    fruits = ['apple', 'banana', 'cherry']

    fruits.pop(1)

Lưu ý:
- Method pop trả về phần tử đã bị xóa.
- Nếu cố gắng truyền index không tồn tại thì chương trình sẽ báo lỗi IndexError.

### Python List Methods
Để tìm hiểu thêm về các method của list trong python, chúng ta có thể đọc thêm ở tài liệu của python.
### Lặp qua một list
Chúng ta có thể sử dụng vòng lặp for để duyệt qua các phần tử của list. Ví dụ:

    languages = ['Python', 'Swift', 'C++']

    # iterating through the list
    for language in languages:
        print(language)

### Kiểm tra xem một item có tồn tại trong list hay không
Chúng tôi có thể sử dụng từ khóa `in` để kiểm tra xem một item có tồn tại trong list hay không. Ví dụ:

    languages = ['Python', 'Swift', 'C++']

    print('C' in languages)    # False
    print('Python' in languages)    # True

### Python List Length
Trong Python, chúng ta có thể sử dụng method len() để tìm số phần tử có trong list. Ví dụ:

    languages = ['Python', 'Swift', 'C++']

    print("List: ", languages)

    print("Total Elements: ", len(languages))    # 3

### Python List Comprehension

Đây là cách ngắn gọn và đẹp mắt để tạo list trong python.
Hãy xem xét ví dụ sau:

    numbers = [number*number for number in range(1, 6)]

    print(numbers)    

    # Output: [1, 4, 9, 16, 25]

Đoạn mã trên tương đương với:

    numbers = []

    for x in range(1, 6):
        numbers.append(x * x)

## Python Tuple

## Python Strings

## Python Sets

## Python Dictionary
## Python Boolean
## Pythonic
