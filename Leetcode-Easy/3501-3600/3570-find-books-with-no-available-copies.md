# 3570. Find Books with No Available Copies

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    COUNT(*) AS current_borrowers
FROM library_books b
JOIN borrowing_records r 
    ON b.book_id = r.book_id
   AND r.return_date IS NULL
GROUP BY b.book_id
HAVING COUNT(*) >= b.total_copies
ORDER BY current_borrowers DESC, b.title ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    COUNT(r.record_id) AS current_borrowers
FROM library_books AS b
JOIN borrowing_records AS r
      ON b.book_id = r.book_id
     AND r.return_date IS NULL
GROUP BY
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    b.total_copies
HAVING COUNT(r.record_id) = b.total_copies
ORDER BY
    current_borrowers DESC,
    b.title ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    cnt.current_borrowers
FROM library_books b
JOIN (
    SELECT book_id, COUNT(*) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
) cnt ON b.book_id = cnt.book_id
WHERE cnt.current_borrowers = b.total_copies
ORDER BY cnt.current_borrowers DESC, b.title ASC;
```

## PythonData
```python
import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    # Records where the book has not been returned yet
    ongoing = borrowing_records[borrowing_records["return_date"].isna()]
    
    # Count current borrowers per book
    borrower_counts = (
        ongoing.groupby("book_id")
        .size()
        .reset_index(name="current_borrowers")
    )
    
    # Join with library books information
    merged = pd.merge(library_books, borrower_counts, on="book_id", how="inner")
    
    # Keep books where all copies are currently borrowed
    filtered = merged[merged["current_borrowers"] == merged["total_copies"]]
    
    # Select required columns and sort as specified
    result = filtered[
        ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"]
    ].sort_values(by=["current_borrowers", "title"], ascending=[False, True])
    
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    COUNT(r.record_id) AS current_borrowers
FROM library_books b
JOIN borrowing_records r 
    ON b.book_id = r.book_id
   AND r.return_date IS NULL
GROUP BY 
    b.book_id, b.title, b.author, b.genre, b.publication_year, b.total_copies
HAVING COUNT(r.record_id) = b.total_copies
ORDER BY current_borrowers DESC, b.title ASC;
```
