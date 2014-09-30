import math
import sys
# I need some way to define this solid..

schism_radius = 0.5
lower_radius = 19
upper_radius = 6.3
height = 64.0
theta = math.pi * 2.0

def inside(x, y, z):
    # First, determine which side of the line the point is on, so we know which hemicircle to
    # check against.
    d_theta = (theta / height) * z
    if d_theta >= math.pi * 2:
        d_theta -= math.pi * 2
    neg_d_theta = d_theta + math.pi
    if neg_d_theta >= math.pi*2:
        neg_d_theta -= math.pi*2
    alpha = math.atan2(y, x+0.5)
    if alpha < 0:
        alpha = math.pi * 2 + alpha
    d_radius = lower_radius - ((lower_radius - upper_radius) / height) * z

    if d_theta < math.pi:
        if alpha >= d_theta and alpha < neg_d_theta:
            c_x = schism_radius * math.cos(d_theta)+0.5
            c_y = schism_radius * math.sin(d_theta)
        else:
            c_x = schism_radius * math.cos(neg_d_theta)+0.5
            c_y = schism_radius * math.sin(neg_d_theta)
    else:
        if alpha >= d_theta or alpha < neg_d_theta:
            c_x = schism_radius * math.cos(d_theta)+0.5
            c_y = schism_radius * math.sin(d_theta)
        else:
            c_x = schism_radius * math.cos(neg_d_theta)+0.5
            c_y = schism_radius * math.sin(neg_d_theta)

    d_y = y - c_y
    d_x = x - c_x
    dist2 = d_y * d_y + d_x * d_x
    if dist2 < d_radius * d_radius:
        return True
    else:
        return False

slice = float(sys.argv[1])

samples = 7

for y in range(21, -21, -1):
    y_five = y % 5 == 0
    line = ''
    for x in range(-21, 21, 1):
        x_five = x % 5 == 0
        in_count = 0
        for dx in range(samples):
            for dy in range(samples):
                for dz in range(samples):
                    x_val = x+float(dx)/samples + 1.0/samples/2
                    y_val = y+float(dy)/samples + 1.0/samples/2
                    z_val = slice+float(dz)/samples + 1.0/samples/2
                    if inside(x_val, y_val, z_val):
                        in_count += 1
        if in_count > samples*samples*samples / 2:
            if x_five and y_five:
                line += 'B'
            elif x_five:
                line += 'Q'
            elif y_five:
                line += 'G'
            else:
                line += 'O'
        else:
            if x_five and y_five:
                line += '+'
            elif x_five:
                line += '|'
            elif y_five:
                line += '-'
            else:
                line += '.'
    print(line)

