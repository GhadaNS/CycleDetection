import argparse
from collections import defaultdict


parser = argparse.ArgumentParser()
# Creating optional arguments
parser.add_argument("-t", action="store_true", help="Print final table")
# Creating positional arguments
parser.add_argument("b", type=int, help="Parameter b")
parser.add_argument("g", type=int, help="Parameter g")
parser.add_argument("table_size", type=int, help="table size maximum")
parser.add_argument("input_sequence", help="The sequence")
# Getting Arguments
args = parser.parse_args()
t = args.t
b = args.b
g = args.g
max_size = args.table_size
fname = args.input_sequence

with open(fname, 'r') as f:
    seq = f.read().splitlines()
    itr = iter(seq)
    table = defaultdict(list)

    def Purge(tbl, c):
        tbl0 = tbl.copy()
        for key, value in tbl0.items():
            if value[0] % c != 0:
                del tbl[key]

    def InsertInTable(tbl, elm, ind):
        tbl[elm].append(ind)

    def SearchTableY(tbl, elm):
        if elm in tbl:
            return tbl[elm][0]
        else:
            return -1

    def f(iterator):
        return next(iterator)


    def DetectCycle(iterator):
        global b
        y = next(iterator)
        i = m = 0
        while True:
            if i % b == 0 and m == max_size:
                b = 2 * b
                Purge(table, b)
                m = abs(-m // 2)  # to perform ceil division without using the math lib since it's not allowed
            if i % b == 0:
                InsertInTable(table, y, i)
                m += 1
            y = f(iterator)
            i += 1
            if i % abs(b-g) < b:
                j = SearchTableY(table, y)
                if j != -1:
                    return y, i, j

    #  Detect Cycle
    y, i, j = DetectCycle(itr)

    def RecoverCycle(y, i, j):
        global itr
        c = 1
        c_found = False
        yc = y
        while c < (g + 1) * b and c_found is False:
            yc = f(itr)
            if y == yc:
                c_found = True
            else:
                c += 1
        if c_found is False:
            c = i - j
        block_len = g * b
        fin_block = block_len * abs(-i // block_len)
        prv_block = fin_block - block_len
        l = max(c, prv_block) - c + 1
        while seq[l] != seq[l+c]:
            l += 1
        return l, c

    # Recover Cycle
    l, c = RecoverCycle(y, i, j)
    print("Cycle", c, "Leader", l)
    if t:
        keys = list(table.keys())
        values = list(table.values())
        values = [str(val[0]) for val in values]
        print(" ".join(values))
        print(" ".join(keys))
