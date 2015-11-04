all : out2.csv
	./plot.R

out2.csv :
	python fake.py > out.csv

github :
	cp ffuu_map.png ~/Dropbox/Public/github_img 

clean :
	rm -f *.csv *.pdf *.png
