# Lập trình hướng đối tượng
Có nhiều mô hình lập trình khác nhau. Cho đến thời điểm này, chúng ta đã làm việc theo quy trình step-by-step.
Trong Python, Lập trình hướng đối tượng (OOPs) là một mô hình lập trình sử dụng các đối tượng và lớp (object và class).

## Bài toán cơ sở
Chúng ta có một bài toán đơn giản như sau:

    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}")

Dựa trên kinh nghiệm từ những buổi trước, chúng ta có thể tạo các hàm để trừu tượng hóa các phần của chương trình này như sau:

    def main():
        name = get_name()
        house = get_house()
        print(f"{name} from {house}")


    def get_name():
        return input("Name: ")


    def get_house():
        return input("House: ")


    if __name__ == "__main__":
        main()

Chúng ta có thể đơn giản hóa hơn nữa chương trình này bằng cách lưu trữ học sinh dưới dạng tuple. Một tuple là một collection có thứ tự, không thể thay đổi. Không giống như một list, a tuple không thể sửa đổi được. Về ý tưởng chung, chúng ta đang trả lại hai giá trị.

    def main():
        name, house = get_student()
        print(f"{name} from {house}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return name, house


    if __name__ == "__main__":
        main()

Lưu ý cách return 2 value ở hàm get_student.

Bây giờ chúng ta sẽ đóng gói tuple, sao cho chúng ta có thể trả lại cả hai item cho một biến có tên student, chúng ta có thể sửa đổi mã trên như sau.

    def main():
        student = get_student()
        print(f"{student[0]} from {student[1]}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return (name, house)


    if __name__ == "__main__":
        main()

Lưu ý:
- Cách viết (name, house) là một cách viết rõ ràng để người đọc hiểu chúng ta đang trả về một tuple có 2 giá trị.
- Cách chúng ta lập chỉ mục của tuples bằng cách sử dụng student[0] hoặc student[1].

Vì tuples là bất biến, nên chúng ta không thể thay đổi các giá trị trong tuple hay thêm, xóa item trong tuple.

Vì vậy chúng ta có thể chuyển sang list, để có thể linh hoạt thêm, sửa, xóa các item.

    def main():
        student = get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return [name, house]


    if __name__ == "__main__":
        main()

- Dĩ nhiên, các list có thể thay đổi được, nên ở đây cần cân nhắc giữa sự linh hoạt và tính bảo mật cho code.

Ở chương trình này, chúng ta cũng có thể dùng một dictionary như sau:

    def main():
        student = get_student()
        print(f"{student['name']} from {student['house']}")


    def get_student():
        student = {}
        student["name"] = input("Name: ")
        student["house"] = input("House: ")
        return student


    if __name__ == "__main__":
        main()

Khi cần sửa thông tin học sinh chúng ta có thể làm như sau:

    def main():
        student = get_student()
        if student["name"] == "Padma":
            student["house"] = "Ravenclaw"
        print(f"{student['name']} from {student['house']}")


    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return {"name": name, "house": house}


    if __name__ == "__main__":
        main()

## OOP
Lập trình hướng đối tượng (OOP) là một kỹ thuật lập trình cho phép lập trình viên tạo ra các đối tượng trong code nhằm trừu tượng hóa các đối tượng.

Trong lập trình OOP, có các khái niệm chính sau:
- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

### Class
Class là gì?

Class là một trong những khái niệm đầu tiên và chủ chốt khi nhắc đến lập trình hướng đối tượng.

Một class, lớp, là một nguyên mẫu mà từ đó các đối tượng, hay object được tạo ra. 

Chúng ta có thể sửa đổi code phía trên của mình để triển khai một class có tên là Student:

    class Student:
        ...


    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")


    def get_student():
        student = Student()
        student.name = input("Name: ")
        student.house = input("House: ")
        return student


    if __name__ == "__main__":
        main()

- Theo quy ước, tên class cần  Studentđược viết hoa. Hơn nữa, hãy lưu ý ý ...nghĩa đơn giản là sau này chúng ta sẽ quay lại để hoàn thành phần mã đó của mình. Hơn nữa, lưu ý rằng trong get_student, chúng ta có thể tạo một studentlớp of Studentbằng cách sử dụng cú pháp student = Student(). Hơn nữa, lưu ý rằng chúng tôi sử dụng “ký hiệu dấu chấm” để truy cập các thuộc tính của biến này studentcủa lớp Student.
Nhưng trường hợp có đến trăm cái ô tô, rồi chúng ta muốn tương tác với từng cái ô tô để thực hiện đổ xăng, lái xe, bảo mật thông tin xe,... thì việc dùng các cấu trúc dữ liệu trên mang lại nhiều hạn chế và bất tiện. Đó là một trong những lý do chúng ta sử dụng class.

Một số đặc điểm của class trong python:
- Các class được định nghĩa bởi từ khóa `class`.
- Một class có thể có một hay nhiều thuộc tính, thuộc tính là các biến của một lớp.
- Một class có thể có một hay nhiều method, method là các phương thức mà chúng ta có thể qua đó, thao tác với object được tạo ra từ class.

#### Cú pháp để tạo một class
Cú pháp:

    class ClassName:
        # code

Ví dụ: Tạo một class trống trong python

    class Car:
        pass # lệnh giữ chỗ

Lưu ý: theo chuẩn PEP8 về đặt tên của lớp (class) thì nên được viết theo kiểu CapWords. Ví dụ là AnonymousUser, SuperUser,...

#### Objects
Objects hay các đối tượng, là các thực thể cụ thể được tạo ra từ một nguyên mẫu class.

Một object bao gồm:
- Identity: mã định danh của đối tượng, để phân biệt đối tượng này với đối tượng khác.
- State: được biểu diễn bởi các thuộc tính - attribute.
- Behavior: được biểu diễn bởi các phương thức - method.

Ví dụ: tạo đối tượng

    car1 = Car()

Điều này sẽ tạo một đối tượng có tên là car1 của lớp Car được định nghĩa ở trên.

Để hiểu state, behavior và identity, chúng ta hãy lấy ví dụ về class Car (đã giải thích ở trên). 

- Identity là mã định danh, chúng ta có thể truy cập nó bằng hàm `id()`:

        id(car1)

- State hoặc Thuộc tính có thể được coi là dòng xe, màu xe, số km đã đi,... của car1.
- Behavior có thể được coi là các hành vi chạy xe, đổ xăng cho xe,...
#### Attribute

### Polymorphism
### Encapsulation
### Inheritance
### Data Abstraction