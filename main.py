import pathlib as pl
import pandas as pd
import json


def import_dict() -> pd.DataFrame:
    file_path = pl.Path('dicionario.txt')
    df = pd.read_csv(file_path, names=['Palavras'])
    return df


def filter_word_len(df: pd.DataFrame, length: int) -> pd.DataFrame:
    df['TAM'] = df['Palavras'].str.len()
    df = df[df['TAM'] == length].reset_index(drop=True)
    return df


def convert_series(df: pd.DataFrame) -> pd.Series:
    df = df['Palavras']
    return df


def lower_letter(df: pd.Series) -> pd.Series:
    df = df.str.lower()
    return df


def replace_accents(df: pd.Series) -> pd.Series:
    file_path = pl.Path('accents.json')
    with open(file_path) as f:
        acc_dict = json.loads(f.read())

    for k, v in acc_dict.items():
        df = df.str.replace(k, v)

    return df


def filter_letters(df: pd.Series, vec_ct: list, vec_nct: list) -> pd.Series:
    new_df = df.copy()
    for let in vec_ct:
        new_df = new_df[new_df.str.contains(let)]

    for let in vec_nct:
        new_df = new_df[~(new_df.str.contains(let))]

    return new_df


def filter_letter_position(new_df: pd.Series, pos_dict: dict) -> pd.Series:
    for k, v in pos_dict.items():
        if v != '':
            new_df = new_df[new_df.str[int(k)-1] == v]

    return new_df


def main():
    df = import_dict()
    df = filter_word_len(df, 5)
    df = convert_series(df)
    df = lower_letter(df)
    df = replace_accents(df)

    vec_ct = ['u', 'e']
    vec_nct = ['n', 'i', 'c', 'a', 'p', 'r', 't', 'o', 'l', 'c', 's']
    new_df = filter_letters(df, vec_ct, vec_nct)

    pos_dict = {
        '1': '',
        '2': 'e',
        '3': '',
        '4': 'u',
        '5': 'e'
    }
    new_df = filter_letter_position(new_df, pos_dict)



