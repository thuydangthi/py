# Chuyển đổi kiểu dữ liệu trong python
## Kiểm tra kiểu dữ liệu của biến
Khác với các ngôn ngữ lập trình khác, khi khai báo biến phải khai báo rõ ràng kiểu dữ liệu. Trong python việc đó không cần thiết mà python sẽ tự biết bằng cách xác định từ kiểu dữ liệu được gán cho biến. Vì vậy để kiểu tra kiểu dữ liệu của một biến, hay giá trị chúng ta dùng hàm `type()`.

Cú pháp:

    type(ten bien)
    hoặc
    type(value)

Ví dụ:

    >>> x = 1
    >>> type(x)
    <class 'int'>
    >>> y = 2/3
    >>> type(value)
    <class 'float'>
    >>> type("hi")
    <class 'str'>
    >>>
## Chuyển đổi kiểu dữ liệu
Trong lập trình, chuyển đổi kiểu dữ liệu là quá trình chuyển đổi dữ liệu từ kiểu này sang kiểu khác.
Ví dụ: chuyển dữ liệu từ `integer` sang `string`.
Có hai loại chuyển đổi:
- Chuyển đổi ngầm định - chuyển đổi tự động
- Chuyển đổi rõ ràng - chuyển đổi thủ công
### Chuyển đổi ngầm định Implicit Conversion
Là kiểu chuyển đổi kiểu dữ liệu do python tự động thực hiện trong một số trường hợp nhất định. Việc này diễn ra trong quá trình biên dịch hoặc trong thời gian chạy. Python tự thực hiện việc này, vì vậy chúng ta không cần phải thực hiện việc chuyển đổi một cách tường minh.

Ví dụ: Chuyển đối số int sang số float

    integer_number = 123
    float_number = 1.23

    new_number = integer_number + float_number

    # display new value and resulting data type
    print("Value:", new_number)
    print("Data Type:", type(new_number))

Ví dụ vừa rồi chúng ta đã tạo hai biến kiểu dữ liệu integer và float và sau đó cộng chúng lại. Chúng ta cũng đã tạo một biến tên là `new_number` và lưu trữ kết quả của phép cộng vào biến đó. Khi kiểm tra kiểu dữ liệu của biến `new_number`, chúng ta có thể thấy rằng kiểu dữ liệu của biến `new_number` đã được trình biên dịch Python tự động chuyển thành kiểu dữ liệu float. Quá trình này được gọi là chuyển đổi kiểu ẩn.
Lý do mà biến `new_number` được chuyển đổi thành kiểu dữ liệu float chứ không phải kiểu dữ liệu int là vì nếu trình biên dịch chuyển đổi Thành kiểu dữ liệu int, thì nó sẽ phải loại bỏ phần đằng sau dấu phẩy và khi đó sẽ gây mất mát dữ liệu. Vì vậy, Python luôn chuyển đổi kiểu dữ liệu nhỏ hơn thành kiểu dữ liệu lớn hơn để tránh mất dữ liệu.

<strong>Chú ý: </strong>
- Nếu chúng ta cố gắng cộng giữa `string` và `int` thì lỗi `TypeError` sẽ được trả ra, ví dụ là `'12' + 34`. Python không thể thực hiện chuyển đổi ngầm định trong các trường hợp này.

    Ví dụ:

        a = 100
        b = "200"
        result1 = a + b
        print(result1)
    
        Traceback (most recent call last):
        File "F:\GS\py\source\01\convert2.py", line 3, in <module>
            result1 = a + b
        TypeError: unsupported operand type(s) for +: 'int' and  'str'

- Khi này chúng ta có một giải pháp là Chuyển đổi rõ ràng

### Chuyển đổi rõ ràng Explicit Conversion
Chuyển đổi kiểu rõ ràng là việc người lập trình chủ động định nghĩa rõ ràng kiểu dữ liệu mà người dùng muốn chuyển đổi thành.
Chuyển đổi kiểu rõ ràng còn được gọi là typecasting. 

Cú pháp:

    required_data type(expression)
Python cung cấp các hàm được dựng sẵn để thực hiện việc chuyển đổi kiểu như sau:

Function | Description 
--- | ---
int(value, base) | Hàm chuyển đổi giá trị được chỉ định thành một số nguyên, base là số nguyên tùy chọn, dùng để chỉ định cơ số
float(value) | Hàm chuyển đổi giá trị được chỉ định thành số float
complex(real, imag) | hàm dùng để tạo số phức
str(value) | hàm chuyển đổi giá trị được chỉ định thành một string
tuple(value) | hàm chuyển đổi giá trị được chỉ định thành một tuple
list(value) | hàm chuyển đổi giá trị được chỉ định thành một list
set(value) | hàm chuyển đổi giá trị được chỉ định thành một list
dict(value) | hàm chuyển đổi giá trị được chỉ định thành dictionary, y nên là một bộ dữ liệu dạng tuple gồm (key, value)
ord(value) | hàm chuyển đổi một character thành một số int
hex(value) | hàm chuyển đổi một int thành một chuỗi thập lục phân
oct(value) | hàm chuyển đổi một int thành một chuỗi bát phân

Xem qua một số ví dụ sau:
Ví dụ 1:

    # Adding string and integer data types using explicit type conversion

    a = 100
    b = "200"
    b = int(b)
    result1 = a + b
    print(result1) # 300

Ví dụ 2:

    # Adding string and integer data types using explicit type conversion

    a = 100
    b = "200"
    a = str(a)
    result1 = a + b
    print(result1) # 100200

<strong>Một số lưu ý: </strong>
- Chuyển đổi ngầm định được thực hiện bởi trình thông dịch Python.
- Chuyển đổi rõ ràng được thực hiện bởi người lập trình bằng cách sử dụng rõ ràng các function được dựng sẵn bởi Python.
- Khi python thực hiện chuyển đổi ngầm định, sẽ đồng thời giảm việc thất thoát dữ liệu.
- Khi thực hiện chuyển đổi rõ ràng, phải chú ý tới rủi ro làm thất thoát dữ liệu.

# Python I/O

## Đầu ra Output
Python cung cấp hàm `print()` để in đầu ra.

Ví dụ:

    print('Good morning')

Cú pháp:

    print(value(s), sep= ' ', end = '\n', file=file, flush=flush)
Trong đó, các parameters dùng để:
- value(s): Các giá trị sẽ được in, không giới hạn giá trị, các giá trị này sẽ được chuyển thành string để in
- sep='separator': Optional, default là ' ', nó dùng để chỉ định cách để phân tách các đối tượng khi có nhiều hơn 1 đối tượng.
- end='end': Optional, default là '\n' (một dòng mới ở cuối), chỉ định cách kết thúc chuỗi được in, có thể là một dòng mới '\n' hay là một tab '\t'.
- file: Optional, default là sys.stdout (màn hình), chỉ định nơi các giá trị được in.
- flush: Optional, default là False, là một giá trị kiểu boolean, dùng để chỉ định đầu ra sẽ được xóa (True) hay được lưu vào bộ đệm (False)

Xem thêm các ví dụ dưới đây:

Ví dụ in ra nhiều object:

    print("Hello", "how are you?", 123)

Ví dụ in ra một list:

    print(["Hello", "how are you?", 123])
    
Ví dụ in ra nhiều object và phân cách giữa các object là `---`:

    print("Hello", "how are you?", sep="---")
    
Ví dụ in ra nhiều object và phân cách giữa các object là `---`, không tự động xuống dòng mới:

    print("Hello", "how are you?", sep="---", end="")
    print("I am doing good")

### Định dạng đầu ra Output formatting
Đôi khi chúng ta sẽ cần định dạng đầu ra của mình để làm code trông tường minh hơn. Chúng ta có một số cách sau:
#### Output formatting sử dụng operator %
Toán tử % có thể được dùng để định dạng chuỗi. Chúng ta cùng xem xét ví dụ sau:

    print("I am %d years old and %f meters tall" % (250, 1.9))

#### Output formatting sử dụng format method
format() method được dùng phổ biến từ python 2.6 để định dạng đầu ra của chuỗi, với phương pháp này chúng ta sử dụng `{}` để đánh dấu nơi mà object sẽ được thay thế (đặt) vào, sau đó, method format() sẽ trả về chuỗi đã được định dạng.

Cú pháp:

    string.format(value1, value2,...)

Ví dụ:

    x = 5
    y = 10

    print('The value of x is {} and y is {}'.format(x, y))

Hoặc chúng ta cũng có thể viết như sau:

    x = 5
    y = 10

    print(f'The value of x is {x} and y is {y}')

#### Output formatting sử dụng việc nối chuỗi

Chúng ta cũng có thể in chuỗi mà được nối bằng việc sử dụng toán tử, hãy xem xét các ví dụ sau:

Ví dụ in ra chuỗi được nối từ 2 chuỗi khác:

    print("Hello" + "how are you?")

Hoặc in 7 lần 1 chuỗi:

    print("Hello"*7)

Hoặc in tổng của 2 số:

    print(5 + 7)

Nhưng hãy nhớ, chúng ta không thể làm thế này:

    print("Hello" + "how are you?" + 1)

    Traceback (most recent call last):
    File output6.py", line 2, in <module>
        print("Hello" + "how are you?" + 1)
    TypeError: can only concatenate str (not "int") to str

## Đầu vào Input
Trong khi lập trình, đôi khi chúng ta có thể muốn lấy thông tin đầu vào từ người dùng. Trong Python, chúng ta có thể sử dụng hàm input().

Cú pháp:

    input(prompt)

Trong đó `prompt` là chuỗi chúng ta muốn hiển thị trên màn hình. Nó là optional.
Ví hàm input sẽ return giá trị người dùng đã nhập, vì vậy chúng ta có thể (thường) gán giá trị từ hàm này cho một biến để sử dụng sau đó. Hãy xem xét ví dụ sau:

    # using input() to take user input
    num = input('Enter a number: ')

    print('You Entered:', num)

    print('Data type of num:', type(num))

___Note:___ điều quan trọng cần lưu ý ở đây là giá trị hàm input trả ra là một string, vì vậy nếu muốn thực hiện tính toán với giá trị người dùng nhập vào, cầm chú ý đến kiểu dữ liệu và việc ép kiểu.

# Toán tử trong python
Trong Python, chúng ta có một tập hợp các ký hiệu đặc biệt thực hiện nhiều loại phép toán khác nhau như phép toán logic, phép toán, v.v. Những ký hiệu này được gọi là toán tử.
Cấu trúc của một phép toán:
- Toán tử
- Toán hạng: các giá trị mà được thực hiện bởi toán tử

Các loại toán tử:
- Toán tử số học
- Toán tử gán
- Toán tử so sánh
- Toán tử logic
- Toán tử Bitwise
- Toán tử đặc biệt
## Toán tử số học trong Python
Các toán tử số học được sử dụng để thực hiện các phép toán như cộng, trừ, nhân, v.v.
Ví dụ:

    sub = 10 - 5 # 5

Ở đây, `-` là một toán tử số học trừ hai giá trị hoặc biến.
Chúng ta có các toán tử số học sau: +, -, *, /, %, **, //
Hãy xem xét thêm ví dụ sau:

    a = 7
    b = 2

    # addition
    print ('Sum: ', a + b)  

    # subtraction
    print ('Subtraction: ', a - b)   

    # multiplication
    print ('Multiplication: ', a * b)  

    # division
    print ('Division: ', a / b) 

    # modulo
    print ('Modulo: ', a % b)  

    # a to the power b
    print ('Power: ', a ** b)
## Toán tử gán trong python
Toán tử gán được sử dụng để gán giá trị cho biến. Ví dụ:

    # assign 5 to x 
    x = 5
Ở đây, toán tử gán `=` đẫ gán giá trị 5 cho biến x.
Trong python chúng ta có các toán tử gán sau:
- =: Gán một giá trị từ toán hạng bên phải sang toán hạng bên trái.
- +=: Thực hiện phép cộng, và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- -=: Thực hiện phép trừ và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- *=: Thực hiện phép nhân và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- /=: Thực hiện phép chia và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- %=: Thực hiện phép chia lấy phần dư và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- **=: Thực hiện số mũ, và sau đó dùng kết quả tính được gán cho toán hạng bên trái.
- //=: Thực hiện phép chia lấy phần nguyên, và sau đó dùng kết quả tính được gán cho toán hạng bên trái.

Chúng ta cùng xem xét ví dụ sau:
    # assign 10 to a
    a = 10

    # assign 5 to b
    b = 5 

    # assign the sum of a and b to a
    a += b      # a = a + b

    print(a)

    # Output: 15

## Toán tử so sánh trong python
Toán tử so sánh dùng để so sánh hai giá trị/biến và trả về kết quả kiểu boolean: True hoặc False.
Ví dụ:

    a = 5
    b = 2

    print (a > b)

Trong python chúng ta có các toán tử so sánh như sau: ==, !=, <, >, <=, >=, <> (like !=)

Chúng ta xem xét thêm ví dụ sau:

    a = 5
    b = 2

    # equal to operator
    print('a == b =', a == b)

    # not equal to operator
    print('a != b =', a != b)

    # greater than operator
    print('a > b =', a > b)

    # less than operator
    print('a < b =', a < b)

    # greater than or equal to operator
    print('a >= b =', a >= b)

    # less than or equal to operator
    print('a <= b =', a <= b)

## Toán tử logic trong python
Các toán tử logic được sử dụng để kiểm tra xem một biểu thức có phải là True hay False không. Chúng thường được sử dụng trong việc ra quyết định trong biểu thực if else.
Ví dụ:

    a = 5
    b = 6

    print((a > 2) and (b >= 6))    # True

Ở đây chúng ta có toán tử and, đại diện cho logic and, tức nếu cả 2 điều này đồng thời xảy ra thì biểu thức là Đúng, ngược lại thì sai.
Trong python chúng ta có các toán tử logic sau: and, not, or
Chúng ta xem xét thêm ví dụ sau:

    # logical AND
    print(True and True)     # True
    print(True and False)    # False

    # logical OR
    print(True or False)     # True

    # logical NOT
    print(not True)          # False
## Toán tử Python Bitwise
Toán tử bitwise hành động trên toán hạng như thể chúng là chuỗi các chữ số nhị phân.
Ví dụ: 2 là 10 ở dạng nhị phân và 7 là 111 ở dạng nhị phân.
Trong python chúng ta có các toán tử Bitwise sau: &, |, -, ^, >>, <<
## Toán tử đặc biệt trong python
Ngôn ngữ Python cung cấp một số loại toán tử đặc biệt như toán tử identity và toán tử membership.
### Toán tử identity
Trong Python, `is` và `is not` được sử dụng để kiểm tra xem hai giá trị có giống nhau hay không.

- `is`: trả về True nếu các toán hạng giống nhau (tham chiếu đến cùng một đối tượng), ví dụ `x is True`
- `is not`: trả về True nếu các toán hạng không giống nhau (không đề cập đến cùng một đối tượng), ví dụ `x is not True`

Chúng ta cùng xem xét ví dụ sau:

    x1 = 5
    y1 = 5
    x2 = 'Hello'
    y2 = 'Hello'
    x3 = [1,2,3]
    y3 = [1,2,3]

    print(x1 is not y1)  # prints False

    print(x2 is y2)  # prints True

    print(x3 is y3)  # prints False
### Toán tử membership
Trong Python, `in` và `not in` là toán tử membership. Chúng được sử dụng để kiểm tra xem một giá trị hoặc biến có được tìm thấy (là thành viên/con) trong/của một chuỗi hay không (string , list , tuple , set và dictionary).
- `in`: trả về True nếu giá trị/biến được tìm thấy trong chuỗi, ví dụ `5 in x`
- `not in`: trả về True nếu giá trị/biến được không đươc tìm thấy trong chuỗi, ví dụ `5 not in x`

Chúng ta cùng xem xét ví dụ sau:

    message = 'Hello world'
    dict1 = {1:'a', 2:'b'}

    # check if 'H' is present in message string
    print('H' in message)  # prints True

    # check if 'hello' is present in message string
    print('hello' not in message)  # prints True

    # check if '1' key is present in dict1
    print(1 in dict1)  # prints True

    # check if 'a' key is present in dict1
    print('a' in dict1)  # prints False

# Luồng if else trong python
Trong python, chúng ta sử dụng câu lệnh if, else để thực hiện biểu thức điều kiện.
Chúng ta có các dạng viết câu lệnh điều kiện như sau: if, else và elif
## Câu lệnh if
Cú pháp của câu lệnh if trong Python là:

    if condition:
        # body of if statement

- Nếu condition là đúng, thì đoạn mã bên dưới câu lệnh if được thực thi
- Nếu condition là sai, thì đoạn mã bên dưới câu lệnh if KHÔNG được thực thi

Ví dụ:

    number = 10

    # check if number is greater than 0
    if number > 0:
        print('Number is positive.')

    print('Here')

Bây giờ hãy thử đổi giá trị của number thành 0 và chạy lại chương trình, chúng ta sẽ thấy nó chỉ in ra `Here`.

## Câu lệnh else
Chúng ta cùng xem xét ví dụ sau khi chúng ta muốn in ra màn hình là "Negative number" nếu giá trị của number là một số không dương:

    number = 10

    if number > 0:
        print('Positive number')

    else:
        print('Negative number')

    print('This statement is always executed')
Ở đây chúng ta thêm câu lệnh `else`, có nghĩa là nếu điều kiện ở if không đúng, thì mặc định một cách tự động là chương trình sẽ chạy khối code ở dưới `else`.

## Câu lệnh elif
Bây giờ chúng ta muốn nâng cấp bài toán bên trên lên bằng cách, nếu số không lớn hơn 0 và bằng 0 thì in ra màn hình là "Zero.
Hãy xem xét ví dụ sau:

    number = 0

    if number > 0:
        print("Positive number")

    elif number == 0:
        print('Zero')
    else:
        print('Negative number')

    print('This statement is always executed')

## If lồng nhau
Chúng ta cũng có thể sử dụng các câu lệnh if lồng trong if như sau:
    
    # outer if statement
    if condition1:
        # statement(s)

        # inner if statement
        if condition2: 
            # statement(s)

Chúng ta cùng xem xét các ví dụ sau:

    number = 5

    # outer if statement
    if (number >= 0):
        # inner if statement
        if number == 0:
        print('Number is 0')
        
        # inner else statement
        else:
            print('Number is positive')

    # outer else statement
    else:
        print('Number is negative')

    # Output: Number is positive

Trong ví dụ trên, chúng ta sử dụng câu lệnh if lồng nhau để kiểm tra xem số đã cho là dương, âm hay bằng 0.

___Lưu ý:___ sử dụng if lồng nhau có thể khiến code chúng ta khó đọc hơn, vì vậy hãy chú ý khi sử dụng nó để tránh lách các logic cần thiết.
