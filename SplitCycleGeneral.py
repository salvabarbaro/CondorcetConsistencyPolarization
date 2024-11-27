## Most of the script is an adoption from 
## https://github.com/epacuit/splitcycle/blob/master/02-SplitCycleExamples.ipynb
import pandas as pd
from pref_voting.profiles import Profile
from pref_voting.voting_methods import split_cycle

a, b, c = 0, 1, 2  # Candidates
cmap_abc = {a: "a", b: "b", c: "c"} 
cmap = cmap_abc

# Generate all valid combinations: gamma_1, gamma_2 \in (gamma_3, 0.5]

results = []
for gamma1 in range(51):  # gamma_1 (supporters)
    for gamma2 in range(51):  # gamma_2 (despisers)
        gamma3 = 101 - gamma1 - gamma2  # gamma_3: (moderates)
        if gamma3 >= 0 and gamma3 <= 50 and gamma3 <= min(gamma1, gamma2):  # Valid configurations
            #  Profile 5
            prof = Profile([(a, b, c), (b, c, a), (c, a, b)],
                           rcounts=[gamma1, gamma2, gamma3],
                           cmap=cmap)
            
            # Calculate the split cycle winner
            winner = split_cycle(prof)
            
            # Append results
            results.append({
                "Gamma1": gamma1,
                "Gamma2": gamma2,
                "Gamma3": gamma3,
                "Winner": winner
            })

# All results in a data frame
df_results = pd.DataFrame(results)
### Winner: 0 --> A, 1 --> B, c(0,1) --> Tie between A and B.

#print(df_results.head())  # Display first few rows
#df_results.to_csv("split_cycle_results.csv", index=False)
