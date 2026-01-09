from __future__ import annotations

from pathlib import Path
from datetime import datetime
import shutil
import pandas as pd

from utils.paths import ensure_dir


def normalize_columns(cols: list[str]) -> list[str]:
    return [c.strip().lower().replace(" ", "_") for c in cols]


def parse_csv(input_file: Path, out_dir: Path) -> tuple[Path, Path | None]:
    if not input_file.exists():
        raise FileNotFoundError(f"CSV introuvable: {input_file}")

    ensure_dir(out_dir)
    output_file = out_dir / "clean_data.csv"
    bad_file = out_dir / "bad_lines.csv"

    bad_lines: list[object] = []

    def save_bad_line(bad_line) -> None:
        bad_lines.append(bad_line)

    df = pd.read_csv(
        input_file,
        sep=";",
        dtype=str,
        encoding="utf-8",
        engine="python",
        on_bad_lines=save_bad_line,
    )

    df.columns = normalize_columns(list(df.columns))
    df = df.replace(r"^\s*$", None, regex=True).dropna(how="all")

    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    if "id_client" in df.columns:
        df = df.drop_duplicates(subset=["id_client"], keep="first")

    df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

    bad_path: Path | None = None
    if bad_lines:
        def as_text(x) -> str:
            if isinstance(x, list):
                return ";".join(map(str, x))
            return str(x)

        bad_file.write_text("\n".join(as_text(x) for x in bad_lines) + "\n", encoding="utf-8")
        bad_path = bad_file

    return output_file, bad_path


def collect_errors(raw_logs: Path, out_dir: Path, archive_dir: Path) -> Path | None:
    if not raw_logs.exists():
        raise FileNotFoundError(f"Dossier logs introuvable: {raw_logs}")

    ensure_dir(out_dir)
    ensure_dir(archive_dir)

    log_files = sorted(raw_logs.glob("*.log"))
    if not log_files:
        print(f"ℹ️ Aucun fichier .log trouvé dans {raw_logs}")
        return None

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    errors_file = out_dir / f"errors_{stamp}.log"

    with errors_file.open("w", encoding="utf-8") as out:
        for log in log_files:
            text = log.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                if "ERROR" in line:
                    out.write(f"{log.name}: {line}\n")
            shutil.move(str(log), str(archive_dir / log.name))

    return errors_file
