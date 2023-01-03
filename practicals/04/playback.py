import time

s = "This is our week on functions"

l = ['This', 'is', 'our', 'week', 'on', 'functions']

for t in l:
    print(t, end="")
    print(".", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.5)
