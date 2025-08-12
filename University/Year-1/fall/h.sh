# iterate over all the folders
TEMPLATES="/home/singularisart/Documents/school-notes/University/template-files"

for dir in */; do
  echo "rm -rf $PWD/$dir/preamble.tex"
  echo "rm -rf $PWD/$dir/Makefile"
  echo "rm -rf $PWD/$dir/assignments/my-assignments/preamble.tex"
  echo "rm -rf $PWD/$dir/assignments/my-assignments/Makefile"

  echo "ln -sf $TEMPLATES/preamble.tex $PWD/$dir/preamble.tex"
  echo "ln -sf $TEMPLATES/Makefile $PWD/$dir/Makefile"

  echo "ln -sf $TEMPLATES/assignments/my-assignments/preamble.tex $PWD/$dir/assignments/my-assignments/preamble.tex"
  echo "ln -sf $TEMPLATES/assignments/my-assignments/Makefile $PWD/$dir/assignments/my-assignments/Makefile"
done
