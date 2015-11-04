all : out2.csv
	./plot.R

out2.csv :
	python fake.py > out2.csv

clean :
	rm -f *.csv *.pdf *.png
