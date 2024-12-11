## Most of the script is an adoption from 
## https://github.com/epacuit/splitcycle/blob/master/02-SplitCycleExamples.ipynb
import pandas as pd
from pref_voting.profiles import Profile
from pref_voting.voting_methods import split_cycle, copeland, ranked_choice, minimax, beat_path

# Initialize candidates
a, b, c = 0, 1, 2  # Candidates
cmap_abc = {a: "A", b: "B", c: "C"}  # Map numeric to "A", "B", "C"
cmap = cmap_abc

# Helper function to map winners, including ties
def map_winner(winner):
    if isinstance(winner, list):  # Handle ties
        tied_candidates = [cmap_abc.get(w, str(w)) for w in winner]
        return "Tie: " + ", ".join(tied_candidates)
    return cmap_abc.get(winner, "Unknown")

# Generate all valid combinations: gamma_1, gamma_2, gamma_3 with gamma_1, gamma_2 \in (gamma_3, .5) and \sum gamma_i = 1
results = []
for gamma1 in range(51):  # gamma_1 (supporters)
    for gamma2 in range(51):  # gamma_2 (despisers)
        gamma3 = 101 - gamma1 - gamma2  # gamma_3: (moderates)
        if gamma3 >= 0 and gamma3 <= 50 and gamma3 <= min(gamma1, gamma2):  # Valid configurations
            # Create the profile
            prof = Profile([(a, b, c), (b, c, a), (c, a, b)],
                           rcounts=[gamma1, gamma2, gamma3],
                           cmap=cmap)
            
            # Calculate winners for various voting methods
            split_cycle_winner = split_cycle(prof)
            copeland_winner = copeland(prof)
            ranked_choice_winner = ranked_choice(prof)
            minimax_winner = minimax(prof)
            beat_path_winner = beat_path(prof)
            
            # Append results
            results.append({
                "Gamma1": gamma1,
                "Gamma2": gamma2,
                "Gamma3": gamma3,
                "SplitCycle": map_winner(split_cycle_winner),
                "Copeland": map_winner(copeland_winner),
                "RankedChoice": map_winner(ranked_choice_winner),
                "Minimax": map_winner(minimax_winner),
                "BeatPath": map_winner(beat_path_winner)
            })

# All results in a data frame
df_results = pd.DataFrame(results)

# Save or display results
print(df_results.head())  # Display first few rows
