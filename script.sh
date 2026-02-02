#!/usr/bin/bash

# iterate over
for folder in $PWD/*; do
  # Check if the thing is a file
  if [ ! -d "$folder" ]; then
    continue
  fi

  cd "$folder"

  rm -rf "$PWD/Makefile"
  rm -rf "$PWD/preamble.tex"
  rm -rf "$PWD/UltiSnips"
  rm -rf "$PWD/assignments/my-assignments/Makefile"
  rm -rf "$PWD/assignments/my-assignments/preamble.tex"

  ln -sf "$HOME/Documents/school-notes/College/_files/Makefile" "$PWD/Makefile"
  ln -sf "$HOME/Documents/school-notes/College/_files/preamble.tex" "$PWD/preamble.tex"
  ln -sf "$HOME/Documents/school-notes/College/_files/UltiSnips" "$PWD/UltiSnips"
  ln -sf "$HOME/Documents/school-notes/College/_files/assignments/my-assignments/Makefile" "$PWD/assignments/my-assignments/Makefile"
  ln -sf "$HOME/Documents/school-notes/College/_files/assignments/my-assignments/preamble.tex" "$PWD/assignments/my-assignments/preamble.tex"
done
