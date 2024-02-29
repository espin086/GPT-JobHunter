import json
import logging
import pprint

import config
from FileHandler import FileHandler
from SQLiteHandler import check_and_upload_to_db, create_db_if_not_there

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(
    level=config.LOGGING_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = FileHandler(
    raw_path=config.RAW_DATA_PATH, processed_path=config.PROCESSED_DATA_PATH
)


def add_primary_key(json_list):
    """
    This function adds a primary key to each JSON object in the list.
    """
    logging.info("Adding primary keys to JSON data.")
    for item in json_list:
        try:
            company = item.get("company", "")
            title = item.get("title", "")
            primary_key = f"{company} - {title}"
            item["primary_key"] = primary_key
        except AttributeError as e:
            logging.error(
                "AttributeError %s occurred while processing %s. Skipping item.",
                e,
                item,
            )
    return json_list


def load():
    """
    This function loads the JSON files from the processed folder and uploads them to the database.
    """
    logging.info("Main loading function initiated.")
    data = file_handler.load_json_files(directory=config.PROCESSED_DATA_PATH)
    data = add_primary_key(json_list=data)
    create_db_if_not_there()
    check_and_upload_to_db(json_list=data)


if __name__ == "__main__":
    logging.info("Jobhunter application started.")
    load()
    logging.info("Jobhunter application finished.")
