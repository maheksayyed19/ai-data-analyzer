from fastapi import FastAPI, UploadFile, File 
import pandas as pd 

app = FastAPI()

@app.get("/")
def home():
    return { "message", "AI Data Analyzer API is running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)): 
    df = pd.read_csv(file.file)

    return {
        "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict()
    }