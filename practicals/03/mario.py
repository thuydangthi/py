"""
Hãy viết chương trình đệ quy để in ra hình kim tự tháp ở bài tập mario ở prac 02
"""

def print_row(height, n):
    print(" "*(n - 1) + "#"*(height - n + 1) + " " + "#"*(height - n + 1) + " "*(n - 1))
    if n > 1:
        print_row(height, n - 1)

def main():
    height = int(input("Height: "))

    while height <= 0:
        print("Invalid height")
        height = int(input("Height: "))

    print_row(height=height, n=height)

main()
