from pathlib import Path
from datetime import datetime
import shutil
import argparse


def collect_errors(logs_folder: Path, output_folder: Path, archive_folder: Path) -> None:
    if not logs_folder.exists():
        print("❌ Dossier introuvable :", logs_folder)
        return

    output_folder.mkdir(parents=True, exist_ok=True)
    archive_folder.mkdir(parents=True, exist_ok=True)

    log_files = [p for p in logs_folder.rglob("*.log") if "__MACOSX" not in str(p)]

    if len(log_files) == 0:
        print("ℹ️ Aucun fichier .log trouvé dans :", logs_folder)
        return

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    errors_file = output_folder / f"errors_{stamp}.log"

    with errors_file.open("w", encoding="utf-8") as out:
        for log in log_files:
            text = log.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                if "ERROR" in line:
                    out.write(f"{log.name}: {line}\n")

            shutil.move(str(log), str(archive_folder / log.name))

    print("✅ Fichier erreurs créé :", errors_file)
    print("📦 Logs archivés dans :", archive_folder)
    print("🔢 Nombre de logs traités :", len(log_files))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logs", default="raw_logs")
    parser.add_argument("--out", default="output")
    parser.add_argument("--archive", default="archive")
    args = parser.parse_args()
    collect_errors(Path(args.logs), Path(args.out), Path(args.archive))


if __name__ == "__main__":
    main()
