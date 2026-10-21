"""Resume un DataFrame y exporta el resumen a un archivo TXT."""

from pathlib import Path
import pandas as pd


class DatasetSummarizer:
    """Crea un resumen de dimensiones, tipos, nulos y estadísticas."""

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def build_summary(self) -> str:
        """Construye y devuelve el resumen como texto."""
        df = self.dataframe
        lines = [
            "RESUMEN DEL DATASET",
            "=" * 60,
            f"Cantidad de filas: {df.shape[0]}",
            f"Cantidad de columnas: {df.shape[1]}",
            "",
            "COLUMNAS Y TIPOS DE DATOS",
            "-" * 60,
        ]
        if df.shape[1] == 0:
            lines.append("El DataFrame no tiene columnas.")
        else:
            for column in df.columns:
                lines.append(f"- {column}: {df[column].dtype}")

        lines.extend(["", "VALORES NULOS POR COLUMNA", "-" * 60])
        if df.shape[1] == 0:
            lines.append("No hay columnas para revisar.")
        else:
            for column, count in df.isna().sum().items():
                lines.append(f"- {column}: {int(count)}")

        lines.extend(["", "ESTADÍSTICAS DESCRIPTIVAS", "-" * 60])
        lines.append(
            df.describe(include="all").to_string()
            if not df.empty else "El DataFrame está vacío."
        )
        lines.append("")
        return "\n".join(lines)

    def save_summary(self, output_path: str = "resumen_dataset.txt") -> str:
        """Guarda el resumen en UTF-8 y devuelve la ruta del archivo."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.build_summary(), encoding="utf-8")
        return str(path)
