import pandas as pd
import numpy as np
from pathlib import Path

class UberDataLoader:
    """Utility class to load and preprocess Uber Drive ride data."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def load_clean_data(self) -> pd.DataFrame:
        """Loads and cleans Uber Drives CSV data."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Dataset not found at {self.filepath}")

        df = pd.read_csv(self.filepath)

        # Drop footer rows if any summary exists
        df = df[df['START_DATE*'].notna() & ~df['START_DATE*'].str.contains("Total", na=False)].copy()

        # Parse datetime columns
        df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
        df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')

        # Drop invalid date rows
        df = df.dropna(subset=['START_DATE*', 'END_DATE*']).copy()

        # Extract temporal features
        df['DURATION_MIN'] = (df['END_DATE*'] - df['START_DATE*']).dt.total_seconds() / 60.0
        df['HOUR'] = df['START_DATE*'].dt.hour
        df['DAY_NAME'] = df['START_DATE*'].dt.day_name()
        df['MONTH_NAME'] = df['START_DATE*'].dt.month_name()
        df['MONTH'] = df['START_DATE*'].dt.month

        # Categorize speed in mph
        df['SPEED_MPH'] = np.where(
            df['DURATION_MIN'] > 0,
            (df['MILES*'] / (df['DURATION_MIN'] / 60.0)),
            0
        )

        return df
