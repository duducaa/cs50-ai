#!/bin/bash

algs=("dfs", "bfs", "gbfs", "a*")

for alg in "${algs[@]}"
do
    for maze_idx in {1..4}
    do
        python3 "./main.py" $alg $maze_idx
    done
done