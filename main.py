def list_print(iterable):
    iterable = list(iterable)
    list_display = '['
    for index, item in enumerate(iterable):
        if not index:
            list_display += str(item)
        else:
            list_display += f', {item}'
    list_display += ']'
    return list_display


class Point:
    def __init__(self, position):
        self.position = position
        self.x = position % 3
        self.y = position // 3

    def dX(self, point):
        return abs(self.x - point.x)

    def dY(self, point):
        return abs(self.y - point.y)

    def __str__(self):
        return str(self.position)


class Pattern:
    map = [Point(position) for position in range(9)]

    def __init__(self):
        self.track = []

    def on_track(self, point):
        return self.track.count(point)

    def valid(self, cp, np):  # cp : current_point, np : next_point
        check = (np is not cp and not self.on_track(np) and
                 ((cp.dX(np) == 1 or cp.dY(np) == 1) or
                  ((cp.dX(np) == 2 and cp.dY(np) == 0) and self.on_track(self.map[1 + cp.y * 3])) or
                  ((cp.dX(np) == 0 and cp.dY(np) == 2) and self.on_track(self.map[cp.x + 3])) or
                  ((cp.dX(np) == 2 and cp.dY(np) == 2) and self.on_track(self.map[4]))))
        return check

    def clone(self):
        new_pattern = Pattern()
        new_pattern.track += self.track
        return new_pattern

    def __len__(self):
        return len(pattern.track)

    def __str__(self):
        return list_print(self.track)


def pattern_track(current_point, length, pattern, pattern_length, pattern_list):
    for next_point in Pattern.map:
        if pattern.valid(current_point, next_point):
            if length == pattern_length:
                pattern = Pattern()
                pattern.track.append(current_point)
            # pattern_copy = copy.deepcopy(pattern)
            pattern_copy = pattern.clone()
            pattern.track.append(next_point)
            if length > 2:
                pattern_track(next_point, length - 1, pattern, pattern_length, pattern_list)
            else:
                pattern_list.append(pattern)
            pattern = pattern_copy


if __name__ == '__main__':
    pattern_min = 4
    pattern_max = 9
    pattern_list = []

    pattern = Pattern()
    for length in range(pattern_min, pattern_max + 1):
        for start_point in Pattern.map:
            pattern_track(start_point, length, pattern, length, pattern_list)

    print(list_print(pattern_list))

    # with open('output.txt', 'w') as file:
    #     file.write(list_print(pattern_list))
    #     file.close()

    print(len(pattern_list))
