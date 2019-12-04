#!/usr/bin/env bash

cd "${0%/*}"

echo "$(date) Starting virtualenv..."

source ./venv/bin/activate

echo "$(date) Starting Api..."

python ./main.py