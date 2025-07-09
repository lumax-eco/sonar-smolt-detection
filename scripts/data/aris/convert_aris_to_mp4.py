"""
CLI script to export an ARIS file into an MP4 file.
"""

import argparse
import logging
from pathlib import Path

from sonar_smolt_detection.aris.pyARIS import (
    DataImport,
    VideoExportOriginal_NoProgressBar,
)


def make_cli_parser() -> argparse.ArgumentParser:
    """
    Make the CLI parser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filepath-save",
        help="filepath to save the mp4 export",
        type=Path,
        default=Path("./data/01_raw/mp4/test_video.mp4"),
        required=True,
    )
    parser.add_argument(
        "--filepath-aris",
        help="ARIS file to convert to mp4",
        type=Path,
        default=Path("./data/01_raw/aris/test_video.aris"),
        required=True,
    )
    parser.add_argument(
        "-log",
        "--loglevel",
        default="info",
        help="Provide logging level. Example --loglevel debug, default=warning",
    )
    return parser


def validate_parsed_args(args: dict) -> bool:
    """
    Return whether the parsed args are valid.
    """
    if not args["filepath_aris"].exists() and args["filepath_aris"].is_file():
        logging.error(
            f"Invalid --filepath-aris file, the file {args['filepath_aris']} does not exist"
        )
        return False
    return True


if __name__ == "__main__":
    cli_parser = make_cli_parser()
    args = vars(cli_parser.parse_args())
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=args["loglevel"].upper())
    if not validate_parsed_args(args):
        logger.error("Invalid arguments")
        exit(1)
    else:
        logger.info(args)
        filepath_save = args["filepath_save"]
        filepath_aris = args["filepath_aris"]
        filepath_save.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Loading and parsing the ARIS file {filepath_aris}")
        aris_data, _ = DataImport(str(filepath_aris))
        logger.info(f"Converting the ARIS file {filepath_aris} into a MP4 file.")
        VideoExportOriginal_NoProgressBar(aris_data, filepath_save)
        logger.info(f"Video exported {filepath_save}")
        logger.info("Done ✅")
        exit(0)
