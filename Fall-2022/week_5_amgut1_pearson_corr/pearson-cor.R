# Assessing the Pearson Correlation on the American Gut Data

# Load the libraries
library(dplyr)
library(ggpubr)

amgut1_data <- data.frame(amgut1.filt)
# For loop that iterates through all the possible combination of the taxas (columns) in the dataset
# Calculate the Pearson Correlation of each taxa pair
# Initialize the cor_dataframe variable with column names : taxa1, taxa2, cor
cor_df <-
  data.frame(taxa1 = character(),
             taxa2 = character(),
             cor = numeric())
for (i in 1:ncol(amgut1_data)) {
  for (j in 1:ncol(amgut1_data)) {
    if (i != j) {
      calc_cor <-
        cor(amgut1_data[, i], amgut1_data[, j], method = "pearson")
      abs_calc_cor <- abs(calc_cor)
      if (abs_calc_cor >= 0.9) {
        print(abs_calc_cor)
        # Append the taxa1, taxa2, cor to the cor_df
        cor_df <-
          rbind(
            cor_df,
            data.frame(
              taxa1 = colnames(amgut1_data)[i],
              taxa2 = colnames(amgut1_data)[j],
              cor = abs_calc_cor
            )
          )
      }
    }
  }
}

# Remove the duplicate taxa1 and taxa2 pairs
cor_df <- cor_df %>%
          rowwise() %>%
          mutate(key = paste(sort(c(taxa1, taxa2)), collapse="")) %>%
          distinct(key, .keep_all=T) %>%
          select(-key)
# Sort the cor_df by the absolute value of the correlation
cor_df <- cor_df[order(cor_df$cor, decreasing = TRUE), ]

for (i in 1:nrow(cor_df)) {
# Plot the taxa1 and taxa2
  taxa1 <- cor_df$taxa1[i]
  taxa2 <- cor_df$taxa2[i]
# taxa1_data <- amgut1_data[, taxa1]
# taxa2_data <- amgut1_data[, taxa2]
# taxa_combined <- data.frame(taxa1_data,taxa2_data)
  plot <- ggscatter(amgut1_data, x = taxa1, y = taxa2, add = "reg.line",
                    xlab = paste( "Taxa", taxa1),
                    ylab = paste( "Taxa", taxa2),
                    add.params = list(color = "blue", fill = "lightgray"),
                    conf.int = TRUE, cor.coef = TRUE, cor.method = "pearson")
}
print(plot)
