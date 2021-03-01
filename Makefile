
all: slides.pdf

%.pdf : %.tex
	xelatex -synctex=1 -interaction=nonstopmode $<

clean :
	@rm -fv *vrb *snm *aux *toc *out *nav *synctex.gz *.log
