all : out.csv
	./plot.R

out.csv :
	./main.py > out.csv

github :
	cp ffuu_map.png ~/Dropbox/Public/github_img 

clean :
	rm -f *.pdf *.png
