#!/bin/bash

## Cleanup vstoarage and internal-storage

[ -f vstorage ] && echo "" > vstorage
[ -f internal-storage/log.txt ] && echo "" > internal-storage/log.txt