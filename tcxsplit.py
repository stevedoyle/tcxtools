#!/usr/bin/env python

# Split a Garmin TCX file containing multiple laps into multiple TCX
# files, each containing 1 lap.

import copy
import os
import argparse
from lxml import objectify

namespace = 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'


def remove_laps():
    pass


def count_laps(tree_root):
    return int(tree_root.xpath('count(//ns:Lap)', namespaces={'ns': namespace}))


def generate_filename_for_lap(base_filename, lap_num):
    parts = os.path.splitext(base_filename)
    return parts[0] + '_' + str(lap_num + 1) + parts[1]


def remove_laps_except(tree, lap_num):
    laps = tree.getroot().xpath('//ns:Lap', namespaces={'ns': namespace})
    del laps[lap_num]
    for lap in laps:
        lap.getparent().remove(lap)


def tcxsplit(filename):
    tree = objectify.parse(filename)
    root = tree.getroot()
    num_laps = count_laps(root)
    print('%d laps found in %s' % (num_laps, filename))

    for lap_idx in range(num_laps):
        lap_tree = copy.deepcopy(tree)
        remove_laps_except(lap_tree, lap_idx)
        lap_filename = generate_filename_for_lap(filename, lap_idx)
        print('Creating ' + lap_filename)
        lap_tree.write(lap_filename, pretty_print=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Split a Garmin TCX file "
                                     "containing multiple laps into multiple TCX file, each containing 1 lap.")

    parser.add_argument('tcx_files', nargs='+', help="TCX files to split")

    args = parser.parse_args()

    for tcx_file in args.tcx_files:
        tcxsplit(tcx_file)
