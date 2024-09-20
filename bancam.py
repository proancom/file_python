with open('bancam.INP', 'r') as f:
    a = [float(line.strip()) for line in f.readlines()]
    d = 0
    if a[0] <= 5:
        d = a[0] * a[1]
    elif a[0] > 5:
        d = a[0] * a[1] - (a[0] * a[1])*25/100
with open('bancam.OUT', 'w') as w:
    w.write(f'{d:.2f}')
