
# Drug Interaction Checker
[![GPL License](https://img.shields.io/badge/license-MIT-violet.svg)](https://opensource.org/license/mit) [![Image_Categorizer](https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square)](https://github.com/agnivadas/Ranklist_Evaluator) ![Maintenance](https://img.shields.io/maintenance/yes/2024) ![Static Badge](https://img.shields.io/badge/contributions-welcome-blue)

Drug Interaction Finder is a Python-based tool for identifying drug interactions using PubChem's public APIs. This script fetches drug interaction data for specified drugs, saves the data in CSV format, and identifies interactions between the input drugs.

It is ideal for quick exploration of interactions between multiple drugs and can be utilized by medical professionals, researchers, and developers working on healthcare applications.

**Main Limitation**: Drug name normalization had to be done according PubChem data.
## Features

- Fetches drug interaction data from PubChem in CSV format.
- Processes multiple drug names provided by the user.
- Identifies interactions between the specified drugs.
- Outputs interaction details directly in the terminal.
- Handles API responses and malformed data gracefully.



## Requirements

Ensure you have the following dependencies installed:

- Python 3.7 or later
- httpx
Install dependencies with-

```bash
pip install httpx

```
## How to Use
1.Clone the repository or download the script file.

2.Install the required library using the command above.

3.Run the script with:
```bash
python drug_interaction_finder.py

```
4.Enter the names of the drugs (space-separated) when prompted. For example:
```java
Enter the drug names (space-separated, e.g., Atenolol Phenytoin Xanthine):
```
5.The script will:
- Fetch interaction data for the drugs from PubChem.
- Save the data in CSV files (one per drug).
- Search for interactions between the specified drugs.
- Display any detected interactions in the terminal.
## Example Output

```
Enter the drug names (space-separated, e.g., Atenolol Phenytoin Xanthine): Atenolol Phenytoin
Fetching data for Atenolol...
Data for Atenolol saved to 'Atenolol_response.csv'
Fetching data for Phenytoin...
Data for Phenytoin saved to 'Phenytoin_response.csv'

Detected Interactions:
Atenolol - Phenytoin: Increases serum levels of Phenytoin
```
## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and bug reports.



## Acknowledgements

Special thanks PubChem for robust database.

