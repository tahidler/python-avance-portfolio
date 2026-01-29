import argparse
import json
import logging
import os
from typing import Any

from parsers import parse_csv, parse_json, parse_xml
from utils.logger import get_logger


def parse_file(path: str) -> Any:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return parse_csv(path)
    if ext == ".json":
        return parse_json(path)
    if ext == ".xml":
        return parse_xml(path)
    raise ValueError(f"Unsupported file extension: {ext}")


def write_json(data: Any, output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parser des fichiers CSV/JSON/XML.")
    parser.add_argument("path", help="Chemin vers le fichier d'entrée")
    parser.add_argument(
        "--export-json",
        dest="export_json",
        help="Écrire la sortie parsée dans un fichier JSON",
    )
    parser.add_argument(
        "--log-level",
        dest="log_level",
        default="INFO",
        help="Niveau de logs (DEBUG, INFO, WARNING, ERROR)",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    logger = get_logger(level=getattr(logging, args.log_level.upper(), logging.INFO))

    try:
        logger.info("Parsing du fichier : %s", args.path)
        data = parse_file(args.path)
        if args.export_json:
            write_json(data, args.export_json)
            logger.info("JSON exporté vers : %s", args.export_json)
        else:
            # Affiche un aperçu court pour un retour rapide
            preview = json.dumps(data, ensure_ascii=False, indent=2)
            print(preview[:2000])
        return 0
    except FileNotFoundError:
        logger.error("Fichier introuvable : %s", args.path)
        return 1
    except Exception as exc:
        logger.error("Erreur : %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
