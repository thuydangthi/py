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

### Truy cập các phần tử của List
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

    my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

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
Method append() thêm một item vào cuối list. Ví dụ:

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

#### \+
Cách dễ nhất là dùng toán từ +, ví dụ:

    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

### Sửa giá trị item trong list
Chúng ta có thể thay đổi giá trị của một item trong list.
Cùng xem xét ví dụ sau:

    languages = ['Python', 'Swift', 'C++']

    # changing the third item to 'C'
    languages[2] = 'C'

    print(languages)  # ['Python', 'Swift', 'C']

### Xóa Item khỏi List
Đôi khi chung ta cần xoa một item ra khỏi một list. Python cung cấp một số method sau:

#### del
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

#### clear()

Method clear cho phép làm rỗng một list. Ví dụ:

    fruits = ["apple", "banana", "cherry"]
    fruits.clear()
    print(fruits)

### Python List Methods
Để tìm hiểu thêm về các method của list trong python, chúng ta có thể đọc thêm ở tài liệu của python.
### Lặp qua một list
Chúng ta có thể sử dụng vòng lặp for để duyệt qua các phần tử của list. Ví dụ:

    languages = ['Python', 'Swift', 'C++']

    # iterating through the list
    for language in languages:
        print(language)

### Kiểm tra một item có tồn tại trong list
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
### Sao chép một list
Chúng ta không thể sao chép một list bằng cách viết `list2 = list1`, bởi vì list2 sẽ là một tham chiếu lên list1, nếu list1 thay đổi thì list2 cũng tự động thay đổi theo và ngược lại.

Ví dụ:

    foods = ["apple", "banana", "cherry"]
    new_foods = foods

    foods[1] = "cherry"
    print(new_foods)

    new_foods.pop()
    print(foods)

Có nhiều cách để tạo một bản sao, một trong số đó là sử dụng method được tích hợp sẵn trong python list là method `copy()`.

Ví dụ:

    foods = ["apple", "banana", "cherry"]

    new_foods = foods.copy()
    print(new_foods)

    foods[1] = "cherry"
    print(new_foods)

    new_foods.pop()
    print(foods)

Hoặc chúng ta cũng có thể sử dụng chính method `list()` như sau:

    foods = ["apple", "banana", "cherry"]

    new_foods = list(foods)
    print(new_foods)

    foods[1] = "cherry"
    print(new_foods)

    new_foods.pop()
    print(foods)

### Sắp xếp list
Các list object có method sort(), dùng để sắp xếp list theo thứ tự chữ và số.

Ví dụ sắp xếp danh sách theo thứ tự bảng chữ cái:

    fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

    fruits.sort()
    print(fruits)

Ví dụ sắp xếp danh sách theo thứ tự số:

    nums = [100, 50, 65, 82, 23]

    nums.sort()
    print(nums)

python không hỗ trỡ sắp xếp giữa int và string, vì vậy chương trình sẽ báo lỗi nếu chúng ta cố gắng làm như sau:

    # an error program
    nums = ["0", 100, "1", 50, 65, 82, 23]

    nums.sort()
    print(nums)

#### reverse

Để sắp xếp giảm dần, chúng ta dùng keyword argument reverse = True:
Để sắp xếp tăng dần, chúng ta dùng keyword argument reverse = False hoặc không truyền reverse:
Ví dụ:

    fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
    fruits.sort(reverse = True)
    print(fruits)

    nums = [100, 50, 65, 82, 23]
    nums.sort(reverse = True)
    print(nums)

    nums.sort(reverse = False)
    print(nums)
#### Tùy chỉnh chức năng sắp xếp
Chúng ta có thể tùy chỉnh chức năng `sort` bằng cách sử dụng keyword argument key = function. Trong đó function sẽ trả về một số mà sẽ được dùng để sắp xếp list.

Ví dụ sắp xếp danh sách dựa trên mức độ gần của số đó với 50:

    def myfunc(n):
        return abs(n - 50)

    nums = [100, 50, 65, 82, 23]
    nums.sort(key = myfunc)
    print(nums)

Ví dụ sắp xếp danh sách dựa trên mức độ xa của số đó với 50:

    def myfunc(n):
        return abs(n - 50)

    nums = [100, 50, 65, 82, 23]
    nums.sort(key = myfunc, reverse=True)
    print(nums)

Chúng ta có thể sử dụng hàm lambda tại đây:

    nums = [100, 50, 65, 82, 23]

    nums.sort(key = lambda n: abs(n - 50))
    print(nums)

## Python Tuple
Tuple là một bộ dữ liệu dùng để lưu nhiều item trong một biến.
Tuple là một trong 4 loại dữ liệu được tích hợp trong python để lưu trữ tập các dữ liệu. 3 loại còn lại là list, set, dictionary.

Một tuple là một bộ lưu các giá trị, được sắp xếp và không thể thay đổi.
### Tạo Tuple
Tuple được viết với dấu ngoặc tròn. Ví dụ:

    fruits = ("banana", "apple", "cherry")
    print(fruits)
#### Tuple Items
Các items trong một Tuple được sắp xếp theo thứ tự các phần tử khi khai báo, không thể thay đổi và cho phép các giá trị trùng lặp.

- Sắp xếp có thứ tự có nghĩa là các item có thứ tự xác định và thứ tự đó sẽ không thay đổi.
- Sắp xếp không có thứ tự có nghĩa là các item không có thứ tự xác định, chúng ta không thể tham chiếu đến một item bằng cách sử dụng index.
#### Tuple index
Các items trong Tuple được lập chỉ mục index, item đầu tiên có index [0], item thứ hai có index [1], v.v.

Chúng ta có thể truy cập vào một item trong tuple bằng index như sau:

    fruits = ("banana", "apple", "cherry")
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])

#### Cho phép trùng lặp
Các item trong một tuple có thể trùng nhau. Ví dụ:

    fruits = ("apple", "banana", "cherry", "apple", "cherry")
    print(fruits)

#### Chiều dài tuple
Để xác định một tuple có bao nhiêu item, chúng ta có thể sử dụng hàm len():

    fruits = ("apple", "banana", "cherry", "apple", "cherry")
    print(len(fruits))

#### Tạo Tuple chỉ với một item
Để tạo một bộ chỉ có một item, chúng ta phải thêm dấu phẩy sau item đó, nếu không Python sẽ không nhận ra nó là một Tuple.

Ví dụ:

    fruits = ("apple",)
    print(fruits)
    print(type(fruits))

    # NOT a tuple
    fruits = ("apple")
    print(fruits)
    print(type(fruits))

Output:

    ('apple',)
    <class 'tuple'>
    apple
    <class 'str'>

#### type()
Chúng ta có thể sử dụng hàm type để kiểm tra một giá trị hay biến có phải tuple không.

Ví dụ:

    fruits = ("apple", "banana", "cherry")
    print(type(fruits))

#### Tuple Items - Data Types
Tuple Items có thể có bất kỳ kiểu dữ liệu nào, ví dụ:

    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)

    print(type(tuple1), tuple1)
    print(type(tuple2), tuple2)
    print(type(tuple3), tuple3)

#### Tạo tuple bằng tuple()
Cũng có thể sử dụng hàm tạo tuple() để tạo một tuple.

    fruits = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(fruits)
### Cập nhật tuple
Chúng ta không thể thêm, sửa, xóa item trong tuple, ví dụ không thể làm như sau:

    tuple1 = ("apple", "banana", "cherry")
    print(tuple1)
    tuple1[0] = "cherry"

Output:

    ('apple', 'banana', 'cherry')
    Traceback (most recent call last):
    File "F:\GS\py\tuple8.py", line 3, in <module>
        tuple1[0] = "cherry"
        ~~~~~~^^^
    TypeError: 'tuple' object does not support item assignment

Hoặc:

    tuple1 = ("apple", "banana", "cherry")
    print(tuple1)
    del tuple1[0]

Output:

    ('apple', 'banana', 'cherry')
    Traceback (most recent call last):
    File "F:\GS\py\tuple9.py", line 3, in <module>
        del tuple1[0]
            ~~~~~~^^^
    TypeError: 'tuple' object doesn't support item deletion

Chúng ta có một số giải pháp như: chuyển tuple thành list để update item sau đó chuyển lại thành tuple, hoặc định nghĩa lại tuple.

Chúng ta không thể xóa một item trong một tuple nhưng có thể xóa cả tuple như sau:

    tuple1 = ("apple", "banana", "cherry")
    print(tuple1)
    del tuple1
    print(tuple1)

Output:

    ('apple', 'banana', 'cherry')
    Traceback (most recent call last):
    File "F:\GS\py\tuple10.py", line 4, in <module>
        print(tuple1)
            ^^^^^^
    NameError: name 'tuple1' is not defined. Did you mean: 'tuple'?
### Lặp qua tuple
Chúng ta có thể lặp qua một tuple bằng cách dùng vòng lặp for.

Ví dụ:

    fruits = ("apple", "banana", "cherry")
    for x in fruits:
        print(x)

Hoặc:

    fruits = ("apple", "banana", "cherry")
    for i in range(len(fruits)):
        print(fruits[i])

Hoặc:

    thistuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(thistuple):
        print(thistuple[i])
        i = i + 1

### Nối các tuple
Chúng ta có thể nối 2 hoặc nhiều tuple với nhau bằng cách dùng toán tử `+`.

Ví dụ:

    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)

    tuple3 = tuple1 + tuple2
    print(tuple3)

Hoặc chúng ta cũng có thể làm như sau:

    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2

    print(mytuple)

## Python Dictionary
Dictionary được dùng để lưu trữ dữ liệu theo cặp và được sắp xếp. Một cặp thì gồm 2 thành phần là: `key` và `value`.
Các cặp trong một dictionary không thể trùng `key`.
Giả sử chúng ta cần lưu danh sách các Quốc Gia với thủ đô của họ, dữ liệu trông như sau:

Keys | Values
--- | --- 
Viet Nam | Ha Noi 
Italy | Rome
England | London

### Tạo một dict
Chúng ta có thể tạo một dict theo 2 cách như sau:

    capital_city = {
        "Viet Nam": "Ha Noi",
        "Italy": "Rome",
        "England": "London"
    }
    print(capital_city)

Hoặc:

    profile = dict(name = "John", age = 36, country = "Norway")
    print(profile)

Trong ví dụ trên, chúng ta đã tạo một dict, có các keys là: "Viet Nam", "Italy", "England" với các values tương ứng là: "Ha Noi", "Rome", "London".

Ở ví dụ trên, các key và value có dữ liệu dạng chuỗi, chúng ta cũng có thể tạo dict với key và value ở các dạng dữ liệu khác.

Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }
    print(car)

__Dictionary item__: Mỗi một cặp key:value trong một dictionary được gọi là 1 item, các item này được sắp xếp theo thứ tự, có thể thay đổi và không cho phép trùng lặp key giữa các item.

Kể từ phiên bản Python 3.7, dictionary được __sắp xếp theo thứ tự__. Trong Python 3.6 trở về trước, dictionary không có thứ tự.
- Sắp xếp có thứ tự có nghĩa là các item có thứ tự xác định và thứ tự đó sẽ không thay đổi.
- Sắp xếp không có thứ tự có nghĩa là các item không có thứ tự xác định, chúng ta không thể tham chiếu đến một item bằng cách sử dụng index.

__Có thể thay đổi__: nghĩa là chúng ta có thể thêm bớt các item hoặc sửa một item trong một dictionary.

__Các item trong một dict không thể trùng key__: 
Xem xét ví dụ sau:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "year": 2020
    }
    print(car)
Output:

    {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

Giá trị của key "year" sẽ là 2020, là giá trị cuối cùng được ghi trong câu lệnh khai báo dict.

Các item trong dict có thể thuộc bất kỳ kiểu dữ liệu nào.
Chúng ta có thể dùng hàm `type()` để kiểm tra một biến có phải là một dict không như sau:

    type(car)

Chúng ta có thể dùng hàm `len()` để kiểm tra số item, hay số cặp key:value của một dict:

    len(car)

Ngoài ra, chúng ta có thể tạo một dict rỗng như sau:

    car = {}

Hoặc:

    car = dict()

### Truy cập dictionary items
#### Truy cập dictionary items
Chúng ta có thể truy cập các item của một dict bằng cách truy cập tới key của chúng.

Ví dụ lấy giá trị thông tin model của car:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car["model"]

Ở đây python cũng cung cấp một method gọi là get() với tính năng tương tự, ví dụ:

    x = car.get("model")

#### Danh sách keys
Python cung cấp method keys, dùng để trả về về danh sách tất cả các keys trong các items của một dictionary.

Ví dụ:

    x = car.keys()

Danh sách key là một dạng view của dict, nghĩa là bất kỳ thay đổi nào được thực hiện trong dict sẽ được thay đổi trong keys.

Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.keys()

    print(x) # before the change

    car["color"] = "white"

    print(x) # after the change

#### Danh sách values
Python cung cấp method values, dùng để trả về về danh sách tất cả các values trong các items của một dictionary.

Ví dụ:

    x = car.values()

Danh sách values là một dạng view của dict, nghĩa là bất kỳ thay đổi nào được thực hiện trong dict sẽ được thay đổi trong values.

Ví dụ thay đổi value của 1 item trong dict và kiểm tra lại danh sách value:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.values()

    print(x) # before the change

    car["year"] = 2020

    print(x) # after the change

Ví dụ thêm mới một item vào dict và kiểm tra lại danh sách value:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.values()

    print(x) # before the change

    car["color"] = "red"

    print(x) # after the change
#### Danh sách items
Python cung cấp method items, dùng để trả về về danh sách tất cả các items trong các items của một dictionary dưới dạng danh sách các tuples.

Ví dụ:

    x = car.items()

Danh sách items là một dạng view của dict, nghĩa là bất kỳ thay đổi nào được thực hiện trong dict sẽ được thay đổi trong items.

Ví dụ thay đổi 1 item trong dict và kiểm tra lại danh sách item:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.items()

    print(x) # before the change

    car["year"] = 2020

    print(x) # after the change

Ví dụ về việc thêm một item trong dict và kiểm tra lại danh sách item:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.items()

    print(x) # before the change

    car["color"] = "red"

    print(x) # after the change

#### Kiểm tra key có tồn tại không
Để kiểm tra một key có tồn tại trong một dict không, chúng ta dùng toán từ `in`:

Ví dụ kiểm tra xem dict có item nào có key là `model` không:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    if "model" in car:
        print("Yes, 'model' is one of the keys in the car dictionary")
### Thay đổi item của dict
Chúng ta có thể thay đổi giá trị của một item bằng cách refer tới key của nó.

Ví dụ về việc đổi year của car thành 2023:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(car["year"]) # before change
    car["year"] = 2018
    print(car["year"]) # after change

Ngoài ra python còn cung cấp method `update` để cập nhật một dict theo đối số truyền vào. Đối số phải là một dict hoặc là một object có thể lặp với các cặp key:value.

Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car.update({"color": "White"})

    print(car)

    new_info = {
        "year": 2022
    }

    car.update(new_info)

    print(car)
### Thêm items
Chúng ta có thể thêm items vào một dict.
Chúng ta có thể thêm item vào dict bằng cách sử dụng các key và gán giá trị cho chúng.

Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    car["color"] = "red"
    print(car)

Hoặc sử dụng method `update()` để thêm nhiều item một lúc, ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    car.update({"color": "red"})

### Xóa items
Chúng ta có thể xóa các items khỏi một dict. Python cung cấp một số phương pháp như sau:

#### pop()
Method pop() nhận vào đối số là key của item cần xóa, sau đó trả ra item và thực hiện xóa item khỏi dict. Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car_model = car.pop("model")
    print(car)
    print(car_model)

Chúng ta có thể lấy giá trị method pop trả ra để gán vào biến và sử dụng sau đó, hoặc chỉ thực hiện pop thông thường như sau:

    car.pop("model")

Việc cố găng truyền vào method pop một key không còn tồn tại trong item sẽ gây lỗi.

#### popitem()
Method popitem() sẽ xóa item cuối cùng của dict và trả ra item đã bị xóa.

Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.popitem()
    print(car)
    print(x)

Chúng ta có thể lấy giá trị method popitem trả ra để gán vào biến và sử dụng sau đó, hoặc chỉ thực hiện popitem thông thường như sau:

    car.popitem()

Không thể thực hiện xoa item cuối cùng của một dict rỗng. Ví dụ:

    # an error program

    my_dict = {}
    my_dict.popitem()

#### del
Từ khóa del được dùng để xóa một item với key cho trước, ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    del car["model"]
    print(car)

Hoặc cũng có thể dùng để xóa luôn dict, ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print(car)
    del car
    print(car)

Ouput:

    {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Traceback (most recent call last):
    File "F:\GS\py\source\04\dict22.py", line 9, in <module>
        print(car)
            ^^^
    NameError: name 'car' is not defined. Did you mean: 'chr'?

#### clear()
Method clear() được dùng khiến cho một dict trở thành empty.
Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print(car)
    car.clear()
    print(car)

Output:

    {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    {}

### Lặp qua dict

Chúng ta có thể lặp qua một dict bằng cách sử dụng vòng lặp `for`.
Khi lặp qua dict một cách thông thường thì giá trị được trả về là danh sách các key của dict đó. Ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    for x in car:
        print(x)

Output:

    brand
    model
    year

Khi đó để in ra value tương ứng, chúng ta có thể làm như sau:

    for x in car:
        print(x)
        print(car[x])

Ouput:

    brand
    Ford
    model
    Mustang
    year
    1964

Hoặc chúng ta có thể sử dụng method keys hoặc values để lặp qua danh sách key hoặc danh sách value của dict, ví dụ:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print("Iterate over the values list")
    for x in car.values():
        print(x)

    print("\nIterate over the keys list")
    for x in car.keys():
        print(x)

Chúng ta cũng có thể lặp qua các cặp key và value bằng cách sử dụng method items:

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    for k, v in car.items():
        print(k, v)
### Sao chép một dict
Chúng ta không thể sao chép một dict bằng cách viết `dict2 = dict1`, bởi vì dict2 sẽ là một tham chiếu lên dict1, nếu dict1 thay đổi thì dict2 cũng tự động thay đổi theo và ngược lại.

Ví dụ:

    car1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car2 = car1

    car1["year"] = 2022

    print(car2["year"])

    car2["color"] = "black"

    print(car1["color"])

Vì vậy hãy cần thận khi viết `dict2 = dict1`, trừ phi bạn chủ động muốn có sự tham chiếu đó.

Có nhiều cách để tạo một bản sao mà không tham chiều tới bản chính, một trong số đó là sử dụng method `copy()` được tích hợp sẵn vào dictionary.

Ví dụ:

    car1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    car2 = car1.copy()
    print(car2)

    car1["year"] = 2022
    print(car2["year"])

    car2["color"] = "black"
    print(car1["color"]) # error KeyError: 'color'

Một cách khác để tạo bản sao là sử dụng chức năng có sẵn `dict()`, ví dụ:

    car1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    car2 = dict(car1)
    print(car2)

    car1["year"] = 2022
    print(car2["year"])

    car2["color"] = "black"
    print(car1["color"]) # error KeyError: 'color'

## Python Sets
## Python Strings

## Python Boolean
## Pythonic
