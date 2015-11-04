#!/usr/bin/env Rscript

require(ggplot2)
X2 = read.csv("./out2.csv")
p <- ggplot(X2, aes(x=Fs,y=Us))

# To get Rplots.pdf, which is smaller than a PNG:
print(p + geom_tile(aes(fill=count)) + scale_fill_gradient(trans = "log"))

# To get PNG:
# p + geom_tile(aes(fill=count)) + scale_fill_gradient(trans = "log")
# ggsave(file="map.png")

# Note: can also do...
# scale_fill_gradient(limits=c(100,1000000),...
