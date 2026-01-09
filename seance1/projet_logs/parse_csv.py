import pandas as pd
from pathlib import Path


def parse_csv() -> None:
    input_file = Path("data.csv")
    output_file = Path("output/clean_data.csv")
    bad_file = Path("output/bad_lines.csv")

    output_file.parent.mkdir(parents=True, exist_ok=True)

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

    # Renommage colonnes
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Valeurs manquantes (vides / espaces -> None)
    df = df.replace(r"^\s*$", None, regex=True)
    df = df.dropna(how="all")

    # Conversion types
    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    # Doublons
    if "id_client" in df.columns:
        df = df.drop_duplicates(subset=["id_client"], keep="first")

    # Export clean
    df.to_csv(output_file, index=False, sep=";", encoding="utf-8")

    # Export lignes rejetées (robuste str OU list)
    if bad_lines:
        def as_text(x) -> str:
            if isinstance(x, list):
                return ";".join(map(str, x))
            return str(x)

        bad_file.write_text("\n".join(as_text(x) for x in bad_lines) + "\n", encoding="utf-8")

    print("✅ Fichier clean créé :", output_file)
    print("⚠️ Lignes rejetées :", len(bad_lines), "(voir", bad_file, ")")


if __name__ == "__main__":
    parse_csv()
