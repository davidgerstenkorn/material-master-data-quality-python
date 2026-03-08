import pandas as pd


def load_material_data(path):
    """
    Load material master dataset from CSV
    """
    df = pd.read_csv(path)
    return df