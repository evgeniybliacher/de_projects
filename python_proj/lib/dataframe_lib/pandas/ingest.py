import pandas as pd
from dataframe_lib.common.guards import ensure, require
from dataframe_lib.common.validators import is_valid_string, is_file_exists
from dataframe_lib.common.pathes import DATA_PATH
from returns.result import safe
from dataframe_lib.common.logging_config import create_logger

logger = create_logger("ingest")

@safe
def load_dataset(name: str, type: str)->pd.DataFrame:
    require(is_valid_string(name), "The name of dataset is not defined")
    require(is_valid_string(type), "The type of dataset is not defined")

    full_path = f"{DATA_PATH}/{name}.{type}"
    logger.debug(f"The full dataset path is {full_path}")
    require(is_file_exists(full_path), f"The dataset path {full_path} is not exists")
    if type.lower() == "csv":
        df = pd.read_csv(full_path)
    elif type.lower() == "parquet":
        df = pd.read_parquet(full_path)
    else:
        raise ValueError("The type of dateset type {type} is not supported. Supported types are csv or parquet")
    ensure (df is not None, "The data set is not load correctly")
    logger.debug("The dataset was loaded succesfully")
    return df 
