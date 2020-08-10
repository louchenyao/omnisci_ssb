#! /usr/bin/env python3

import argparse
import glob
import subprocess
import os
import pandas as pd

# https://stackoverflow.com/a/13197763
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def convert(n):
    print(f"Converting table {n}...")
    t = pd.read_table(f"{n}.tbl", sep="|", header=None)
    t = t.drop(columns=[t.columns[-1]])
    t.to_csv(f"{n}.csv", header=False, index=False)

def run(sql, db=""):
    assert(os.system(f"echo \"{sql}\" | /opt/omnisci/bin/omnisql -u admin -p HyperInteractive {db}") == 0)

def run_sqlfile(path, db=""):
    p = subprocess.run(f"/opt/omnisci/bin/omnisql -t -u admin -p HyperInteractive {db} < {path}",
                       stdout=subprocess.PIPE,
                       shell=True)
    assert(p.returncode == 0)
    # eg: Execution time: 18 ms, Total time: 20 ms
    for l in p.stdout.decode().splitlines():
        if l.startswith("Execution"):
            assert("ms," in l)
            l = l.split()
            return int(l[2]), int(l[6])
    return 0, 0

def gen(sf=1):
    os.system(f"rm -rf data_sf{sf}")
    os.system(f"mkdir -p data_sf{sf}")
    with cd(f"data_sf{sf}"):
        os.system("cp ../dists.dss .")
        assert(os.system(f"../dbgen -s {sf}") == 0)
        for t in ["customer", "date", "lineorder", "part", "supplier"]:
            convert(t)
        os.system("rm -rf *.tbl dists.dss")

def import_(sf=1):
    # create db
    run(f"DROP DATABASE IF EXISTS ssb_sf{sf};")
    run(f"CREATE DATABASE ssb_sf{sf};")

    # create table
    run_sqlfile("./tables.sql", f"ssb_sf{sf}")

    # import
    for t in ["customer", "date", "lineorder", "part", "supplier"]:
        print(f"Importing table {t}")
        f = os.getcwd() + f"/data_sf{sf}/{t}.csv"
        to = t
        if to == "date":
            to = "date_"
        run(f"copy {to} from '{f}' with (quoted='true');", f"ssb_sf{sf}")

def bench(sf=1):
    queries = glob.glob("./queries/*.sql")
    queries.sort()
    for q in queries:
        min_ = 1000000000
        for _ in range(3):
            time, _ = run_sqlfile(q, f"ssb_sf{sf}")
            if time < min_:
                min_ = time
        print(f"{q} takes {min_} ms")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', type=str, choices=['gen', 'import', 'bench'])
    parser.add_argument('sf', type=int)
    args = parser.parse_args()

    if args.cmd == 'gen':
        gen(args.sf)
    elif args.cmd == 'import':
        import_(args.sf)
    elif args.cmd == 'bench':
        bench(args.sf)