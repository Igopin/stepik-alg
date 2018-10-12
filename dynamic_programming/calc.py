#!/usr/bin/python3

def calculate(num):
    dynamic = [0, 1, 1] + [0 for i in range(num - 3)]

    for n in range(3, len(dynamic)):
        tmp = [dynamic[n - 1]]
        if (n + 1) % 2 == 0:
            tmp.append(dynamic[(n - 1) // 2])
        if (n + 1) % 3 == 0:
            tmp.append(dynamic[(n - 2) // 3])

        dynamic[n] = 1 + min(tmp)

    if len(dynamic) <= 3:
        dynamic = dynamic[:num]

    return dynamic


def restore(dynamic):
    print(dynamic)
    ind = len(dynamic) - 1
    res = [ind + 1]

    while ind > 0:
        tmp = [(ind - 1, dynamic[ind - 1])]
        if (ind + 1) % 2 == 0:
            i = (ind - 1) // 2
            tmp.append((i, dynamic[i]))
        if (ind + 1) % 3 == 0:
            i = (ind - 2) // 3
            tmp.append((i, dynamic[i]))
        ind, _  = min(tmp, key=lambda x: x[1])
        res.append(ind + 1)
    return res[::-1]



def main():
    number = int(input())
    dynamic = calculate(number)
    print(dynamic[-1])
    print(*restore(dynamic))

if __name__ == "__main__":
    main()
