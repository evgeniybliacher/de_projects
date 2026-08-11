import pandas as pd

def get_dataframe(df: pd.DataFrame, head:int|None = None, tail:int|None = None) -> pd.DataFrame:
    if head is None and tail is None:
        return df
    elif head is not None:
        return df.head(head)
    elif tail is not None:
        return df.tail(tail)
    raise ValueError("Both head and tail parameters cannot be defined.")

def overview(df: "pd.DataFrame")-> list[str]:
    return [str(df.shape[0]), str(df.shape[1]), memory_size(df)]

def format_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def memory_size(df: pd.DataFrame) -> str:
    return format_size(df.memory_usage(deep=True).sum())