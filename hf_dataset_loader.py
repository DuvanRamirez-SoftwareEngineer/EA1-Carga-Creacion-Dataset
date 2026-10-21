"""Carga un dataset público de Hugging Face y lo convierte en DataFrame."""

import pandas as pd
from datasets import load_dataset


class HFDatasetLoader:
    """Extrae un split de Hugging Face y lo devuelve como DataFrame de pandas."""

    def __init__(self, dataset_id: str, split: str = "train"):
        self.dataset_id = dataset_id
        self.split = split

    def load_dataframe(self) -> pd.DataFrame:
        """Carga el dataset indicado y devuelve sus datos como DataFrame."""
        dataset = load_dataset(self.dataset_id, split=self.split)
        return dataset.to_pandas()
