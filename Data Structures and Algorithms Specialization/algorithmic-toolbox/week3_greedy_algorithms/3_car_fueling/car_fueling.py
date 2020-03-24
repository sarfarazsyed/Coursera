# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    start = 0
    count = 0
    for i in range(len(stops) - 1):
        dis_start_fil = (stops[i] - start)
        dis_f_stop_start = stops[i + 1] - start
        if dis_start_fil > tank:
            break
        if dis_start_fil <= tank < dis_f_stop_start:
            start = stops[i]
            count += 1

    if distance - start <= tank:
        return count
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
