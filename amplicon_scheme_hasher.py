#!/usr/bin/env python

import argparse
import hashlib
import itertools
import sys

def hash_bed(bed_fp):
    """
    Parse and hash a bed file in a manner robust to differences in amplicon
    names/order
    """
    bed_primers = []
    with open(bed_fp) as bed_fh:
        for line in bed_fh:
            line = line.strip().split()
            bed_primers.append((line[0], line[1], line[2], line[5]))
    bed_primers.sort(key=lambda x: x[1])
    bed_primers = "\n".join(list(itertools.chain.from_iterable(bed_primers)))
    bed_hash = hashlib.sha256(bed_primers.encode('utf-8')).hexdigest()
    return bed_hash


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Hash and compare amplicon "
                                                 "scheme bed files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--bed",
                        help="Get a hash for an amplicon scheme "
                             "(based on primer sequences)")
    group.add_argument("-c", "--compare",
                       help="Hash and compare 2 or more primer beds", nargs="+")

    args = parser.parse_args()

    if args.bed:
        print(f"{args.bed} hash: {hash_bed(args.bed)}")
    elif args.compare:
        hashes = []
        for bed in args.compare:
            bed_hash = hash_bed(bed)
            print(f"{bed} hash: {bed_hash}")
            hashes.append((bed, bed_hash))
        if len(args.compare) == 1:
            print("Require >1 bed files to do comparison", file=sys.stderr)
            sys.exit(1)

        print()
        for bed1, bed2 in itertools.combinations(hashes, 2):
            if bed1[1] == bed2[1]:
                print(f"\033[94m{bed1[0]} and {bed2[0]} MATCH\033[4m")
            else:
                print(f"\033[91m{bed1[0]} and {bed2[0]} DO NOT MATCH\033[4m")
