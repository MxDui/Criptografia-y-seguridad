#!/bin/sh
set -eu

if ! command -v steghide >/dev/null 2>&1; then
    echo "Falta steghide. Instala con: sudo apt-get install steghide jp2a" >&2
    exit 1
fi

rm -f silent.sh secrets.sh index.html
IMAGE="mao-shi.jpg"
if [ ! -f "$IMAGE" ] && [ -f "../$IMAGE" ]; then
    IMAGE="../$IMAGE"
fi
steghide extract -sf "$IMAGE" -p eje4 -f
ls -l silent.sh
grep -n 'FLAG' silent.sh
