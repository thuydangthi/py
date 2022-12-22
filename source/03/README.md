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

#### Làm sao để gọi hàm trong python?
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

### Python Function Arguments
Như đã đề cập phía trên, một hàm cũng có thể có các đối sổ (argument). Đối số là giá trị được truyền vào hàm khi hàm được gọi.
Ví dụ về đối số:

    # function with two arguments
    def add_numbers(num1, num2):
        sum = num1 + num2
        print('Sum: ',sum)

Nếu chúng ta tạo hàm có tham số thì khi gọi hàm chúng ta cần truyền các đối số tương ứng như sau:

    # function call with two values
    add_numbers(5, 4)

Hoặc

    # function with no argument
    def add_numbers():
        # code

Nếu chúng ta tạo hàm không có tham số thì khi gọi hàm chúng ta không truyền tham số như sau:

    # function call with no value
    add_numbers()

Chúng ta cùng xem ví dụ hoàn chỉnh sau:

    # function with two arguments
    def add_numbers(num1, num2):
        sum = num1 + num2
        print("Sum: ",sum)

    # function call with two values
    add_numbers(5, 4)

    # Output: Sum: 9

<strong>Note: </strong> Ngoài cách gọi hàm là add_numbers(5, 4), chúng ta cũng có thể gọi add_numbers(num1 = 5, num2 = 4), trong python, đây gọi là Keyword Argument (đối số từ khóa).

Câu hỏi: nên gọi hàm theo cách nào trong 2 cách trên và tại sao?

### Cách khiến hàm trả về giá trị
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

## Parameter và Argument
Hiểu một cách đơn giản, parameter chính là tham số của hàm – là tên các biến sẽ được sử dụng trong hàm.
Còn argument là đối số, tức là giá trị mà ta truyền cho parameter.

Ví dụ:

    def add_numbers(a, b): # a, b là parameter (tham số)
        sum = a + b
        print('Sum:', sum)

    add_numbers(2, 3) # 2, 3 là argument (đối số)

    # Output: Sum: 5

Trong ví dụ trên, hàm add_numbers() nhận hai tham số: a và b. Chú ý dòng

    add_numbers(2, 3)

Ở đây, add_numbers(2, 3) chỉ định tham số a và b sẽ nhận giá trị 2 và 3 tương ứng.

### Default Values của Arguments
Trong Python, chúng ta có thể cung cấp các giá trị mặc định cho các đối số của hàm.

Chúng tôi sử dụng toán tử `=` để xác đinh các giá trị mặc định. Ví dụ:

    def add_numbers(a = 7, b = 8):
        sum = a + b
        print('Sum:', sum)

    # function call with two arguments
    add_numbers(2, 3)

    #  function call with one argument
    add_numbers(a = 2)

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

Hãy thử gọi hàm theo những cách sau:

    def add_numbers(a = 7, b = 8):
        sum = a + b
        print('Sum:', sum)

    add_number(2, 3)

    add_number(2)

    add_number()

### Python Keyword Argument


## Python Recursion

## Python Lambda/Anonymous Function

## Python Variable Scope

## Python Global Keyword

## Python Modules

## Python Package
