# tcxtools
Collection of utilities for processing TCX files

## tcxsplit.py
usage: tcxsplit.py [-h] tcx_files [tcx_files ...]

Split a Garmin TCX file containing multiple laps into multiple TCX file, each containing 1 lap.

positional arguments:
  tcx_files   TCX files to split

optional arguments:
  -h, --help  show this help message and exit

Example output:
```
./tcxsplit.py sample.tcx
2 laps found in sample.tcx
Creating sample_1.tcx
Creating sample_2.tcx
```
