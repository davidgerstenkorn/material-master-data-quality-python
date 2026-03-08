import pandas as pd


def check_negative_stock(df):
    return df[df["current_stock"] < 0]


def check_missing_description(df):
    return df[df["material_description"].isna()]


def check_missing_base_unit(df):
    return df[df["base_unit"].isna()]


def check_missing_lead_time(df):
    return df[df["lead_time_days"].isna()]


def check_duplicates(df):
    return df[df.duplicated("material_id")]