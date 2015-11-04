#!/usr/bin/env Rscript

require(ggplot2)
X2 = read.csv("./out2.csv")
p <- ggplot(X2, aes(x=Fs,y=Us))

p + geom_tile(aes(fill=count)) + scale_fill_gradient(trans = "log") # pdf
ggsave(file="ffuu_map.png") # png obviously

# Note: can add...
# scale_fill_gradient(limits=c(100,1000000),...

# Alternate way to get Rplots.pdf:
# print(p + geom_tile(aes(fill=count)) + scale_fill_gradient(trans = "log"))
