PY_SOURCE=$(wildcard *.py)
TX_SOURCE=$(PY_SOURCE:.py=.tex)

all : $(TX_SOURCE)

%.tex : %.py pygments.tex
	@pygmentize -f latex -P linenos=True -P verboptions="xleftmargin=.5em,numbersep=1em" -o $*.tex $*.py

pygments.tex:
	@pygmentize -S friendly -f latex  > pygments.tex

show:
	@echo $(PY_SOURCE)

clean:
	@rm -fv $(TX_SOURCE)
