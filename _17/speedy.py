import sys
import math
from functools import lru_cache

# Returns the timestep (float) for the projectile with x-velocity vx to reach x
@lru_cache(maxsize=None)
def tx(vx, x):
    # The maximum value never reaches x
    if (vx*(vx+1))/2 < x:
        return sys.maxsize
    return ((2*vx+1)-math.sqrt(4*vx**2 + 4*vx-8*x+1))/2

# Returns the timestep (float) for the projectile with y-velocity vy to reach y
@lru_cache(maxsize=None)
def ty(vy, y):
    if vy > 0:
        return ((2*vy+1)+math.sqrt(4*vy**2 + 4*vy-8*y+1))/2
    else:
        return ((2*vy+1)+math.sqrt(4*vy**2 + 4*vy-8*y+1))/2

def solve(vx, vy, bounds):
    
    # The range of timesteps where the projectile is valid in the x or y boundaries
    tx_lo = math.ceil(tx(vx, bounds[0]))
    tx_hi = math.floor(tx(vx, bounds[1]))
    ty_hi = math.ceil(ty(vy, bounds[3]))
    ty_lo = math.floor(ty(vy, bounds[2]))
    
    if ty_lo >= tx_lo and tx_hi >= ty_hi and ty_hi <= ty_lo:
        return 1
    return 0


if __name__ == "__main__":
    ans = 0
    bounds = [81,129,-150,-108]

    for vx in range(bounds[1] + 1):
        for vy in range(bounds[2], 200):
            ans += solve(vx, vy, bounds)
    print(f"Answer: {ans} ")
