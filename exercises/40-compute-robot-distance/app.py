import math
def compute_robot_distance(directions):
    directions_list = directions.split(' ')
    pos = [0,0]
    for x in range(0, len(directions_list), 2):
        if directions_list[x] == 'UP':
            pos[0] += int(directions_list[x+1])
        elif directions_list[x] == 'DOWN':
            pos[0] -= int(directions_list[x+1])
        elif directions_list[x] == 'LEFT':
            pos[1] -= int(directions_list[x+1])
        elif directions_list[x] == 'RIGHT':
            pos[1] += int(directions_list[x+1])

    # use pythagorean theorem to calculate the distance
    return int(round(math.sqrt(pos[0]**2+pos[1]**2)))

print(compute_robot_distance("DOWN 2 UP 10 LEFT 1 RIGHT 8"))