from __future__ import annotations

import argparse
from pathlib import Path

from utils.io import parse_csv, collect_errors


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Mini-projet: nettoyage CSV + collecte erreurs logs")
    p.add_argument("--input", required=True, help="Chemin CSV (ex: data/data.csv)")
    p.add_argument("--logs", required=True, help="Dossier logs (ex: raw_logs)")
    p.add_argument("--out", required=True, help="Dossier sortie (ex: output)")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    input_csv = Path(args.input)
    logs_dir = Path(args.logs)
    out_dir = Path(args.out)
    archive_dir = Path("archive")

    clean_path, bad_path = parse_csv(input_csv, out_dir)
    errors_path = collect_errors(logs_dir, out_dir, archive_dir)

    print("✅ Terminé.")
    print(f"- CSV clean -> {clean_path}")
    if errors_path:
        print(f"- Errors -> {errors_path}")
    else:
        print("- Errors -> aucun log à traiter")
    if bad_path:
        print(f"- Bad lines -> {bad_path}")
    print(f"- Archive -> {archive_dir}")


if __name__ == "__main__":
    main()
