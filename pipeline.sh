#!/bin/bash

CUNI-x-ling/metadata2commands.py $1 $2 > run.sh
bash run.sh
