#!/bin/bash
set -e

./src/scripts/setup.sh
ament_${LINTER} src/
