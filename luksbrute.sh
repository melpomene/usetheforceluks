#!/bin/bash

DEVICE=$2
while read line; do
    echo "$line" | cryptsetup luksOpen "$DEVICE" encrypted 2>/dev/null
    # success
    if [[ $? -eq 0 ]]; then
        cryptsetup luksClose encrypted
        echo "Passphrase: $line"
        exit 0
    else 
	echo "no"
    fi

done < "$1"

echo "Passphrase not contained in word list. ! "
exit 1
