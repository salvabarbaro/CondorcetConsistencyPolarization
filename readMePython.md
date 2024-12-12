
# SplitCycle General Voting Analysis

This Python script performs an analysis of voting outcomes using various voting methods, including SplitCycle, Copeland, Ranked Choice, Minimax, and Beat Path. It generates results based on combinations of voting support configurations (`gamma_1`, `gamma_2`, `gamma_3`), ensuring only valid configurations are processed.

## Features

- Generates results for different voting methods.
- Handles ties gracefully with clear output for tied candidates.
- Provides a detailed data frame summarizing voting outcomes across all methods.

## Getting Started

### Prerequisites

Ensure you have Python installed along with the following dependencies:

- `pandas`
- `pref_voting`

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repository-name.git

# Navigate to the project directory
cd your-repository-name
```

### Usage

1. Run the script directly:
    ```bash
    python SplitCycleGeneral.py
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

- This script is adapted from [SplitCycle Examples](https://github.com/epacuit/splitcycle/blob/master/02-SplitCycleExamples.ipynb).

## Authors

Salvatore Barbaro
