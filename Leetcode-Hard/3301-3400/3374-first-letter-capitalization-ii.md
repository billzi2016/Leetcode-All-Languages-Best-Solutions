# 3374. First Letter Capitalization II

## MySQL
```sql
# Write your MySQL query statement below
WITH RECURSIVE cte AS (
    SELECT 
        content_id,
        content_text,
        1 AS pos,
        CASE
            WHEN SUBSTRING(content_text,1,1) REGEXP '[a-zA-Z]' THEN UPPER(SUBSTRING(content_text,1,1))
            ELSE SUBSTRING(content_text,1,1)
        END AS ch
    FROM user_content
    UNION ALL
    SELECT 
        content_id,
        content_text,
        pos + 1,
        CASE
            WHEN SUBSTRING(content_text,pos+1,1) REGEXP '[a-zA-Z]' THEN
                IF(SUBSTRING(content_text,pos,1) IN (' ', '-'),
                   UPPER(SUBSTRING(content_text,pos+1,1)),
                   LOWER(SUBSTRING(content_text,pos+1,1)))
            ELSE SUBSTRING(content_text,pos+1,1)
        END AS ch
    FROM cte
    WHERE pos < CHAR_LENGTH(content_text)
)
SELECT 
    content_id,
    content_text AS original_text,
    GROUP_CONCAT(ch ORDER BY pos SEPARATOR '') AS converted_text
FROM cte
GROUP BY content_id, content_text;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT 
        content_id,
        LOWER(content_text) AS txt,
        1 AS pos,
        CASE 
            WHEN SUBSTRING(LOWER(content_text),1,1) BETWEEN 'a' AND 'z'
                THEN UPPER(SUBSTRING(LOWER(content_text),1,1))
            ELSE SUBSTRING(LOWER(content_text),1,1)
        END AS acc
    FROM user_content

    UNION ALL

    SELECT 
        content_id,
        txt,
        pos + 1,
        acc + CASE 
                WHEN SUBSTRING(txt,pos,1) BETWEEN 'a' AND 'z'
                     AND (SUBSTRING(txt,pos-1,1) = ' ' OR SUBSTRING(txt,pos-1,1) = '-')
                    THEN UPPER(SUBSTRING(txt,pos,1))
                ELSE SUBSTRING(txt,pos,1)
              END
    FROM cte
    WHERE pos < LEN(txt)
)
SELECT 
    u.content_id,
    u.content_text AS original_text,
    f.acc AS converted_text
FROM user_content u
JOIN (
    SELECT content_id, acc
    FROM cte
    WHERE pos = LEN(txt)
) f ON u.content_id = f.content_id
ORDER BY u.content_id
OPTION (MAXRECURSION 0);
```

## OracleSQL
```sql
SELECT
    content_id,
    content_text AS original_text,
    INITCAP(content_text) AS converted_text
FROM user_content;
```

## PythonData
```python
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def transform(text: str) -> str:
        if not isinstance(text, str):
            return text
        def cap_part(part: str) -> str:
            return part[:1].upper() + part[1:].lower() if part else ""
        def cap_word(word: str) -> str:
            return "-".join(cap_part(p) for p in word.split("-"))
        return " ".join(cap_word(w) for w in text.split())
    
    result = user_content.copy()
    result["original_text"] = result["content_text"]
    result["converted_text"] = result["content_text"].apply(transform)
    return result[["content_id", "original_text", "converted_text"]]
```

## PostgreSQL
```sql
SELECT 
    content_id,
    content_text AS original_text,
    regexp_replace(
        lower(content_text),
        '(^|[ -])([a-z])',
        '\1\U\2',
        'g'
    ) AS converted_text
FROM user_content;
```
