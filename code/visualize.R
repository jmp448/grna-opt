library(corrplot)

# corrs <- data.frame("Experimental" = c(NA, 0.368, 0.2, 0.771), "Azimuth" = c(0.388, NA, 0.174, 0.443), "DeepCRISPR" = c(0.182, 0.179, NA, 0.237), "DeepHF"=c(0.829, 0.457, 0.215, NA), row.names = c("Experimental", "Azimuth", "DeepCRISPR", "DeepHF"))
# corrplot(as.matrix(corrs), method="color", addCoef.col = "black", na.label='-', tl.col="black")

training <- "indel"
dtype <- "azimuth"

preds.loc = "../results/indel_data/retrained.txt"

preds <- read.delim(preds.loc, header=TRUE, row.names=1)

corrs <- cor(preds, method="spearman")

png(paste0("../figs/", dtype, ".", training, ".corrs.png"))
corrplot(corrs, tl.col = "black")
dev.off()
