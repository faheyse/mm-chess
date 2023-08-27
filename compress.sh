#!/bin/bash

# Search and compress all jpg, png, and gif files in current and sub-directories
find . -type f \( -iname \*.jpg -o -iname \*.jpeg \) -exec bash -c 'echo "Compressing {}"; jpegoptim --max=90 {}' \;
find . -type f \( -iname \*.png \) -exec bash -c 'echo "Compressing {}"; optipng -o2 {}' \;
find . -type f \( -iname \*.gif \) -exec bash -c 'echo "Compressing {}"; gifsicle -O2 -o {} {}' \;
