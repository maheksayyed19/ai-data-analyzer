import pandas as pd 

def analyze_csv(file): 
    df = pd.read_csv(file) 
    
    summary = {
    "columns": list(df.columns),
    "shape": df.shape,
    "sample_data": df.head(5).to_dict(),
    "numeric_summary": df.describe().to_dict()
}

    return df, summary