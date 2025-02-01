#!/bin/sh

BASEDIR=$(pwd)
echo $"running : auditor.sh"
echo $"BASEDIR: $BASEDIR"

index=1
for item in *; do
  echo "item $index: $item"
  ((index++))
done

DELAY=3
sleep $DELAY