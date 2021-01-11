bottles = "green bottles sitting on the wall"
numbers = ["ten ", "nine ", "eight ", "seven ", "six ", "five ", "four ", "three ", "tho ", "one "]

for i in range(10):
    print(numbers[i] + bottles)
    print(numbers[i] + bottles)
    print("And if one green bottle should accidentally fall")
    if i != 9:
        print("There would be" + numbers[i + 1] + bottles)
    else:
        print("There would be No" + bottles + "THE END")
