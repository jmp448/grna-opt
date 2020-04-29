library(corrplot)

corrs <- data.frame("Experimental" = c(NA, 0.312, 0.907, 0.345), "Azimuth" = c(0.324, NA, 0.312, 0.523), "DeepCRISPR" = c(0.905, 0.330, NA, 0.350), "DeepHF"=c(0.375, 0.550, 0.383, NA), row.names = c("Experimental", "Azimuth", "DeepCRISPR", "DeepHF"))
corrplot(as.matrix(corrs), method="color", addCoef.col = "black", na.label='-', tl.col="black")
