import pandas as pd

def update_availability(book_id: int, copies: int, df_books: pd.DataFrame) -> pd.DataFrame:
    if book_id in df_books['book_id'].values:
        df_books.loc[df_books['book_id'] == book_id, 'copies_available'] = copies
    return df_books
