# Lập trình hướng đối tượng
Có nhiều mô hình lập trình khác nhau. Cho đến thời điểm này, chúng ta đã làm việc theo quy trình step-by-step.
Trong Python, Lập trình hướng đối tượng (OOPs) là một mô hình lập trình sử dụng các đối tượng và lớp (object và class).

## OOP
Python là một ngôn ngữ lập trình hướng đối tượng hoàn toàn, nghĩa là mọi phần tử trong chương trình Python đều là object. Một số, một chuỗi, một danh sách, v.v., mà chúng ta đã biết thực ra đều là object của một class xây dựng sẵn (int, float, str, list, v.v.). Một hàm (xây dựng sẵn hoặc do chúng ta tự xây dựng bằng từ khóa def) cũng là một object.

Như vậy, khi làm việc với Python từ đầu đến giờ, trên thực tế là chúng ta đã trực tiếp sử dụng class và object.

Python cho phép người lập trình tự xây dựng class riêng của mình.
## Class
Class là gì?

Class là một trong những khái niệm đầu tiên và chủ chốt khi nhắc đến lập trình hướng đối tượng.

Một class, lớp, là một nguyên mẫu mà từ đó các đối tượng, hay object được tạo ra. 

Chúng ta có thể tạo một class có tên là Student như sau:

    class Student:
        ...


- Dấu chấm lửng `...` sẽ nói cho chương trình biết chúng ta đang tạm bỏ qua phần này và sẽ quay lại sau. Trong python `...` được ước tính bằng với `Ellipsis`, nó là một hằng số được tích hợp sẵn, nên chúng ta có thể viết `Ellipsis` hoặc chỉ cần viêt là `...`.

![Ellipsis](media/ellipsis.png)

Class trong Python được khai báo với từ khóa class theo cấu trúc như sau:

    class Student:
        # code

Ví dụ: Tạo các class trống trong python

    class Student:
        pass

    class Teacher:
        ...

    class Eexam:
        Ellipsis


Lưu ý: theo chuẩn PEP8 về đặt tên của lớp (class) thì nên được viết theo kiểu CapWords. Ví dụ là AnonymousUser, SuperUser,...

### Các thành phần chính trong một class
Mặc dù chúng ta có thể khai báo một class hoàn toàn không chứa thành viên nào, class như vậy không có giá trị. Class trong Python thường chứa những thành phần sau:

- Các attribute (biến)
- Constructor (hàm tạo)
- Các method (phương thức)
- Các property (thuộc tính)

Chúng ta sẽ học cụ thể về nó ở những phần kế tiếp.

## Objects
Khi chúng ta tạo class, và sử dụng class đó làm nguyên mẫu để tạo ra các thực thể cụ thể, thì các thực thể đó được gọi là các object.

Ví dụ về các object:

    student1 = Student()
    student2 = Student()

Dễ thấy rằng, lệnh tạo object không khác biệt gì so với lời gọi hàm thông thường.

Một đối tượng có 2 thứ đặc trưng:
- Thuộc tính
- Hành vi

## Attribute
Để hiểu attribute là gì, cùng sửa đổi chương trình của chúng ta như sau:

    class Student:
        ...


    student1 = Student()
    student1.name = input("Name: ")
    student1.house = input("House: ")
    print(f"{student1.name} from {student1.house}")

    student2 = Student()
    print(f"{student2.name} from {student2.house}")



Chúng ta đã tạo 2 object là student1 và student2.

Attribute student1 trong trường hợp này có 2 thuộc tính là name và house.

Attribute student2 không có attribute nào.

Chúng ta có thể truy cập tới các attribute của từng object. Làm việc đó bằng cách dùng dấu `.`.

Khi chúng ta cố gắng truy xuất và in ra name và house của student 1 thì chương trình đã in ra thành công, nhưng khi cố gắng làm tương tự vói student2 thì chương trình báo lỗi.

Vì object student1 có 2 attribute là name và house được tạo ra ở ngoài phần khai báo class (hoàn toàn nằm ngoài class), còn object student2 thì không có.

=> Trong Python, attribute là những biến có thể chứa giá trị đặc trưng cho một object. Nó chính là đại diện cho thuộc tính của object.
=> Nó có thể được tạo hoàn toàn độc lập với khai báo class (không bắt buộc phải chỉ định trong khai báo class).

## Hàm constructor \__init__
Từ ví dụ trên, chúng ta thấy có thể tạo object từ cùng một class nhưng có attribute khác nhau bằng cách chỉ định bên ngoài object như thế này:

    class Student:
        ...


    student1 = Student()
    student1.name = input("Name: ")
    student1.house = input("House: ")
    print(f"{student1.name} from {student1.house}")

    student2 = Student()
    student2.age = 12
    print(f"{student2.age}")

Vậy trong trường hợp các object cùng có các attribute giống nhau, và class có trăm, nghìn object? Việc gán bằng tay không phải là một cách tốt.

Vì vậy, python cung cấp method `__init__`, là method constructors. Chúng ta không cần phải gọi nó, nó sẽ được tự động gọi ngay khi một object của một class được khởi tạo.

Nó là một khuôn mẫu để mỗi khi tạo object chúng ta phải là theo để các object được tạo ra có các loại attribute giống nhau.

Ví dụ, class Student xác định rằng, tất cả học sinh được đặc trưng bởi name, house, mỗi một object được tạo đều có sẵn 2 attribute này:

    class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house

- `name` và `house` là hai attribute của class Student.
- `self` là từ khóa dùng đề cập tới chính object đó.
- Ở trong hàm `__init__`, chúng ta đã yêu cầu khi tạo một object từ class Student, phải truyền name và house, vì vậy cách tạo một object trước đó

        student = Student()

    sẽ gây lỗi:

        TypeError: __init__() missing 2 required positional arguments: 'name' and 'house'

    mà cần viết là:

        student = Student(name="Anna", house="house")

    hoặc chỉ cần viết ngắn gọn hơn:

        student = Student("Anna", "house")

Nếu chúng ta muốn khi tạo các object từ class Student không bắt buộc truyền name và house, có 2 cách:
- Không viết method `__init__`
- Hoặc vẫn viết method `__init__` nhưng sử dụng default arguments. Ví dụ:

        class Student:
            def __init__(self, name="Default name", house="Default house"):
                self.name = name
                self.house = house

        student1 = Student()
        print(f"{student1.name} from {student1.house}")

        student2 = Student("Anna", "Gryffindor")
        print(f"{student2.name} from {student2.house}")

Chú ý:
- Cách viết các tham số trong method `__init__` giống hàm bình thường.
- Khi viết method `__init__` cần có tham số `self` đầu tiên.
- Khi tạo object bằng cú pháp `new_obj = ClassName(arguments)` thì method `__init__` được tự động gọi ngay sau khi new_obj được tạo.
## 2 loại Attribute
### Instance Attribute
Instance Attribute là các attribute là các attribute được gắn riêng cho từng object (object trong nhiều ngữ cảnh được gọi là instance).

Attribute name, house trong đoạn mã bên trên cũng là 2 instacne attribute của object.

Hãy mở rộng đoạn mã trên như sau.

    class Student:
        def __init__(self, name="Default name", house="Default house"):
            self.name = name
            self.house = house

    student1 = Student()
    print(f"{student1.name} from {student1.house}")

    student2 = Student("Anna", "Gryffindor")
    print(f"{student2.name} from {student2.house}")

    student1.age = 11
    print(f"Age of student 1: {student1.age}")

Ở đây student1 còn có thêm một instance attribute là age, student2 chỉ có 2 instance attribute là name và house.

Chú ý:
- Attribute được tạo ra trong hàm tạo `__init__` cũng là các instance attribute.
- Chúng ta có thể tạo thêm instance attribute cho một object bên ngoài khai báo class. Nhưng nó không phải là một cách viết tốt, chúng ta luôn nên tạo instance attribute trong constructor (`__init__`)
#### Truy xuất instance attribute
Với các instance attribute tạo ra như trên, chúng ta có thể truy xuất nó qua tên object trong code ở ngoài class, việc truy xuất là 2 chiều, tức chúng ta có thể gán và thay đổi giá trị.

    class Student:
        def __init__(self, name="Default name", house="Default house"):
            self.name = name
            self.house = house

    student1 = Student()
    print(f"{student1.name} from {student1.house}")
    student1.name = "Anna"
    print(f"{student1.name} from {student1.house}")

### Class Attribute
Hình dung bài toán sau: sau khi tạo class Student, làm thế nào để theo dõi số lượng object đã tạo ra?

Logic đơn giản nhất là tạo ra một biến đếm. Mỗi khi tạo một object mới thì tăng giá trị của biến đếm. Nếu biến đếm và việc tăng giá trị của biến đếm nằm ngoài class thì rất đơn giản. Nhưng nếu chúng ta cần tích hợp logic này vào chính class thì làm như thế nào?

Chúng ta thấy rằng, biến đếm trên không thể phục thuộc vào từng object. Nói cách khác, tất cả các object đều phải dùng chung một biến đếm.

Python cung cấp một một công cụ lá class attribute để thực hiện điều này.

    class Student:
        count = 0

        def __init__(self, name="Default name", house="Default house"):
            self.name = name
            self.house = house
            Student.count += 1


    student1 = Student()
    print(Student.count, student1.count)
    student2 = Student()
    print(Student.count, student2.count)
    student3 = Student()
    print(Student.count, student3.count)

Trong ví dụ này, count là class attribute của class Student, name và house là các instance attribute.

=> Như vậy, class attribute là một biến gắn liền với chính class, có thể được truy xuất từ các object hoặc từ chính class và có giá trị chung cho tất cả các object.

#### Cập nhật giá trị class attribute
Tương tự instance attribute, chúng ta cũng có thể thay đổi giá tị của class attribute.

    class Student:
        count = 0

        def __init__(self, name="Default name", house="Default house"):
            self.name = name
            self.house = house
            Student.count += 1

    student1 = Student()
    print(Student.count, student1.count)
    student2 = Student()
    print(Student.count, student2.count)
    student3 = Student()
    print(Student.count, student3.count)
    Student.count = 0
    print(Student.count, student1.count, student2.count, student3.count)

Output:

1 1
2 2
3 3
0 0 0 0

=> Khi thay đổi giá trị class attribute thông qua Class thì thuộc tính đó ở object cũng bị đổi theo.

Hãy thử trường hợp thay đổi từ object:

    class Student:
        count = 0

        def __init__(self, name="Default name", house="Default house"):
            self.name = name
            self.house = house
            Student.count += 1

    student1 = Student()
    print(Student.count, student1.count)
    student2 = Student()
    print(Student.count, student2.count)
    student3 = Student()
    print(Student.count, student3.count)
    student1.count = 0
    print(Student.count, student1.count, student2.count, student3.count)
    Student.count = 2
    print(Student.count, student1.count, student2.count, student3.count)

Output:
    1 1
    2 2
    3 3
    3 0 3 3
    2 0 2 2

=> Khi thay đổi giá trị class attribute thông qua object thì chỉ có object đó thay đổi, và kể từ đó khi thay đổi từ class thì object đó không bị ảnh hưởng theo.
## Method
Xem xét bài toán điểm danh học sinh:

    class Student:
        count = 0

        def __init__(self, name, house):
            self.name = name
            self.house = house
            Student.count += 1
        
    def attendance(name):
        print(f"{name} is here!")

    student1 = Student("Lan", "Gryffindor")
    student1.check = attendance
    student1.check(student1.name)
    student2 = Student("Minh", "Gryffindor")
    student2.check(student2.name)

Chúng ta có class Student và hàm attendance bên ngoài class.

Ở đây dòng mã `student1.check(student1.name)` sẽ in ra màn hình `Lan is here!` còn dòng mã `student2.check(student2.name)` sẽ báo lỗi `'Student' object has no attribute 'check'`.

Như vậy giống như attribute, cách viết trên không thỏa mãn rằng tất các các học sinh đều có thể thực hiện chức năng điểm danh, mà phải chủ động khai báo bằng cách viết `student1.check = attendance` sau khi đã tạo object.

Để khiến cho các object có cùng các method ngay sau khi khởi tạo, chúng ta có thể khai báo các method trong thân class.

=> Method là một phần của Object (method chính là hành vi của object). Hay nói cách khác, method nằm bên trong class và có thể xử lý dữ liệu được chứa bên trong class.

Khi tạo một class bất kỳ, python tích hợp sẵn một số method, hoặc chúng ta cũng có thể tự tạo các method cho riêng mình.

#### Instance method
Chúng ta sửa đoạn mã trên như sau:

    class Student:
        count = 0

        def __init__(self, name, house):
            self.name = name
            self.house = house
            Student.count += 1

        def attendance(self):
            print(f"{self.name} is here!")

    student1 = Student("Lan", "Gryffindor")
    student1.attendance()
    student2 = Student("Tuan", "Gryffindor")
    student2.attendance()

Ở đây, chúng ta tạo method attendance có tham số là self dùng để chỉ tới một object, trong method, chúng ta truy cập tới attribute name của object.

Method attendance trên đây là một instance method.

Instance method trong Python là những phương thức có khả năng truy xuất trạng thái của object (trạng thái của object trong Python được lưu trữ trong các instance attribute)

Lưu ý:
- Danh sách tham số của instance method tương tự của hàm, nhưng cần có từ khóa `self`. Nếu có nhiều tham số, `self` phải là tham số đầu tiên được liệt kê.
- Có thể truy xuất attribute trong chính instance method thông qua từ khóa `self`.

#### Class method
Trong phần trước chúng ta đã làm quen với class attribute – loại biến chứa giá trị đặc trưng cho class và gắn với class, thay vì gắn với object. Một ví dụ đã được đưa ra để minh họa là đếm số lượng object của class đã được khởi tạo trong chương trình.

Class method cũng có cùng ý tưởng với class attribute. Class method là những phương thức đặc trưng cho class và gắn liên với class, thay vì gắn với object. Class method có nhiệm vụ xử lý dữ liệu lưu trong class attribute.

Ví dụ:

    class Student:
        count = 0

        def __init__(self, name, house):
            self.name = name
            self.house = house
            Student.count += 1
        
        def attendance(self):
            print(f"{self.name} is here!")

        @classmethod
        def show_count(cls):
            print(cls.count)
    

    student1 = Student("Lan", "Gryffindor")
    student1.show_count()
    student2 = Student("Tuan", "Gryffindor")
    student2.show_count()
    Student.show_count()

`@classmethod` là một decorator. Decorator là một loại hàm đặc biệt có thể nhận một hàm khác làm tham số để bổ sung tính năng cho hàm tham số đó. Chúng ta sẽ quay lại học chi tiết về decorator trong phần dưới.

Để tạo ra class method, chúng ta sử dụng decorator @classmethod.

Lưu ý:
- Class method cũng bắt buộc phải có một biến đặc biệt trong danh sách tham số: biến cls (viết tắt của class). Biến này có vai trò tương tự như biến self của instance method. Điểm khác biệt nằm ở chỗ biến cls chứa thông tin về chính class.

Trong ví dụ trên, count là một class attribute – chứa thông tin về chính class. Do vậy, có thể truy xuất count qua biến cls. Trên thực tế, bạn có thể hình dung truy xuất qua biến cls cũng chính là truy xuất qua tên class. Tức là `cls.count` tương đương với `Student.count`.

Ngoài Instance method và class method, python còn có static method. Chúng ta sẽ tìm hiểu ở những bài sau.

## Public, protected, private trong Python
Trong các ngôn ngữ hướng đối tượng truyền thống như C++, Java hay C#, mỗi thành viên của object về một trong các mức truy cập sau:
- (1) public: tự do truy cập, không có giới hạn gì.
- (2) protected: chỉ class con và trong nội bộ class mới có thể truy cập.
- (3) private: giới hạn truy cập trong nội bộ class.

Trong Python không có khái niệm về kiểm soát truy cập các thành viên như vậy. Hoặc cũng có thể nói rằng mặc định mọi thành viên của class trong Python đều là public. Nghĩa là code ngoài class có thể tự do truy cập các thành viên này.

Để mô phỏng lại hiệu quả của việc kiểm soát truy cập, Python sử dụng loại kỹ thuật có tên gọi là xáo trộn tên (name mangling)

Kỹ thuật này quy ước rằng:
- Nếu muốn biến chỉ được sử dụng trong nội bộ class và các class con (mức truy cập là protected), tên biến cần bắt đầu là _ (một dấu gạch chân);
- Nếu muốn biến chỉ được sử dụng trong nội bộ class (mức truy cập private), tên biến cần bắt đầu là __ (hai dấu gạch chân).

Thực ra, loại kỹ thuật này không làm thay đổi được việc truy cập thành viên của class. Nó đơn thuần là chỉ báo để lập trình viên và IDE biết ý định sử dụng của thành viên đó.

    class Student:
        def __init__(self):
            self.__private = False

    s = Student()

Ví dụ, trong class Student như trên, thực tế biến __private  không hề trở thành private. IDE sẽ trợ giúp che đi biến này trong phần nhắc code. Tuy nhiên bạn vẫn có thể truy xuất nó như bình thường:

    class Student:
        def __init__(self):
            self.__private = False

    s = Student()
    s.__private = True

#### Method \__str__
Đây là một method được tích hợp sẵn bởi python.

Với code trước đó, hay thử sửa đổi hàm main để in ra object đã tạo:

    def main():
        student = get_student()
        print(student)

Output:

    <__main__.Student object at 0x000002AA47064FD0>

Python tích hợp sẵn method `__str__` để in ra một số nội dung của object.

    class Student:
        def __init__(self, name, house, patronus):
            self.name = name
            self.house = house
            self.patronus = patronus

        def __str__(self):
            return f"{self.name} from {self.house}"


    def main():
        student = get_student()
        print(student)


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return Student(name, house, patronus)


    if __name__ == "__main__":
        main()

Output:

    Name: Anna
    House: a1
    Patronus: 5
    Anna from a1

## Property
Property là một loại thành viên đặc biệt trong class Python cho phép truy xất và kiểm soát truy xuất một (instance) attribute cụ thể. Property rất quan trọng và được khuyến khích sử dụng khi xây dựng các class chuyên để chứa dữ liệu. Python cung cấp một số cách khác nhau để khai báo property.

### Mô hình getter/setter
Trong class python, dù được quy ước cách viết __ và _ dùng để chỉ những attribute hoặc mehtod private và protected trong class, nhưng về bản chất, mọi thành viên của class đều là public và có thể truy xuất tự do.

Điều này sinh ra một vấn đề là kiểm sóat dữ liệu. Ví dụ: tuổi của con người không thể âm.

Để kiểm soát việc nhập xuất dữ liệu cho các opject, không chỉ python, mà các ngôn ngữ lập trình hướng đối tượng thường sử dụng mô hình getter/setter. Ví dụ trên class Student:

Theo mô hình này, những biến đăt là private (viết `__` ngay trước tên biến) là những biến cần được kiểm soát dữ liệu. Tức là nó không nên được truy xuất và thay đổi bên ngoài class. Trong python chúng ta sử dụng hai dấu gạch chân `__` cho biến private khi khai báo attribute đó trong hàm tạo `__init__()`.

Ví dụ:

    class Student:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age

        def set_age(self, age: int):
            if age > 0:
                self.__age = age

        def get_age(self):
            return self.__age

        def get_name(self):
            return self.__name

        def set_name(self, name: str):
            self.__name = name.title()

        def __str__(self):
            return f'{self.__name} {self.__age}'

    s1 = Student('tom', 10)
    print(s1)
    s1.set_name('bim bim')
    print(s1)
    s1.set_age(22)
    print(s1)
    s1.set_age(-1)
    print(s1)

Ứng với mỗi một biến private, chúng ta sẽ tạo 2 method get/set để nhập và xuất dữ liệu. Ví dụ với biến `__age`, chúng ta xây dựng method `get_age` để trả dữ liệu chứa trong `__age` và `set_age` để nhập dữ liệu cho `__age`. Cặp method get/set như vậy được gọi là getter và setter. Tương tự với attribute `__name` chúng ta cũng xây dựng hai method để nhập xuất dự liệu là `set_name` và `get_name`.

Trong getter và setter, tùy vào yêu cầu kiểm soát mà chúng ta thực hiện những logic riêng. Ví dụ trong set_age(), chúng ta chỉ gán giá trị cho `__age` khi giá trị truyền vào lúc tạo object lớn hơn 0. Hoặc trong set_name() chúng ta sẽ viết hoa các chữ cái đầu của tên được truyền vào trước khi gán cho `__name`.

Lưu ý: 
- Việc sử dụng `__` và `_` để hạn chế quyền truy cập chỉ là quy ước, python không cấm chúng ta cố tình truy cập, tuy nhiên nó là một cách triển khai tệ.
- Các ngôn ngữ lập trình hướng đối tượng như Java, C++ khuyến khích chúng ta không bao giờ để lộ các thuộc tính của class. Thay vào đó sẽ cung cấp getter và setter methods để truy cập từ ngoài vào. Đó là lý do vì sao những thiết kế OOP tốt trong python thường sử dụng các attribute với `__` hoặc `_` để giới hạn quyền truy cập, dù nó chỉ nằm trên quy ước.
- Mô hình getter, setter vừa giưới thiệu là một thiết kế OOP tệ vì nó không đảm bảo tính đóng gói của đối tượng. Đồng thời sử dụng mô hình này thì việc lấy và cập nhật dữ liệu trở nên cồng kềnh vì cần quá nhiều method. Vì vậy tiếp theo chúng ta sẽ tiếp cận một mô hình khác là Property và hàm property().

### Property và hàm property() trong trong python
Property đại diện cho một chức năng trung gian giữa một method và một attribute bình thường. Tức là nó cho phép chúng ta tạo method nhưng hoạt động như một attribute. Với các property, chúng ta có thể thay đổi cách tính toán attribute.

property() là một cách Pythonic để tránh các method getter, setter trong code. Hàm này cho phép biến các class attribute thành properties.

property() là một build-in function.

Full signature của property():

    property(fget=None, fset=None, fdel=None, doc=None)

Ba đối số đầu tiên nhận các function object (các function trong python cũng là các object), cụ thể:
- fget: method trả về giá trị của managed attribute.
- fset: method cho phép chúng ta đặt giá trị cho managed attribute.
- fdel: method xác định cách xử lý khi xóa managed attribute.
- doc: string đại diện cho docstring của property.

Chú ý:
- Docstring là một dạng chú thích nhiều dòng hay xuất hiện ở đầu một file Python, sau một dòng định nghĩa lớp, hàm. Đây cũng là một trong những chuẩn quy ước về định dạng, trình bày code Python. Python cung cấp method hàm help() để hỗ trợ đọc chuỗi docstring.
- 3 đối số đầu tiên nhận về các function objects, vì vậy khi truyền vào không cần dấu ngoặc đơn.

Chúng ta có thể sử dụng property như một function hoặc một decorator để xấy dựng property cho mình.

### Tạo property bằng hàm property()
Chúng ta có thể tạo các property bằng hàm property() với các đối số thích hợp truyền vào hàm và gán giá trị màn nó trả về cho một class attriute. Các đối số cho hàm property() là không bắt buộc, tức có thể gọi hàm này mà không truyền gì cả.

Dưới đây là một ví dụ cho việc tạo class Circle có property để quản lý bán kính.

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        def _get_radius(self):
            print("Get radius")
            return self._radius

        def _set_radius(self, value):
            print("Set radius")
            self._radius = value

        def _del_radius(self):
            print("Delete radius")
            del self._radius

        radius = property(
            fget=_get_radius,
            fset=_set_radius,
            fdel=_del_radius,
            doc="The radius property."
        )

Ở đây chúng ta có class Circle, một hàm constructor  `__init__()` nhận đối số radius và lưu nó vào protected attribute có tên là `_radius`. Sau đó chúng ta có 3 public method là:
- _get_radius() trả về giá trị hiện tại của instance attribute _radius
- _set_radius() nhận đối số `value` và gán nó cho instance attribute _radius
- _del_radius() xóa instance attribute _radius

Khi đã có 3 method này, chúng ta tạo một class attribute có tên là radius để lưu trữ property object.

Chạy đoạn mã sau:

    from circle import Circle

    c1 = Circle(20)
    print(c1.radius)
    c1.radius = 11
    print(c1.radius)
    del c1.radius
    print(c1.radius)

Ở đây, property radius đã giúp che giấu protected instance attribute _radius. Lúc này _radius là một managed attribute trong class. Chúng ta có thể truy cập và chỉ định giá trị cho radius trực tiếp, mỗi khi làm việc đó, python tự động gọi hàm _get_radius() và _set_radius() mà chúng ta đã truyền vào. Còn khi thực hiện `del c1.radius`, python tự động gọi _del_radius() cho chúng ta.

Như vậy property là các class attribute, quản lý các instance attribute. Chúng ta có thể coi property là tập hợp các method dùng để quản lý một instance attribute lại với nhau.

Chạy đoạn mã sau để thấy các method chúng ta đã truyền vào khi gọi hàm property và gán object trả về cho attribute radius:

    from circle import Circle


    print(Circle.radius.fget)
    print(Circle.radius.fset)
    print(Circle.radius.fdel)
    print(dir(Circle.radius))
    print(Circle.radius)

### Tạo property bằng decorator property
Có một cách ngắn gọn hơn để tạo property trong python là sử dụng decorator property. Cú pháp này được thêm vào python từ python 2.4. Và ngay này cách này là cách phổ biến nhất được sử dụng để tạo property.

Cú pháp sử dụng decorator là sử dụng ký hiệu `@` kèm tên của decorator trước phần định nghĩa hàm/method mà chúng ta muốn dùng decorator.

Ví dụ:

    @decorator
    def func(a):
        return a

Cú pháp này tương đương với:

    def func(a):
        return a

    func = decorator(func)

Hàm property() cũng có thể hoạt động như một decorator, vì vậy chúng ta có thể sử dụng cú pháp @property để tạo các property một cách nhanh chóng.

Ví dụ:

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            """The radius property."""
            print("Get radius")
            return self._radius

        @radius.setter
        def radius(self, value):
            print("Set radius")
            self._radius = value

        @radius.deleter
        def radius(self):
            print("Delete radius")
            del self._radius

Code lúc này so với lúc dùng hàm property ngắn gọn và clean hơn. Bây giờ chúng ta không tạo và sử dụng các method như _get_radius(), _set_radius() và _del_radius() nữa. Mà bây giờ chúng ta có ba method có tên trùng với tên của property.

Dưới đây là cách nó hoạt động:

Khi sử dụng decorator để tạo property, chúng ta cần tạo puplic method đầu tiên sử dụng public name cho managed attribute, là `radius` trong đoạn mã này. Method cũng chính là method getter.

Sau đó chúng ta xác định method setter và del cho property `radius`. Trong trường hợp này, thay vì sử dung decorator là @property, chúng ta sử dụng decorator lần lượt là @radius.setter và @radius.deleter.

Chú ý:
- Decorator @property phải dùng cho method getter
- Các method setter và deleter phải được dùng decorator là @ten_property.setter và @ten_property.deleter
- Vì python không bảo vệ dữ liệu chặt chẽ, nên ngay cả khi chúng ta tạo các property để dấu đi các non-public attribute thì chúng ta vẫn có thể trực tiếp thay đổi giá trị của các attribute đó bên ngoài class mà không thông qua property. Nhưng đó là một cách viết mã tệ.

### Property chỉ...
Chúng ta có thể tạo ra các property chỉ đọc, hoặc chỉ cho đọc và ghi, hoặc chỉ ghi.

Ví dụ cho một property chỉ đọc:

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            """The radius property."""
            print("Get radius")
            return self._radius

Ở đây chúng ta tạo property radius, và chỉ tạo method getter cho nó, không có method setter và deleter. Vì vậy khi cố gắng đặt lại giá trị cho _radius attribute thông qua đặt lại giá trị cho radius property thì chương trình sẽ báo lỗi "property 'radius' of 'Circle' object has no setter".

Kiểm tra nó như sau:

    from circle3 import Circle

    c = Circle(22)
    print(c.radius)
    c.radius = 11 # property 'radius' of 'Circle' object has no setter

Ví dụ cho property chỉ viết:

    import hashlib
    import os

    class User:
        def __init__(self, name, password):
            self.name = name
            self.password = password

        @property
        def password(self):
            raise AttributeError("Password is write-only")

        @password.setter
        def password(self, plaintext):
            salt = os.urandom(32)
            self._hashed_password = hashlib.pbkdf2_hmac(
                "sha256", plaintext.encode("utf-8"), salt, 100_000
            )

Ở đây hãy chú ý một điều là chúng ta không tạo attribute non-public ở method constructor mà tạo public attribute, đồng thời tạo property cùng tên. Bởi vì chúng ta muốn ngay khi tạo object mới, thì phải đi qua setter để hash mật khẩu của người dùng. Và chúng ta lưu string đã được mã hóa vào một non-public attribute có tên là _hashed_password.

Cùng xem xét một ví dụ khác.

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, value):
            try:
                self._x = float(value)
                print("Validated!")
            except ValueError:
                raise ValueError('"x" must be a number') from None

        @property
        def y(self):
            return self._y

        @y.setter
        def y(self, value):
            try:
                self._y = float(value)
                print("Validated!")
            except ValueError:
                raise ValueError('"y" must be a number') from None

Ở đây chúng ta cũng tạo property x, y có tên trùng với attribute được tạo trong hàm tạo constructor. Bởi vì chúng ta muốn ngay từ lúc tạo object thì chương trình phải kiểm tra xem giá trị đối số truyền vào có phải float không. Và chúng ta lưu nó vào các instance attribute non-public là `_y` và `_x`.

Chú ý: những property được tạo bằng hàm property() cũng có thể chỉ là property chỉ đọc, chỉ ghi,...

Ví dụ:

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        def _get_radius(self):
            print("Get radius")
            return self._radius

        radius = property(
            fget=_get_radius,
            doc="The radius property."
        )

Ở ví dụ này, property radius chỉ đọc.


## Static method
Ngoài class method, instance method, python còn hỗ trợ static method.

Static method là loại method hoàn toàn tự do, không ràng buộc dữ liệu với class hay object. Chúng được đặt trong class vì một lý do nào đó.

Để tạo ra static method trong class python, chúng ta sử dụng decorator @staticmethod.

Ví dụ:

    class User:
        count = 0
        def __init__(self, fname='', lname='', age=18):
            self.fname = fname
            self.lname = lname
            self.age = age
            User.count += 1

        def print(self):
            print(f'{self.fname} {self.lname} ({self.age} years old)')

        @property
        def full_name(self):
            return f'{self.fname} {self.lname}'

        @classmethod
        def print_count(cls):
            print(f'{cls.count} objects created')

        @staticmethod
        def birth_year(age: int) -> int:
            from datetime import datetime as dt
            year = dt.now().year
            return year - age


    if __name__ == '__main__':
        trump = User('Donald', 'Trump', 22)
        trump.print()
        print(trump.full_name)
        print(User.count)
        User.print_count()
        print(User.birth_year(37))
        print(trump.birth_year(37))

Ở đây chúng ta có một static method là birth_year. Method này không nhận tham số `self` hay `cls`, nhưng có thể nhận các tham số tùy ý khác. Bởi vậy nó không dùng bất kỳ thông tin nào từ object hay class, tức nó bị hạn chế loại dữ liệu mà nó có thể truy cập.

Chúng ta có thể gọi static method qua class lẫn object.

    print(User.birth_year(37))
    print(trump.birth_year(37))

## Cách hoạt động của instance method, class method, static method
Chúng ta có ví dụ sau:

    class MyClass:
        def method(self):
            return 'instance method called', self

        @classmethod
        def classmethod(cls):
            return 'class method called', cls

        @staticmethod
        def staticmethod():
            return 'static method called'

### Instance method
Cách gọi instance method:
- Từ object
- Không thể gọi từ class

Ví dụ:
    
    obj1 = MyClass()
    obj1.method()

Trong định nghĩa của instance method, nó nhận tham số self, chỉ tới object.

Khi gọi, sẽ chuyển obj1 vào vị trí tham số self.
Trong instance method, có thể truy cập tới và chỉnh sửa class attribute.

### Class method
Cách gọi Class method:
- Từ class
- Không thể gọi từ class

Trong định nghĩa của class method, nó nhận tham số cls, chỉ tới class.

Cách gọi:

    MyClass.staticmethod()
    obj1 = MyClass()
    obj1.staticmethod()

Có thể gọi static method thông qua class và object, nhưng phía sau, python vẫn tự động hạn chế quyền truy cập và chỉnh sửa tới các class attribute vào instance attribute.

Trong static method, KHÔNG thể truy cập tới và chỉnh sửa instance attribute và class attribute.

### Static method
Cách gọi Static method:
- Từ class lẫn object

Trong định nghĩa của class method, nó nhận tham số cls, chỉ tới class.

    MyClass.classmethod()
    obj1 = MyClass()
    obj1.classmethod()

Khi gọi bằng cách `MyClass.classmethod()`, sẽ chuyển `MyClass` vào vị trí tham số `cls`. Nếu gọi bằng cách `obj1.classmethod()`, python sẽ tự động chuyển lấy về đối tượng class để truyền vào cho tham số `cls`.

Trong class method, KHÔNG thể truy cập tới và chỉnh sửa instance attribute, có thể truy cập và chỉnh sửa class attribute.

Chú ý: từ khóa `cls` và `self` không phải quy định bắt buộc, chúng ta có thể sử dụng các từ khóa khác như `cls_name`, `obj_name` thay thế.
## Kế thừa
Kế thừa (inheritance) là một công cụ rất mạnh và được sử dụng rất nhiều trong lập trình hướng đối tượng. Nó cho phép tạo một class mới từ một class sẵn có, qua đó có thể tái sử dụng code và giảm thiểu việc lặp code.

Ví dụ chúng ta có một class User, và chúng ta tạo một class Student kế thừa từ class User. Điều này có nghĩa là Dog kế thừa cách triển khai của Animal.

Cùng xem xét một ví dụ khác như sau:

    class User:
        count = 0
        def __init__(self, fname='', lname='', age=18):
            self.fname = fname
            self.lname = lname
            self.age = age
            User.count += 1

        def print(self):
            print(f'{self.fname} {self.lname} ({self.age} years old)')

        @property
        def full_name(self):
            return f'{self.fname} {self.lname}'

        @classmethod
        def print_count(cls):
            print(f'{cls.count} objects created')

        @staticmethod
        def birth_year(age: int) -> int:
            from datetime import datetime as dt
            year = dt.now().year
            return year - age


    class Student(Person):
        def __init__(self, fname='', lname='', age=18, group='', specialization=''):
            super().__init__(fname, lname, age)
            self.group = group
            self.specialization = specialization

        def print(self):
            super().print()
            print(f'Group {self.group}/{self.specialization}')

        @property
        def academic_info(self):
            return f'Group {self.group}, Specialization of {self.specialization}'


    if __name__ == '__main__':
        trump = Student('Donald', 'Trump', 22, '051311', 'Computer science')
        trump.print()
        print(trump.full_name)
        print(Student.count)
        Student.print_count()
        print(Student.birth_year(37))
        print(trump.academic_info)

Output:

    Donald Trump (22 years old)
    Group 051311/Computer science
    Donald Trump
    1
    1 objects created
    1986
    Group 051311, Specialization of Computer science

Trong ví dụ trên chúng ta đã xây dựng hai class: User và Student.

Trong class Person chúng ta tạo các instance attribute `fname`, `lname`, `age` trong hàm tạo, một class attribute `count`, một class method, một static method và một property.

Chúng ta xây dựng class Student kế thừa từ class User. Trong class này chúng ta chỉ định nghĩa hàm constructor (`__init__`) và method `print()`. Chúng ta tạo object `trump`, nhưng từ object `trump` chúng ta vẫn truy xuất được tới các member của class User như property full_name, class method print_count và static method birth_year.

Khi này chúng ta gọi mối quan hệ giữa class User và class Student là mối quan hệ kế thừa. Trong đó Student kế thừa User. User là lớp cha hay lớp cơ sở, còn Student là lớp con hay lớp dẫn xuất.

### Cú pháp
Cú pháp khai báo kế thừa trong python:

    class ChildClass(ParentClass):
        # code

Khi kế thừa, class con kế thừa được tất cả mọi thứ từ lớp cha.

Python cho phép đa kế thừa, tức là một lớp con kế thừa nhiều lớp cha.
- Tuy nhiên việc này không được khuyến khích, vì nó khó kiểm soát và dự đoán kết quả khi 2 class cha có các member giống nhau.

### Ghi đè khi kế thừa
Việc ghi đè chính là việc lớp con kế thừa lớp cha nhưng có thể thay đổi các hành vi được kế thừa.

Việc này được thực hiện bằng cách lớp con có quyền tạo một phương thức giống hệt với phương thức của lớp cha.

Bởi đôi khi những định nghĩa trong class cha lại không phù hợp với mục đích sử dụng của class con.

Trong ví dụ trên, class con Student đã ghi đè (override) method `print()` của class cha User.

Vì vậy khi chương trình gọi lệnh `print()` từ một object của class Student, nó sẽ tìm đến method `print()` mới override của class Student.

Ở đây chúng ta có câu lệnh `super().print()`, với câu lệnh này, python sẽ gọi tới hàm print() của class cha, trước khi chạy câu print kế tiếp.

### Ghi đè hàm tạo
Là việc chúng ta tạo một class con kế thừa một class cha, đồng thời muốn định nghĩa lại hàm constructor của riêng mình.

Thông thường nếu không cần ghi đè hàm tạo, khi tạo lớp con, chúng ta không cần xây dựng hàm `__init__` ở lớp con.

Khi ghi đè hàm tạo, chúng ta cần xây dựng lại hàm `__init__`, và có một điều bắt buộc trong hàm tạo của lớp con là phải gọi lại hàm tạo của lớp cha trông qua phương thức `super()`.

Trong ví dụ trên, chúng ta đã ghi đè hàm tạo như sau:

    class Student(Person):
        def __init__(self, fname='', lname='', age=18, group='', specialization=''):
            super().__init__(fname, lname, age)
            self.group = group
            self.specialization = specialization

### Private và protected trong kế thừa
Khi một lớp con kế thừa bởi một lớp cha, thì từ lớp con chỉ có thể truy cập các member public và protected được kế thừa từ lớp cha, không thể truy cập các member private từ lớp cha.

Ví dụ:

    class Parent:
        count = 0
        def __init__(self):
            self._protected = True
            self.__private = True

    class Child(Parent):
        ...

    c1 = Child()
    print(c1._protected) # True
    print(c1.__private) # 'Child' object has no attribute '__private'

Ở đoạn mã trên, khi chúng ta cố gắng in ra `c1.__private`, chương trình sẽ báo lỗi, vì __private là private member của class Parent.
