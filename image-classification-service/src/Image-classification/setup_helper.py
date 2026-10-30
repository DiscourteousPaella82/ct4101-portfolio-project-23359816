import os

def get_data_path(data_path_env_name = "DATA_PATH"):
    ""
    data_path = os.getenv(data_path_env_name)
    assert data_path is not None, "IMAGES_PATH could not be read, make sure to set IMAGES_PATH environment variable"

    return data_path