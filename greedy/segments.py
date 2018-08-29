#!/usr/bin/python3
def find_points(segments):
    points = []

    segments = sorted(segments, key=lambda x: x[1])
    num_of_seg = len(segments)

    i = 0
    while i < num_of_seg:
        points.append(segments[i][1])
        i =+ 1

        while i < num_of_seg:
            if segments[i][0] > points[-1]:
                break
            i += 1
        
    return points

def main():
    n = int(input())

    segments = []
    for i in range(n):
        segment = list(map(int, input().split()))
        segments.append(tuple(segment))

    points = find_points(segments)
    print(len(points))
    print(' '.join(str(e) for e in points))

if __name__ == "__main__":
    main()
