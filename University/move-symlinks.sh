# iterate over all the folders
TEMPLATES="/home/singularisart/Documents/school-notes/University/template-files"

for dir in */; do
  rm -rf $PWD/$dir/preamble.tex
  rm -rf $PWD/$dir/Makefile
  rm -rf $PWD/$dir/assignments/my-assignments/preamble.tex
  rm -rf $PWD/$dir/assignments/my-assignments/Makefile

  ln -sf $TEMPLATES/preamble.tex $PWD/$dir/preamble.tex
  ln -sf $TEMPLATES/Makefile $PWD/$dir/Makefile

  ln -sf $TEMPLATES/assignments/my-assignments/preamble.tex $PWD/$dir/assignments/my-assignments/preamble.tex
  ln -sf $TEMPLATES/assignments/my-assignments/Makefile $PWD/$dir/assignments/my-assignments/Makefile
done
