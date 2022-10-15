DOCNAME=master
PDF_VIEWER=zathura

.PHONY:
	clean

all:
	make compile
	make clean

compile:
	pdflatex -synctex=1 $(DOCNAME).tex
	pdflatex -synctex=1 $(DOCNAME).tex
	pdflatex -synctex=1 $(DOCNAME).tex

clean:
	rm -rf *.aux *.bcf *.fdb_latexmk *.fls *.log *.out *.toc *.synctex.gz

view:
	make compile
	make clean
	$(PDF_VIEWER) $(DOCNAME).pdf
