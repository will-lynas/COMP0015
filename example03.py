def enough_time(hour1, minute1, hour2, minute2):
    all1 = hour1 * 60 + minute1
    all2 = hour2 * 60 + minute2

    diff = all2 - all1

    if diff < 0:
        diff = 0

    enough_time = diff >= 45

    return (enough_time, diff)


assert(enough_time(11, 00, 11, 59) == (True, 59))
assert(enough_time(12, 30, 13, 00) == (False, 30))
assert(enough_time(12, 30, 13, 15) == (True, 45))
assert(enough_time(14, 20, 17, 2) == (True, 162))
assert(enough_time(12, 30, 9, 30) == (False, 0))
assert(enough_time(12, 00, 11, 55) == (False, 0))
