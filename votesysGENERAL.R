library(votesys)
library(dplyr)

# Generate all admissible configurations of gamma1, gamma2, gamma3
step <- 1
total <- 101
max_value <- 50  # Maximum value for gamma1 and gamma2

configs <- expand.grid(
  gamma1 = seq(0, max_value, by = step),
  gamma2 = seq(0, max_value, by = step)
)

configs <- configs[configs$gamma1 + configs$gamma2 <= total, ]
configs$gamma3 <- total - configs$gamma1 - configs$gamma2

# Filter configurations where gamma3 is the smallest group
configs <- configs[configs$gamma3 < configs$gamma1 & configs$gamma3 < configs$gamma2, ]

# Initialize a results data frame
results <- data.frame(
  gamma1 = numeric(0),
  gamma2 = numeric(0),
  gamma3 = numeric(0),
  smr = character(0),
  dodgson1 = character(0),
  dodgson2 = character(0),
  copeland = character(0),
  kemmeny = character(0),
  schulze = character(0),
  rankedpairs = character(0),
  borda = character(0)
)

# Helper function to safely extract the winner
safe_winner <- function(method_result) {
  if (is.null(method_result) || length(method_result) == 0) {
    return(NA)
  }
  return(method_result[1])  # Take the first winner if multiple exist
}

# Evaluate voting methods for each configuration
for (i in 1:nrow(configs)) {
  gamma1 <- configs$gamma1[i]
  gamma2 <- configs$gamma2[i]
  gamma3 <- configs$gamma3[i]
  
  # Create the raw preference matrix
  raw <- c(
    rep(c('A', 'B', 'C'), gamma1), 
    rep(c('B', 'C', 'A'), gamma2), 
    rep(c('C', 'A', 'B'), gamma3)
  )
  raw <- matrix(raw, ncol = 3, byrow = TRUE)
  
  # Create vote object
  vote <- create_vote(raw, xtype = 2, candidate = c('A', 'B', 'C'))
  
  # Run all methods and safely extract winners
  smr <- safe_winner(cdc_simple(vote)$winner)
  dodgson1 <- safe_winner(cdc_dodgson(vote, dq_t = "dq")$winner)
  dodgson2 <- safe_winner(cdc_dodgson(vote, dq_t = "t")$winner)
  copeland <- safe_winner(cdc_copeland(vote, lose = 0)$winner)
  kemmeny <- safe_winner(cdc_kemenyyoung(vote)$winner)
  schulze <- safe_winner(cdc_schulze(vote)$winner)
  rankedpairs <- safe_winner(cdc_rankedpairs(vote)$winner)
  borda <- safe_winner(borda_method(vote)$winner)
  
  # Add results to data frame
  results <- rbind(
    results, 
    data.frame(
      gamma1 = gamma1, gamma2 = gamma2, gamma3 = gamma3,
      smr = smr, dodgson1 = dodgson1, dodgson2 = dodgson2,
      copeland = copeland, kemmeny = kemmeny,
      schulze = schulze, rankedpairs = rankedpairs,
      borda = borda
    )
  )
}

# View or save results
View(results)

bordaA <- results %>% filter(., borda == "A")
bordaB <- results %>% filter(., borda == "B")
bordaB2 <- results %>% filter(., borda == "B" & gamma1 > gamma2)
