#!/bin/bash

## Cleanup vstoarage and internal-storage

[ -f vstorage ] && false > vstorage
[ -f internal-storage/log.txt ] && false > internal-storage/log.txt