clean:
	rm -f *.html
	rm -rf *-*_files/

all: r11 r12 r13 r14 r21 r22 r23 r24

r11:
	quarto render P1B1*.qmd

r12:
	quarto render P1B2*.qmd

r13:
	quarto render P1B3*.qmd

r14:
	quarto render P1B4*.qmd

r21:
	quarto render P2B1*.qmd

r22:
	quarto render P2B2*.qmd

r23:
	quarto render P2B3*.qmd

r24:
	jupyter notebook
	
v11:
	open P1B1*.html

v12:
	open P1B2*.html

v13:
	open P1B3*.html

v14:
	open P1B4*.html

v21:
	open P2B1*.html

v22:
	open P2B2*.html

v23:
	open P2B3*.html


r11v: r11 v11

r12v: r12 v12

r13v: r13 v13

r14v: r14 v14

r21v: r21 v21

r22v: r22 v22

r23v: r23 v23

r24v: r24

