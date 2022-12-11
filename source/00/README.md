# Python Introduction
Python (phát âm tiếng Anh: /ˈpaɪθɑːn/) là một ngôn ngữ lập trình bậc cao cho các mục đích lập trình đa năng, do Guido van Rossum tạo ra và lần đầu ra mắt vào năm 1991.
Python được thiết kế với ưu điểm mạnh là dễ đọc, dễ học và dễ nhớ.
Python là ngôn ngữ có hình thức rất sáng sủa, cấu trúc rõ ràng, thuận tiện cho người mới học lập trình và là ngôn ngữ lập trình dễ học; được dùng rộng rãi trong phát triển trí tuệ nhân tạo. [_(Theo Wiki)_](https://vi.wikipedia.org/wiki/Python_(ng%C3%B4n_ng%E1%BB%AF_l%E1%BA%ADp_tr%C3%ACnh))

Python là ngôn ngữ lập trình đa nền tảng, nghĩa là nó có thể chạy trên nhiều nền tảng như Windows, macOS, Linux và thậm chí đã được chuyển sang các máy ảo Java và .NET. Nó là miễn phí và mã nguồn mở.
Mặc dù hầu hết Linux và Mac ngày nay đều được cài đặt sẵn Python, nhưng phiên bản này có thể đã lỗi thời. Vì vậy, luôn luôn nên cài đặt phiên bản mới nhất.

# Cài đặt python và chạy python
Here: [Website của python](https://www.python.org/downloads/)

## Chạy python trên cửa sổ command line
Một điều tiện lợi của python là nó tự động cài đặt một cửa sổ shell cho riêng nó.
Chúng ta mở python shell bằng cách gõ `python` vào command line (cmd của Windows).

![Chạy Python trên dòng lệnh](media\pythonshell.png)

## Chạy python trên IDE

IDE là viết tắt của Integrated Development Environment, là môi trường tích hợp dùng để viết code để phát triển ứng dụng. IDE tích hợp các tool hỗ trợ khác như trình biên dịch (Compiler), trình thông dịch (Interpreter), kiểm tra lỗi (Debugger), định dạng hoặc highlight code, tổ chức thư mục code, tìm kiếm code…

Khi cài đặt python, một IDE có tên là IDLE cũng được cài đặt. Chúng ta có thể dùng nó để chạy Python trên máy tính của mình. Nó cũng phù hợp cho người mới bắt đầu.

![Chạy Python trên idle](media\idle.png)


## Viết một file .py

Hãy dùng VS code và viết chương trình đầu tiên của bạn vào file `helloworld.py`:

    print("Hello, world!")

Mở terminal và chạy câu lệnh `python helloworld.py`

# Một chút so sánh với C
| Nội dung so sánh | C    | Python    |
| :---   | :--- | :--- |
| Mô hình | C là ngôn ngữ lập trình hướng cấu trúc   | Python là một ngôn ngữ lập trình hướng đối tượng   |
| Loại ngôn ngữ | C là ngôn ngữ cấp trung   | Python là ngôn ngữ cấp cao   |
| Biên dịch và thông dịch | C sử dụng trình biên dịch. Trình biên dịch là chương trình đặc biệt dùng để kiểm tra từng dòng mã C và nếu tìm thấy bất kỳ lỗi nào trên bất kỳ dòng nào, quá trình biên dịch chương trình sẽ dừng lại ngay sau đó.   | Python sử dụng trình thông dịch. Trình thông dịch là các chương trình đặc biệt dùng để kiểm tra toàn bộ mã Python và tất cả các lỗi trong toàn bộ mã Python được báo cáo cùng một lúc.   |
| Tốc độ | C nhanh hơn, do chạy bằng trình biên dịch   | Python chậm hơn   |
| Cách định nghĩa | Trong C, data type của các biến phải được khai báo rõ ràng khi ta khai báo nó, và chỉ có thể gán các giá trị có kiểu đúng với kiểu dữ liệu cho biến cụ thể đó   | Với python, khai báo các biến không phải khai báo kieur dữ liệu, chúng ta có thể gán giá trị có kiểu dữ liệu khác với kiểu dữ liệu lúc khai báo, lúc đó quá trình thay đổi kiểu dữ liệu cũng diễn ra   |
| Quản lý bộ nhớ | Quản lý bộ nhớ cần được thực hiện thủ công trong C   | Quản lý bộ nhớ được xử lý tự động trong Python   |
| Con trỏ | C hỗ trợ cho con trỏ   | Python không hỗ trợ con trỏ |
| Functional Units | Trong C, hầu hết các Functional Units là các chức năng vì nó là ngôn ngữ lập trình thủ tụ (hướng cấu trúc)   | Trong Python, hầu hết các Functional Units là các đối tượng vì nó là ngôn ngữ lập trình hướng đối tượng   |
| Ứng dụng | C chủ yếu được sử dụng để phát triển các ứng dụng phần cứng   | Python là một ngôn ngữ lập trình mục đích chung (được thiết kế để sử dụng để xây dựng phần mềm trong nhiều miền ứng dụng hay trên vô số cấu hình phần cứng và hệ điều hành) |
| Hàm tích hợp | Số lượng hàm tích hợp trong C rất hạn chế   | Có rất nhiều hàm tích hợp sẵn trong Python |
| Cấu trúc dữ liệu | Để sử dụng các cấu trúc dữ liệu khác nhau như ngăn xếp, hàng đợi, v.v. trong C, chúng ta cần tự triển khai chúng   | Python cung cấp các thư viện tích hợp sẵn, vì vậy việc sử dụng các cấu trúc dữ liệu trong python trở nên dễ dàng hơn  |
| Gán nội tuyến | Có thể   | Không thể |
| File | .c   | .py |

# Identifiers và keywords trong python

## keywords
Các keywords trong python:
False, True, await, else, import, None, except, try,raise, class, return, or, and, is, as, in, not, lambda, def, pass, from, nonlocal, for, while, finally, continue, break, assert, del, global, with, async, elif, if, yield

## Identifiers
Identifiers, định danh, tức là các tên dùng để đặt cho các biến, các class, tên hàm, method,... trong python. Ví dụ:

    language = 'Python'

Không thể dùng tên keyword làm định danh


![Định danh trong python](media\keyword.png)

Quy tắc đặt tên cho một định danh:
- Định danh không thể là một từ khóa.
- Mã định danh phân biệt chữ hoa chữ thường.
- Nó có thể có một chuỗi các chữ cái và chữ số. Tuy nhiên, nó phải bắt đầu bằng một chữ cái hoặc _. Chữ cái đầu tiên của mã định danh không được là chữ số.
- Đó là một quy ước để bắt đầu một số nhận dạng bằng một chữ cái thay vì _.
- Khoảng trắng không được phép.
- Chúng tôi không thể sử dụng các ký hiệu đặc biệt như ! , @ , # , $ , v.v.

Hãy thử bằng IDLE hoặc cmd hoặc một file .py!

# Comments

Nhận xét trong python giúp source code dễ hiểu hơn, các comments được bỏ qua bởi trình thông dịch, mà nó dành cho các lập trình viên để đọc nó.

Ví dụ:

    # declare and initialize two variables
    num1 = 6
    num2 = 9

## Các loại bình luận trong python
Có 2 loại:
- Bình luận 1 dòng
- Bình luận nhiều dòng

## Bình luận 1 dòng
Bình luận một dòng bắt đầu và kết thúc trên cùng một dòng. Chúng ta sử dụng biểu tượng `#` để viết bình luận một dòng. Ví dụ,

    # Create a variable
    name = 'Snowman'

    # Print the value
    print(name) # name is a string

Hãy chạy nó:

    Snowman

Ở đây chúng ta đã có 3 cmt, các cmt có thể dùng dòng với dòng mã hoặc ở một dòng riêng.

## Bình luận nhiều dòng
Python không cung cấp cách riêng biệt để viết nhận xét nhiều dòng, tuy nhiên có một số cách khác để làm nó, như sau:
- Chúng ta có thể dùng dấu `#` ở mỗi dòng để viết nhận xét liên túc:

        # This is a long comment,
        # because it was too long,
        # I split it into 3 lines
- Một cách khác để làm việc này là sử dụng `"""` hoặc `'''` để bắt đầu và kết thúc phần comments:
        
        """ This is a long comment,
        because it was too long,
        I split it into 3 lines """

    hoặc:

        ''' This is a long comment,
        because it was too long,
        I split it into 3 lines '''

Ở đây, chuỗi nhiều dòng không được gán cho bất kỳ biến nào, vì vậy nó sẽ bị trình thông dịch bỏ qua. Mặc dù về mặt kỹ thuật nó không phải là một bình luận nhiều dòng, nhưng nó có thể được sử dụng như một bình luận.

# Biến
Giống như C, biến trong python, hay trong lập trình là một vùng lưu trữ giá trị mà được gắn một định danh. Ví dụ cách tạo biến trong python:

    number = 10

Ở đây chúng ta có một biến tên là number, có giá trị là 10.

## Định nghĩa biến
Không giống trong C:

    int x;

Trong python chúng ta không thể viết thế này:

    x

![Biến trong python](media\variable_err.png)
Mà chúng ta cần gán giá trị cho nó luôn. Chúng ta sử dụng toán tử gán `=` để gán giá trị cho biến:

    # assign value to name variable
    name = 'Snowman'

    print(name)

## Thay đổi giá trị biến

    # assign value to name variable
    name = 'Snowman'

    # assign value to name variable
    name = 'Duo'

    print(name)

Hãy chạy thử, chúng ta sẽ thấy, ở đây chúng ta dã thay đổi giá trị của biế name, chương trình in ra là Duo thay vì Snowman.

## Gán nhiều giá trị cho nhiều biến
Chúng ta có thể gán nhiều giá trị cho nhiều biến cùng một lúc, ví dụ:

    a, b, c = 5, 3.2, 'Hello'

    print(a)  # prints 5
    print(b)  # prints 3.2
    print(c)  # prints Hello

Hoặc chúng ta có thể làm như thế này để gán cùng một giá trị cho nhiều biến:

    name1 = name  = 'Snowman'

    print(name1)  # prints Snowman
    print(name)  # prints Snowman

## Biến hằng số
Hằng số là một loại biến đặc biệt mà giá trị của nó không thể thay đổi được.
Trong Python, các biến hằng số thường được khai báo và gán trong một mô-đun (một tệp mới chứa các biến, hàm, v.v. mà sau đó sẽ được import vào file chính).

Ví dụ, tạo một file `const.py`:

    A = 100
    B = 200

Tạo một file `main.py` như sau:

    import const

    print(const.A)
    print(const.B)

Hãy chạy nó.

Lưu ý: Trên thực tế, chúng ta không sử dụng hằng số trong Python. Đặt tên chúng bằng tất cả các chữ in hoa là một quy ước để tách chúng khỏi các biến, tuy nhiên, nó không thực sự ngăn cản việc gán lại giá trị cho chúng. Như thế này:

    import const

    print(const.A)
    print(const.B)

    const.A = 2
    print(const.A)
## Quy tắc và quy ước đặt tên cho các biến và hằng số trong Python
- Tên hằng và tên biến phải có sự kết hợp của các chữ cái ở dạng chữ thường (a đến z) hoặc chữ hoa (A đến Z) hoặc chữ số (0 đến 9) hoặc dấu gạch dưới (_).
- Nên tạo một cái tên có ý nghĩa. Ví dụ, name thay vì n.
- Nếu ta muốn tạo một tên biến có hai từ, ta có thể sử dụng dấu gạch dưới để phân tách chúng.
- Sử dụng các chữ cái in hoa để khai báo một hằng số.
- Không bao giờ sử dụng các ký hiệu đặc biệt như !, @, #, $,%, v.v.
- Không bắt đầu tên biến bằng một chữ số.

Chú ý khi đặt tên biến: trong python phân biệt định danh chữ hoa chữ thường, vì vậy biến Name khác biến NAME

## Các loại biến
### Biến kiểu chữ số
Các giá trị kiểu chữ số có thể thuộc 3 kiểu dữ liệu số khác nhau bao gồm số nguyên (Integer), số thập phân (Float) hoặc số phức (Complex).
#### Số nguyên
Là số bao gồm các số nguyên dương (1, 2, 3, ..), các số nguyên âm (-1, -2, -3) và số 0.
Ví dụ:

        x = 1
        y = 2
    Một điểm đáng chú ý trong Python 3.X đó là kiểu dữ liệu số nguyên là vô hạn. Điều này cho phép chúng ta tính toán với những số cực kì lớn, điều mà đa số các ngôn ngữ lập trình khác KHÔNG THỂ.
#### Số thập phân
Ví dụ:

    x = 1.1
    print(x)
    
    y = 10/3
    printf(y) # 3.3333333333333335

- Lưu ý: Thường khi chúng ta viết số thực, phần nguyên và phần thập phân được tách nhau bởi dấu phẩy ( , ). Thế nhưng trong Python, dấu phẩy ( , ) này được thay thế thành dấu chấm ( . )
- Số thực trong Python có độ chính xác xấp xỉ 15 chữ số phần thập phân.
- Nếu muốn có kết quả được chính xác cao hơn, chúng ta nên sử dụng `Decimal`.
- Tuy Decimal có độ chính xác cao hơn so với float tuy nhiên nó lại khá rườm rà so với float. Do đó, hãy cân bằng sự tiện lợi và chính xác để chọn kiểu dữ liệu phù hợp.

#### Số phức

Số phức gồm 2 thành phần :

    <Phần thực> + <Phần ảo> j

Để tạo một số phức, bạn có thể sử dụng hàm `complex` với cú pháp sau:

    complex(<Phần_thực>,<Phần_ảo>)

Ví dụ:

    complex(1, 2)

Gán giá trị số phức cho một biến:

    <tên_biến> = <Phần_thực> + <Phần_Ảo>j
Ví dụ:

    x = complex(1, 2)

Xuất ra từng phần của một biến số phức:
- Để xuất ra phần thực, ta sử dụng cú pháp:

        <tên_biến>.real

    Ví dụ:

        x = complex(1, 2)
        print(x)
        print(x.real)

- Để xuất ra phần ảo của biến số phức, ta dùng cú pháp:

        <tên_biến>.imag
    Ví dụ:

        x = complex(1, 2)
        print(x)
        print(x.imag)

#### Các toán tử cơ bản với kiểu dữ liệu số trong python
Biểu thức chính là một thực thể toán học. Nói cách khác, nó là một sự kết hợp giữa 2 thành phần:
- Toán hạng: có thể là một hằng số, biến số (X , Y)
- Toán tử: xác định cách thức làm việc giữa các toán hạng (+,-,*,/)
Dưới đây là một số toán tử toán học của ngôn ngữ python: +, -, *, /(kết quả luôn là một số float), // (kết quả là phần nguyên), % (phần dư phép chia), ** (lũy thừa)

Chúng ta sẽ đi kỹ hơn về nó ở phần sau.

### Biến Boolean
Có hai chữ boolean: True và False.

Ví dụ:
    pass = true

### String
Ký tự chữ là các ký tự unicode được đặt trong một dấu ngoặc. Ví dụ:
    
    my_string1 = 'S'
    my_string2 = "hello"

### Các giá trị đặc biệt
Python chứa một chữ đặc biệt là `None`. Chúng ta sử dụng nó để chỉ định một biến null. Ví dụ:

    value = None

    print(value)

    # Output: None

# Các kiểu đầu vào đầu ra của python

# In ra màn hình
Trong Python, chúng ta chỉ cần sử dụng hàm print() để in đầu ra. Ví dụ:
    print('Hi')

    # Output: Hi

Cú pháp hàm print:

    print(object=, separator=, end=, file=, flush=)

- object (require): giá trị sẽ được in
- sep (optional): cho phép chúng tôi tách nhiều đối tượng bên trong print().
- end (optional): cho phép chúng tôi thêm các giá trị cụ thể như dòng mới "\n", tab"\t"
- file (optional): nơi các giá trị được in. Giá trị mặc định của nó là sys.stdout(màn hình)
- flush (optional): boolean, chỉ định nếu đầu ra được xóa hoặc lưu vào bộ đệm. Mặc định là False.

## Lấy input từ người dùng
Trong python chúng ta sử dụng hàm input để lấy giá trị từ người dùng. Ví dụ

    # Ask the user for their name
    name = input("What's your name? ")
    print("hello, ")
    print(name)

Ở đây chúng ta thấy nó bị xuống dòng, chúng ta có thể truyền value cho parameter end như sau:

    # Ask the user for their name
    name = input("What's your name? ")
    print("hello, ", end="")
    print(name)

- Bằng cách cung cấp, end="" chúng ta đang ghi đè giá trị mặc định end để cho nó không bao giờ tạo một dòng mới sau câu lệnh in đầu tiên.

## Định dạng trong chuỗi
Chúng ta có những cách khác để truyền biến vào chuỗi:

    # Ask the user for their name
    name = input("What's your name? ")
    print(f"hello ,{name}")

Hoặc:

    # Ask the user for their name
    name = input("What's your name? ")
    print("hello , {}".format(name))
