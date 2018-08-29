#!/usr/bin/python3
def decompose(number):
    acc = 0
    numbers = []

    if number <= 2:
        return [number]

    for i in range(1, number):
        if acc + i <= number:
            numbers.append(i)
            acc += i
        else:
            acc -= numbers.pop()
            numbers.append(number - acc)
            break

    return numbers
        
def main():
    number =int(input())

    numbers = decompose(number)

    print(len(numbers))
    print(" ".join(str(num) for num in numbers))

if __name__ == "__main__":
    main()
