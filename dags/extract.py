import pandas as pd

def extract(csv_file):
    
    df = pd.read_csv(csv_file)
    return df['context']

def save(data, output):
    
    with open(output, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
