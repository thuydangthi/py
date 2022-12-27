# Python Functions
Trong bài này, chúng ta sẽ tìm hiểu về hàm.
## Lập trình hướng cấu trúc
Ngày xưa khi lập trình mới bắt đầu, người ta lập trình toán tính (linear programming) viết các dòng code để chạy từ trên xuống dưới.
Sau này khi những vấn đề phát sinh như việc bảo trì, sửa đổi, tái sử dụng code phát sinh thì người ta đưa ra một kỹ thuật lập trình mới gọi là lập trình cấu trúc, hay còn gọi là lập trình hướng thủ tục (procedural programming).
Dù là ngôn ngữ hướng đối tượng, nhưng python vẫn cho phép người dùng lập trình theo phong cách lập trình hướng thủ tục.
Trong lập trình hướng thủ tục, khái niệm hàm rất quan trọng.

## Tổng quan về hàm

Hàm là gì?
Hàm là một khối mã dùng để thực hiện một tác vụ cụ thể.

Chúng ta đã sử dụng hàm trong python nhiều lần trong những bài trước, một trong số đó là hàm `print`, hàm dùng để in ra chuỗi.
Tương tự python, hàm `range` cũng là hàm được build-in, tức hàm dựng sẵn bởi python.
Ngoài việc sử dụng các hàm được dựng sẵn, chúng ta còn có thể tự tạo hàm cho mình.

Như vậy có các loại hàm nào?
- Standard library functions: hàm được tích hợp sẵn trong python và có sẵn để chúng ta sử dụng.
- User-defined functions: hàm được chúng ta tự tạo nên.

Tại sao sử dụng hàm?
Giả sử chúng ta cần viết một chương trình tính điểm của sinh viên và tìm ra danh sách sinh viên trượt môn, chúng ta sẽ có 2 hàm như sau:
- Hàm tính điểm cho từng sinh viên
- Hàm kiểm tra điểm đó có pass

Việc chia một vấn để lớn thành các vấn đề nhỏ giúp chương trình dễ hiểu và dễ tái sử dụng.

#### Khai báo hàm
Cú pháp để khai báo một hàm là gì?

    def function_name(arguments):
        # function body

Trong đó:
- def: là từ khóa dùng để khai báo hàm
- function_name: tên được dùng để đặt cho hàm
- arguments: những giá trị được truyền vào hàm
- Một hàm có thể return value hoặc không

Đôi khi chưa muốn define rõ ràng thân hàm viết gì, chúng ta có thể viết như sau:

    def greet():
        pass

Ở đây lệnh `pass` là một lệnh "giữ chỗ" (placeholder statement) để giúp cho các block của Python không bị thiếu câu lệnh trong trường chúng ta chưa biết viết gì cho phù hợp.

Hoặc nếu đã có ý tưởng về nó, đây là một ví dụ cho thân hàm:

    def greet():
        print('Hello World!')

Ở đây chúng ta có hàm tên là `greet`. Hàm này không yêu cầu truyền đối số, cũng không trả ra giá trị gì. Nó thực hiện việc in ra màn hình `Hello World!` khi hàm được gọi.

Vậy làm sao để gọi hàm trong python?

#### Cách gọi hàm trong python
Trước tiên chúng ta phải khai báo và định nghĩa hàm.
Ví dụ chúng ta có hàm sau:

    def greet():
        """function used to greet"""
        print('Hello World!')

Bây giờ để sử dụng chức năng này, chúng ta cần gọi nó như sau:

    # call the function
    greet()

Trong một đoạn mã đẩy đủ:

    def greet():
        """function used to greet"""
        print('Hello World!')

    # call the function
    greet()

    print('Outside function')

Hãy chạy trương trình trên để thấy đầu ra là:

    Hello World!
    Outside function

Ở đây, khi hàm `greet` được gọi, chương trình sẽ đi đến định nghĩa hàm và thực hiện khối code trong nó, sau khi thực hiện xong khối code, nó sẽ nhảy ra ngoài và thực hiện tiếp câu lệnh ở sau câu lệnh gọi hàm.

Trong thực tế, dù không phải là một quy tắc bắt buộc, với chương trình lập trình hướng cấu trúc mà có phạm vi nhỏ, chúng ta nên tạo các hàm và gọ lại nó trong hàm main. Sau đó gọi hàm main một lần để chạy cả chương trinh. Với các chương trình lớn cũng không nằm ngoài phong cách này, nhưng nó được chia tách module, chúng ta sẽ học về nó ở phần sau.

Cấu trúc của một chương trình python theo kỹ thuật lập trình hướng cấu trúc nên là:

    """Module docstring"""


    # imports
    # CONSTANTS

    def main():
        """Function docstring"""
        # statements...
        do_stuff()


    def do_stuff():
        """Function docstring"""
        # statements 


    main()

___Note:___
- Lưu ý rằng một hàm chỉ nên thực hiện một việc.
- Tên của hàm cần phản ánh được chức năng hàm thực hiện
- Trong thân hàm nên có comment để mô tả việc mà hàm thực hiện

### Parameter và Argument
Hiểu một cách đơn giản, parameter chính là tham số của hàm – là tên các biến sẽ được sử dụng trong hàm.
Còn argument là đối số, tức là giá trị mà ta truyền cho parameter.

Một hàm có thể có tham số hoặc không.
Ví dụ về hàm không có tham số:

    # function with no argument
    def add_numbers():
        # code

Nếu chúng ta tạo hàm không có tham số thì khi gọi hàm chúng ta không truyền đối số như sau:

    # function call with no value
    add_numbers()

Ví dụ về hàm có tham số:

    def add_numbers(a, b): # a, b là parameter (tham số)
        sum = a + b
        print('Sum:', sum)

Nếu chúng ta tạo hàm có tham số thì khi gọi thường chúng ta sẽ phải truyền đối số như sau:

    # function call with two values
    add_numbers(2, 3) # 2, 3 là argument (đối số)

    # Output: Sum: 5

Trong ví dụ trên, hàm add_numbers() nhận hai tham số: a và b.

    add_numbers(2, 3)

Ở đây, add_numbers(2, 3) chỉ định tham số a và b sẽ nhận giá trị 2 và 3 tương ứng.
#### Positional arguments
Đối số được truyền vào hàm `add_numbers` gọi là positional arguments. Khi chúng ta gọi hàm bằng cách truyền các positional arguments, hàm sẽ ánh xạ giá trị các đối số cho tham số tương ứng bằng vị trí của chúng ở phần khai báo hàm.

Ví dụ chúng ta có hàm sau:

    def info(name, age):
        print(f"Hi, my name is {name}. I am {age * 365.25} days old.")

Bây giờ hãy gọi hàm như sau:

    info("Alice", 23.0)

Output:

    Hi, my name is Alice. I am 8400.75 days old.

Khi sử dụng Positional arguments, vị trí các đối số rất quan trọng. Giờ nếu gọi hàm này với cùng giá trị các đối số như đảo vị trí, chúng ta sẽ gặp lỗi:

    info(23.0, "Alice")

Output:

    Traceback (most recent call last):
    File "filename.py", line 5, in <module>
        info(23.0, "Alice")
    File "filename.py", line 3, in info
        print(f"Hi, my name is {name}. I am  {age * 365.25} days old.")
    TypeError: can't multiply sequence by non-int of type 'float'

Bởi bây giờ nó đang coi name là age, age là name.
#### Default arguments
Trong Python, chúng ta có thể cung cấp các giá trị mặc định cho các đối số của hàm.

Chúng ta sử dụng toán tử `=` để xác đinh các giá trị mặc định. Ví dụ:

    def add_numbers(a = 7, b = 8):
        sum = a + b
        print('Sum:', sum)

    # function call with two arguments
    add_numbers(2, 3)

    #  function call with one argument
    add_numbers(2)

    # function call with no arguments
    add_numbers()

Đầu ra:

    Sum: 5
    Sum: 10
    Sum: 15

Trong ví dụ trên, hãy chú ý định nghĩa hàm:

    def add_numbers(a = 7, b = 8):
        ...

Ở đây, chúng ta đã xác định giá trị mặc định của các tham số a và b tương ứng là 7 và 8. Khi đó, khi gọi hàm mà không truyền giá trị đối số thì hàm sẽ lấy giá trị lần lượt là 7 và 8 mà không báo lỗi.


#### Python Keyword Argument
Các đối số từ khóa là các đối số được truyền vào hàm mà được kèm theo tên tham số tương ứng của nó.
Ví dụ:

    def display_info(first_name, last_name):
        print('First Name:', first_name)
        print('Last Name:', last_name)

    display_info(last_name='Cartman', first_name='Eric')
    display_info('Cartman', 'Eric')

Output

    First Name: Eric
    Last Name: Cartman
    First Name: Cartman
    Last Name: Eric

Lời gọi hàm ở đây là:

    display_info(last_name='Cartman', first_name='Eric')

Chúng ta đã chỉ định rõ ràng giá trị của từng đối số với tham số tương ứng.

___Note:___
- Positional argument không thể xuất hiện sau keyword arguments.

    Ví dụ:

        def display_info(first_name, last_name):
            print('First Name:', first_name)
            print('Last Name:', last_name)

        display_info(last_name='Cartman', 'Eric')

    Output:

        File "F:\GS\py\source\03\ar.py", line 5
            display_info(last_name='Cartman', 'Eric')
                                                    ^
        SyntaxError: positional argument follows keyword argument

- Non Default arguements không thể xuất hiện sau default arguments.
    Ví dụ:

        def display_info(first_name="Bob", last_name):
        print('First Name:', first_name)
        print('Last Name:', last_name)

    Output:

        File "F:\GS\py\source\03\arer2.py", line 1
            def display_info(first_name="Bob", last_name):
                                            ^^^^^^^^^
        SyntaxError: non-default argument follows default argument

### Hàm trả về giá trị
Một hàm có thể trả về một giá trị hoặc không, nó phụ thuộc vào mục đích và cách viết mã của người lập trình.
Hàm `greet` ở trên là một hàm không trả về giá trị, dưới đây là một ví dụ cho hàm trả về giá trị và cách gọi nó:

    # function with two arguments
    def add_numbers(num1, num2):
        sum = num1 + num2
        return sum

    # function call with two values
    sum = add_numbers(5, 4)
    print(sum)

Với hàm có return value, chúng ta có thể gọi hàm, sử dụng giá trị hàm trả về gán vào biến, nhưng việc này là không bắt buộc, chúng ta có thể gọi hàm có return value mà không gán giá trị hàm trả về cho một biến nào như sau:

    # function with two arguments
    def add_numbers(num1, num2):
        sum = num1 + num2
        return sum

    # function call with two values
    add_numbers(5, 4)

Hoặc viết như thế này:

    # function with two arguments
    def add_numbers(num1, num2):
        sum = num1 + num2
        return sum

    # function call with two values
    print(add_numbers(5, 4))

Nhưng hãy cân nhắc về design và yêu cầu thực tế để có cách viết và gọi hàm hợp lý.
### Standard library functions
Trong Python, các hàm thư viện tiêu chuẩn là các hàm tích hợp sẵn có thể được sử dụng trực tiếp trong chương trình của chúng ta. Ví dụ: print(), input(), sqrt() (hàm trả về căn bậc 2), pow()

    import math

    # sqrt computes the square root
    square_root = math.sqrt(4)

    print("Square Root of 4 is",square_root)

    # pow() comptes the power
    power = pow(2, 3)

    print("2 to the power 3 is", power)

Ở đây chúng ta sử dụng 3 build-in function, là sqrt, power, print. Trong đó để sử dụng được hàm sqrt và power chúng ta cần nhập (import) từ module math. Vì hàm power() và sqrt() được định nghĩa bên trong module math. 
## Python Recursion
### Đệ quy là gì
Đệ quy là quá trình xác định một cái gì đó theo chính nó.
![Mirror](media/recursion.jpg)

### Hàm đệ quy trong python
Hàm đệ quy là hàm tự gọi chính nó.
Ví dụ chúng ta có một hàm đệ quy `recurse` thì đây là hình ảnh minh họa cho cách nó hoạt động:
![Mirror](media/python-recursion-function.png)

Ví dụ về hàm đệ quy tính giai thừa của một số nguyên:

    def factorial(x):
        """This is a recursive function
        to find the factorial of an integer"""

        if x == 1:
            return 1
        else:
            return (x * factorial(x-1))


    num = 3
    print("The factorial of", num, "is", factorial(num))

Output:

    The factorial of 3 is 6

Ở đây, hàm `factorial` là hàm đệ quy khi nó tự gọi lại chính nó. Trong mỗi hàm, nó sẽ nhân một số với giai thừa của của số bên dưới nó cho đến khi số giảm về 1. Quá trình này có thể được minh họa như sau:

    factorial(3)          # 1st call with 3
    3 * factorial(2)      # 2nd call with 2
    3 * 2 * factorial(1)  # 3rd call with 1
    3 * 2 * 1             # return from 3rd call as number=1
    3 * 2                 # return from 2nd call
    6                     # return from 1st call

Hàm đệ quy dừng lại khi nó dừng việc gọi lại chính nó. Ở đây hàm `factorial` dừng việc gọi lại chính nó khi `x == 1`. Đây gọi là điều kiện cơ sở.

Trình thông dịch Python giới hạn độ sâu của đệ quy để giúp tránh chạy đệ quy vô hạn, dẫn đến tràn ngăn xếp.

Theo mặc định, độ sâu tối đa của đệ quy là 1000. Nếu vượt qua giới hạn, nó dẫn đến lỗi `RecursionError`. Hãy xem xét một chương trình như vậy:

    def recursor():
        recursor()
    recursor()

Output:

    Traceback (most recent call last):
        File "<string>", line 3, in <module>
        File "<string>", line 2, in a
        File "<string>", line 2, in a
        File "<string>", line 2, in a
        [Previous line repeated 996 more times]
    RecursionError: maximum recursion depth exceeded
### Ưu điểm của đệ quy
- Các hàm đệ quy làm cho mã trông sạch sẽ và thanh lịch.
- Một nhiệm vụ phức tạp có thể được chia nhỏ thành các vấn đề con đơn giản hơn bằng cách sử dụng đệ quy.
- Trong nhiều trường hợp, việc sự dụng đệ quy giúp tạo trình tự logic dễ dàng so với sử dụng việc sử dụng các phép lặp.
### Nhược điểm của đệ quy
- Đôi khi logic đằng sau đệ quy khó theo dõi.
- Chường trình đệ quy tốn kém (không hiệu quả) vì chúng chiếm nhiều bộ nhớ và thời gian.
- Hàm đệ quy khó gỡ lỗi.
## Python Lambda - Anonymous Function
Trong python, hàm ẩn danh, hay còn gọi là hàm lambda là hàm không có tên hàm. Ví du:

    lambda : print('Hello World')

Cú pháp:

    lambda arguments : expression

Trong đó:
- argument(s)- đối số được truyền vào hàm
- expression - biểu thức được thực thi và trả về

Hàm lambda có thể nhập không hoặc nhiều đối số nhưng chỉ có thể có một biểu thức.

Hãy xem xét ví dụ sau:

    greet = lambda : print('Hello World')

Ở đây chúng ta định nghĩa một hàm lambda và gán nó cho biến `greet`. Để thực thi hàm lambda chúng ta cần gọi nó. Đây là cách gọi:

    # call the lambda
    greet()

Output:

    Hello World

___Note:___ Hàm lambda này khống có bất kỳ đối số nào.

Ví dụ về hàm lambda nhận đối số:

    # lambda that accepts one argument
    greet_user = lambda name : print('Hey there,', name)

    # lambda call
    greet_user('Delilah')

    # Output: Hey there, Delilah

Ở đây, chúng ta đã định nghĩa hàm lambda và gán nó cho biến greet_user. Ở đây từ `name` đặt ngay sau từ khóa `lambda` và trước dấu `:` có nghĩa là hàm nhận đối số tên là name. Và khi gọi hàm, chúng ta truyền giá trị đối số vào như sau:

    greet_user('Delilah')

Ví dụ khác về hàm lambda:

    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2))

Chúng ta cũng có thể truyền đối số vào hàm lambda bằng các keyword argument, ví dụ như sau:

    x = lambda a, b, c : a/b + c
    print(x(12, 6, c=2))
    print(x(b=6, a=12, c=2))

### Tại sao nên sử dụng hàm lambda
Sức mạnh của lambda được thể hiện rõ hơn khi chúng ta cần sử dụng chúng như một chức năng ẩn danh bên trong một chức năng khác hoặc khi cần một hàm ẩn danh trong một khoảng thời gian ngắn.


Ví dụ về việc tạo hai hàm luôn nhân đôi và nhân ba giá trị người dùng truyền vào:

    def multi_func(n):
    return lambda a : a * n

    doubler = multi_func(2)
    tripler = multi_func(3)

    print(doubler(11))
    print(tripler(11))

## Python Variable Scope
Phạm vi của biến chính là khu vực mà chúng ta có thể truy cập tới biên đó.
Trong Python, phạm vi của một biết có thể thuộc một trong các loại sau: phạm vi cục bộ, toàn cầu và phạm vi không cục bộ.
Nếu phân loại trên phạm vi biến, thì chúng ta có thể phân loại biến python thành ba loại:
- Biến cục bộ
- Biến toàn cầu
- Biến không cục bộ

### Biến cục bộ Python
Là biến được khai báo trong phạm vi hàm. Chúng ta không thể truy cập chúng ở ngoài phạm vi hàm.

Ví dụ:

    """
    An error program
    """

    def greet():
        # local variable
        message = 'Hello'
        
        print('Local', message)

    greet()

    # try to access message variable 
    # outside greet() function
    print(message)

Output:

    Local Hello
    NameError: name 'message' is not defined

Lỗi `name 'message' is not defined` xuất hiện khi chúng ta cố gắng truy cập một biến local ngoài phạm vi của nó.
Để truy cập một biến ở ngoài hàm, biến đó cần là biến toàn cục Global variable.
### Python Global Variables
Biến được khai báo bên ngoài hàm hoặc trong phạm vi toàn cục được gọi là biến toàn cục hay biến global. Biến toàn cục có thể được truy cập từ bên trong hoặc bên ngoài hàm.

Ví dụ:

    # declare global variable
    message = 'Hello'

    def greet():
        # declare local variable
        print('Local', message)

    greet()
    print('Global', message)

Output

    Local Hello
    Global Hello

Ở đây biến `message` được khai báo ngoài hàm vì vậy chúng ta có trể truy cập ở cả trong hàm lẫn ngoài hàm.

### Python Nonlocal Variables
Trong python, từ khóa nonlocal được sử dụng để làm việc với các biến bên trong các hàm lồng nhau, trong đó biến không được thuộc về hàm bên trong.

Hãy so sánh kết quả của hai chương trình:

    # outside function 
    def outer():
        x = "John"

        # declare nonlocal variable
        def inner():
            nonlocal x
            x = "hello"

        inner()
        return x

    print(outer())

Ouput:

    hello

Và,

    # outside function 
    def outer():
        x = "John"

        # nested function
        def inner():
            x = "hello"

        inner()
        return x

    print(outer())

Ouput:

    John

## Python Global Keyword
Hãy xem xét ví dụ sau, ví dụ về việc cố gắng thay đổi giá trị của biến global trong phạm vi local:

    # declare variable x
    x = 2

    def mmath():
        # try to change the value of x in mmath function
        x *= 2
        print(x)

    mmath() # cannot access local variable 'x' where it is not associated with a value

Output:

    UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

Lỗi này xuất hiện là do Python xử lý x như một biến cục bộ và x không được định nghĩa trong mmath().

Để thay đổi biến toàn cục trong một hàm bạn sẽ phải sử dụng từ khóa global.

Trong python, từ khóa `global` được sử dụng để tạo các biến toàn cục từ phạm vi không toàn cầu, ví dụ như bên trong một hàm. Hoặc để sửa đổi giá trị một biến toàn cầu trong phạm vi toàn cục.

Hãy xem xét những ví dụ sau:

    # create a function:
    def myfunction():
    global x
    x = "hello"

    # execute the function:
    myfunction()

    # x should now be global, and accessible in the global scope.
    print(x)

Ở ví dụ trên, chúng ta đã khai báo một biến toàn cục ở trong phạm vi hàm và sau đó có thể sử dụng nó trong phạm vi toàn cục.

Hãy xem xét một ví dụ khác:

    # declare variable x
    x = 2

    def mmath():
        # use of global keyword
        global x

        x *= 2
        print("Inside mmath function ", x)

    print("Before calling mmath function ", x)
    mmath()
    print("After calling mmath function ", x)

Ở ví dụ trên, chúng ta đã sử dụng từ khóa `global` để thay đổi giá trị của biển toàn cầu trong phạm vi một hàm.

Chúng ta cũng có thể sử dụng từ khóa global trong các hàm lồng nhau

<strong>Lưu ý: </strong>Những quy tắc khi dùng từ khóa `global`.
- Khi ta tạo một biến bên trong một hàm, nó sẽ là cục bộ theo mặc định.
- Khi chúng ta xác định một biến bên ngoài một hàm, nó là toàn cục theo mặc định. Chúng ta không cần phải sử dụng từ khóa `global`.
- Ta sẽ sử dụng từ khóa `global` để đọc và ghi một biến toàn cục bên trong một hàm.
- Lưu ý việc sử dụng từ khóa `global` bên ngoài một hàm sẽ không có tác dụng.

## Python Modules
Module là một tệp chứa mã để thực hiện một tác vụ cụ thể. Một module có thể chứa các biến, hàm, class, v.v.

Khi chương trình của chúng ta phát triển lớn hơn, nó có thể có số lượng dòng mã lớn từ vài trăm tới vài nghìn dòng hoặc hơn thế nữa. Thay vì đặt mọi thứ vào một file `.py` duy nhất, chúng ta có thể sử dụng các module để phân tách mã ra các file riêng biệt theo chức năng của chúng. Điều này làm cho mã của chúng ta được tổ chức tốt và dễ bảo trì hơn.

Hoặc ở ngoài kia cũng có những chức năng được python hoặc nhà phát triển open soure khác phát triển và đóng thành các gói, các module để chúng ta có thể tải về hoặc trực tiếp sử dụng, và dùng cho mã của mình.

### Tạo một module
Trước tiên hãy tự tạo module cho chính mình.
Để tạo một module, chỉ cần lưu mã mà chúng ta muốn vào một file có extension là `.py`:

Ví dụ, lưu những dòng code sau và một file .py, ví dụ file mymodule0.py:

    def greeting(name):
        print("Hello, " + name)

### Sử dụng một module
Bây giờ chúng ta có thể sử dụng module chúng ta vừa tạo ở một file khác tên là use_mymodule0.py bằng cách sử dụng câu lệnh `import`:
   
    import mymodule

    mymodule.greeting("Jonathan")

### Biến trong module
Như đã được mô tả, module có thể chứa các hàm, nhưng cũng có các biến thuộc mọi loại:

Ví dụ, hãy viết những dòng code sau trong file `mymodule1.py`:

    x = 1
    y = 2

Sau đó trong file use_mymodule1.py, chúng ta có thể import module mymodule1 và sử dụng biến x và y.

    import mymodule1

    a = mymodule1.x
    b = mymodule1.y
    print(a)
    print(b)

### Đặt bí danh cho một module
Đôi khi chúng ta sẽ muốn đặt bí danh cho một module, khi đó chúng ta sử dựng từ khóa `as`:

    import mymodule1 as mx

    a = mx.x
    b = mx.y
    print(a)
    print(b)

### Built-in Modules
Built-in Modules là những module được xây dựng và tích hợp sẵn trong python.

Ví dụ chúng ta có thể import và sử dụng các hàm của module math như sau:

    # import standard math module 
    import math

    # use math.pi to get value of pi
    print("The value of pi is", math.pi)

Chúng ta không cần phải tạo một file tên là math.py và viết tất cả mã nguồn trong đó, mà có thể sử dụng ngay và luôn các hàm của module math. Bởi python đã tự động tích hợp những module đó.

### From module import something
Đôi khi chúng ta muốn chủ đích import cụ thể một biến hay một hàm hay class, object..., chúng ta có thể sử dụng cú pháp:

    form module import something

Ví dụ về import hàm:

    from mymodule0 import greeting

    greeting("Jonathan")

Ví dụ về import biến:

    from mymodule1 import x

    a = x
    print(a)

Chúng ta có thể import nhiều giá trị một lúc như sau:

    from mymodule1 import x, y

Những nội dung không được import thì sẽ không được sử dụng.

### Import all

Trong Python, chúng ta có thể nhập tất cả các tên (định nghĩa) từ một module bằng cách sử dụng cấu trúc sau:

    # import all names from the standard module math
    from math import *

    print("The value of pi is", pi)

Khi import * thì lúc sử dụng hàm, thay vì phải viết math.pi, chúng ta chỉ cần viết pi. Nhưng hãy lưu ý đây không phải là một cách lập trình tốt bởi có thể dẫn đến việc trùng tên mã định danh.
### Gọi hàm trong module
Đôi khi một số hàm trong module được gọi ngay trong chính module đó, khi đó nếu gọi hàm một các bình thường ở trong file module, sau đó import module ở bên ngoài và chạy file bên ngoài, thì hàm được gọi 2 lần. Hãy xem xét tiến trình sau:

file module:

    def greeting(name="My"):
        print("Hello, " + name)

    greeting()


file use module:

    import mymodule3

    mymodule3.greeting("Jonathan")

Ouput:

    Hello, My
    Hello, Jonathan

Sửa lại file module:

file module:

    def greeting(name="My"):
        print("Hello, " + name)

    if __name__ == "__main__":
        greeting()


Ở dây chúng ta dùng `__name__ == "__main__"` để chương trình hiểu hàm này chỉ chạy khi module này được chạy trưc tiếp.
## Python Package

Package là một gói bao gồm một hoặc nhiều file. Các file, hay module .py được tách và gộp vào thành package khi chương trình dự án lớn, cần được tách ra để dễ bảo trì, quản lý và sử dụng.

Để một thư mục được coi là một package trong python, cần tạo cho nó file __init__.py. File này có thể để trống.

### Nhập module từ một package
Giả sử chúng ta tạo package tên là mypackage, trong đó có module mymodule0.
Chúng ta có thể làm như sau:

    import mypackage.mymodule0

Hoặc

    from mypackage.mymodule0 import x, y

để nhập cụ thể một số giá trị nhất định.

Ở đây cách viết `mypackage.mymodule0` thể hiện mối quan hệ thư mục, hay còn gọi là path, để dẫn đến được module chúng ta muốn import.

Chúng ta có một chương trình hoàn thiện như sau:

    from mypackage.mymodule0 import x, y

    print("x + y = {}".format(x + y))
