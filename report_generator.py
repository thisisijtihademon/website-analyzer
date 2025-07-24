# report_generator.py
import pandas as pd

def save_report(results, filename='website_report.xlsx'):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False)
