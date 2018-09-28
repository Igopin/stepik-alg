#!/usr/bin/python3
def pack_backpack(max_volume, items):
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    current_volume = 0
    total = 0

    for cost, vol in items:
        if vol <= max_volume - current_volume:
            current_volume += vol
            total += cost
        else:
            total += (max_volume - current_volume) * cost / vol
            break

    return total

def main():
    n, volume = map(int, input().split())

    items = []
    for _ in range(n):
        item = list(map(int, input().split()))
        items.append(tuple(item))

    print("{:.3f}".format(pack_backpack(volume, items)))

if __name__ == "__main__":
    main()
