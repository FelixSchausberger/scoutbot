#!/bin/bash
set -e

./src/scripts/setup.sh
./src/scripts/build.sh
./src/scripts/test.sh
