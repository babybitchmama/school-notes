DOCNAME=master
PDF_VIEWER=zathura

.PHONY:
	clean

all:
	make compile
	make clean

doall:
	make clean compile clean view

compile:
	pdflatex -synctex=1 $(DOCNAME).tex
	pdflatex -synctex=1 $(DOCNAME).tex
	bibtex master
	pdflatex -synctex=1 $(DOCNAME).tex
	pdflatex -synctex=1 $(DOCNAME).tex

clean:
	rm -rf master.bcf master.fdb_latexmk master.fls master.log master.out master.toc master.synctexmaster master.tdo master.loe master.snm master.nav master.bib master.bbl master.blg master.xml master.mtc master.ptc master.mtc0 master.maf master.nlo master.ist master.nls master.lof master.lot master.ilg master.aux

view:
	make compile
	make clean
	$(PDF_VIEWER) $(DOCNAME).pdf
