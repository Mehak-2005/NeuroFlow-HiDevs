import pandas as pd
from . import ExtractedPage

def extract_csv(file_path):
    df = pd.read_csv(file_path)

    return [ExtractedPage(
        page_number=0,
        content=df.head().to_string(),
        content_type="table",
        metadata={}
    )]