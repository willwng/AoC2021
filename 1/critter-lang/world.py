with open('input.txt', 'r') as f, open('world.wld', 'w') as w:
    w.write("name day1\n")
    w.write("size 2 200\n")
    w.write("critter sol.ctr 0 0 1\n")

    row = 1
    for line in f:
        w.write(f"food 1 {row} {line}")
        row += 2
