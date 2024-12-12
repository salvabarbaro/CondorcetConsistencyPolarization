# votesys General Voting Analysis

This R script performs an analysis of voting outcomes using various voting methods, including Borda, Copeland, Dodgson, Schulze, Ranked Pairs, and Kemeny. It generates results based on combinations of voting support configurations (`gamma_1`, `gamma_2`, `gamma_3`), ensuring only valid configurations are processed.

## Features

- Supports multiple voting methods, including advanced algorithms.
- Handles ties and missing results gracefully.
- Generates a detailed data frame summarizing voting outcomes across all methods.

## Getting Started

### Prerequisites

Ensure you have R installed along with the following packages:

- `votesys`
- `dplyr`

Install them using:
```R
install.packages("votesys")
install.packages("dplyr")
 ```
### Usage

1. Run the script directly:
    ```bash
    R votesysGENERAL.R
    ```
2. Review the output in the console or modify the script to save results to a file for further analysis.

## Tested Platforms

- Debian OS
- Ubuntu OS

## Known Issues

- None

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing


## Acknowledgments

- This script uses the R package votesys by Jiang Wu.

## Authors

Salvatore Barbaro
