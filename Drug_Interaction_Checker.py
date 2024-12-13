import httpx
import csv
import os

def fetch_drug_data(drug_name):
    # URL for the SDQ agent query with a placeholder for the drug name
    url = f"https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=csv&query={{%22download%22:%22*%22,%22collection%22:%22drugbankddi%22,%22order%22:[%22cid2,asc%22],%22start%22:1,%22limit%22:10000000,%22downloadfilename%22:%22pubchem_name_%5E{drug_name}%24_drugbankddi%22,%22where%22:{{%22ands%22:[{{%22name%22:%22%5E{drug_name}%24%22}}]}}}}"

    try:
        response = httpx.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Generate the correct filename based on the drug name
        filename = f"{drug_name}_response.csv"

        # Save the response as a .csv file (even if it's served with a non-CSV content type)
        with open(filename, "wb") as file:  # Use binary mode to handle the gzipped response correctly
            file.write(response.content)  # Write the raw content to the file
        print(f"File saved as '{filename}'")

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def search_interactions_for_drugs(drugs_to_check):
    interactions = set()  # Use a set to avoid duplicates

    # Step 1: Fetch data for each drug and save the files
    for drug_name in drugs_to_check:
        fetch_drug_data(drug_name)

    # Step 2: Now, read the saved files and search for interactions
    for drug_name in drugs_to_check:
        filename = f"{drug_name}_response.csv"
        if os.path.exists(filename):  # Check if the file exists
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                for row in reader:
                    drug1 = row[3]  # First drug in interaction
                    drug2 = row[5]  # Second drug in interaction
                    interaction = row[6]  # Interaction details
                    
                    # Check if drug1 and drug2 are both in the list of drugs to check
                    if drug1 in drugs_to_check and drug2 in drugs_to_check:
                        # Ensure the interaction is stored in a unique, order-independent way
                        interaction_tuple = tuple(sorted([drug1, drug2]))  # Sort the drugs to ensure order doesn't matter
                        if interaction_tuple not in interactions:
                            interactions.add(interaction_tuple)
                            print(f"{drug1} - {drug2}: {interaction}")
        else:
            print(f"File for {drug_name} not found.")
    
    # If no interactions found, notify the user
    if not interactions:
        print("No interactions found between the drugs.")

# User input for multiple drug names (space-separated)
input_drugs = input("Enter the drug names (space-separated, e.g., Atenolol Phenytoin Xanthine): ")

# Convert input into a list of drug names
drugs_to_check = input_drugs.split()

# Search for interactions among the drugs
search_interactions_for_drugs(drugs_to_check)
