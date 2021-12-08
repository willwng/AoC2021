import sys
from functools import lru_cache


def intersect(a1, a2):
    return [v for v in a1 if v in a2]


def find_odd(a1, a2):
    return [v for v in a1 if v not in a2]


def find_corr(dic, k):
    for key in dic:
        found = True
        if len(k) != len(dic[key]):
            continue
        for c in k:
            if c not in list(dic[key]):
                found = False
        if found:
            return key


def solve():
    ans = 0

    uniq = {}
    uniq[2] = 1
    uniq[3] = 7
    uniq[4] = 4
    uniq[7] = 8
    with open('input.txt') as f:
        for line in f:
            a = line.strip().split(' | ')
            a1 = a[0].split(' ')
            a2 = a[1].split(' ')
            on = {}
            known = {}
            dic = {}
            for seq in a1:
                siz = len(seq)
                if siz not in uniq:
                    continue
                corresp = uniq[siz]
                known[corresp] = []

                for c in seq:
                    known[corresp].append(c)
                    on[c] = True

            seq1 = known[1]
            seq4 = known[4]
            seq7 = known[7]
            seq8 = known[8]
            seq17 = intersect(seq1, seq7)

            c_or_f = seq17
            a_pos = find_odd(seq7, seq17)[0]
            b_or_d = find_odd(seq4, seq1)
            dic[a_pos] = 'a'

            for seq in a1:
                siz = len(seq)
                seq_l = list(seq)
                # know its a 0 or 9
                if siz == 6 and c_or_f[0] in seq_l and c_or_f[1] in seq_l:
                    corresp = 0
                    b_ds = 0
                    for c in seq:
                        # matdh d
                        if c in seq4 and not c in seq1:
                            b_ds += 1

                    if b_ds == 2:
                        corresp = 9
                elif siz == 6:
                    corresp = 6
                elif siz == 5:
                    c_fs = 0
                    for c in seq:
                        # c f
                        if c in seq1:
                            c_fs += 1
                    if c_fs == 2:
                        corresp = 3
                    else:
                        eee = intersect(list(seq), seq4)
                        if len(eee) == 2:
                            corresp = 2
                        else:
                            corresp = 5
                else:
                    continue
                known[corresp] = []
                for c in seq:
                    known[corresp].append(c)
                    on[c] = True

            mapdic = {}
            for key in known:
                known[key] = "".join(known[key])
                mapdic[known[key]] = key

            # for key in list(sorted(known)):
            #     print(f"{key}: {known[key]}")
            st1 = ""
            for seq in a2:
                st1 += str(find_corr(known, seq))
                # print("HI", seq, str(find_corr(known, seq)))

            ans += int(st1)
    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
