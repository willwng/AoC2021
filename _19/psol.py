import sys
import numpy as np
from random import choice

def to_int(arr):
    return [int(a) for a in arr]

def intersection(a1, a2):
    return [list(x) for x in set(tuple(x) for x in a1).intersection(set(tuple(x) for x in a2))]

def unique(a):
    return set(tuple(x) for x in a)


def overlap_beacons(scanners, i, j, rot_matrices):
    beacons_i = scanners[i]  # should be solved?
    beacons_j = scanners[j]
    # find transformation
    for r in rot_matrices: 
        # apply the rotation to all beacons
        rotated_beacons = [r.dot(b) for b in beacons_j]
        # pick a specific beacon and test a translation
        for b_j in rotated_beacons:
            for b_i in beacons_i:
                translate = b_i - b_j
                trans_beacons = [b + translate for b in rotated_beacons]
                if len(intersection(trans_beacons, beacons_i)) >= 12: # ladies and gentlemen, we found a match!
                    scanners[j] = trans_beacons
                    return trans_beacons, translate
    return None, []


def solve(file_name):
    # Get each of the scanner's beacons
    scanners = {}
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            if "scanner" in l:
                n_scan = int(l.split("scanner ")[1].split(" ---")[0])
                scanners[n_scan] = []
            elif not l:
                continue
            else:
                beacon = np.array(to_int(l.split(",")))
                scanners[n_scan].append(beacon)
    
    # do stuff
    # Find an axis of orientation first
    faces = [tuple(o) for dir in [1, -1] for o in [[dir, 0,0], [0,dir,0],[0,0,dir]]]
    # rotation for each axis
    rotations = {}
    for o in faces:
        rot = [o1 for o1 in faces if (np.abs(o1) != np.abs(o)).any()]
        rotations[o] = rot
    # finally, find all 24 orientation matrices
    rot_matrices = []
    for o in faces:
        for r in rotations[o]:
            # find third vector
            t = np.cross(o, r)
            mat = [o, r, t]
            mat = np.array([np.array(m) for m in mat])
            rot_matrices.append(mat)
    
    # brute force hard
    n_scanners = len(scanners.keys())
    solved = [False] * n_scanners
    solved[0] = True
    all_beacons = [b for b in scanners[0]]
    positions = {0: [0,0,0]}
    # To not lose patience
    patience = ["Patience, young one.", "Time is the money.", "Slow and steady wins the race",
     "One minute of patience, ten years of peace.", "To lose patience is to lose the battle",
     "Come what may, all bad fortune is to be conquered by endurance"]
    
    while not all(solved):
        print(choice(patience)) #:)
        # pick a solved scanner
        for i in range(n_scanners):
            if solved[i]:
                for j in range(n_scanners):
                    # ignore solved scanners
                    if solved[j]:
                        continue
                    new_beacons, trans = overlap_beacons(scanners, i, j, rot_matrices)
                    # match!
                    if new_beacons is not None:
                        solved[j] = True
                        all_beacons.extend(new_beacons)
                        positions[j] = trans
    # answer 1
    unique_beacons = unique(all_beacons)
    ans1 = len(unique_beacons)
    # answer 2
    ans2 = -1
    print(positions)
    for i in range(n_scanners):
        for j in range(n_scanners):
            p1 = positions[i]
            p2 = positions[j]
            dis= abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])
            if dis > ans2:
                ans2 = dis
    return ans1, ans2


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans1, ans2 = solve(file_name)
    print(f"Answer 1: {ans1} ")
    print(f"Answer 2: {ans2} ")
