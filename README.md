# omnisci_ssb
Run SSB over Omnisci

## Usage

```
usage: bench.py [-h] {gen,import,bench} sf

positional arguments:
  {gen,import,bench}
  sf
```

Run `./bench.py gen 1` to generate SSB data.

Run `./bench.py import 1` to import tables.

Run `./bench.py bench 1` to run queries.

## Results

### NVIDIA Tesla V100 SXM2 16 GB

**SF = 20**

```
./queries/q11.sql takes 19 ms
./queries/q12.sql takes 19 ms
./queries/q13.sql takes 18 ms
./queries/q21.sql takes 27 ms
./queries/q22.sql takes 26 ms
./queries/q23.sql takes 23 ms
./queries/q31.sql takes 34 ms
./queries/q32.sql takes 53 ms
./queries/q33.sql takes 52 ms
./queries/q34.sql takes 53 ms
./queries/q41.sql takes 43 ms
./queries/q42.sql takes 43 ms
./queries/q43.sql takes 45 ms
```

Note: The above results are the best results across multiple runs.
