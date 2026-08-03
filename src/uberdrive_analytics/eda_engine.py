import pandas as pd
import numpy as np

class UberEDAEngine:
    """Analytical engine providing metrics and breakdowns for Uber ride data."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_metrics(self) -> dict:
        """Returns overall KPI metrics."""
        return {
            "total_trips": len(self.df),
            "total_miles": round(self.df['MILES*'].sum(), 2),
            "avg_trip_miles": round(self.df['MILES*'].mean(), 2),
            "avg_duration_min": round(self.df['DURATION_MIN'].mean(), 2),
            "business_trips_pct": round((self.df['CATEGORY*'] == 'Business').mean() * 100, 1),
        }

    def trips_by_purpose(self) -> pd.Series:
        """Counts trips grouped by purpose."""
        return self.df['PURPOSE*'].value_counts(dropna=False)

    def top_pickup_locations(self, top_n: int = 10) -> pd.Series:
        """Returns top N pickup locations."""
        return self.df['START*'].value_counts().head(top_n)

    def top_dropoff_locations(self, top_n: int = 10) -> pd.Series:
        """Returns top N dropoff locations."""
        return self.df['STOP*'].value_counts().head(top_n)

    def hourly_distribution(self) -> pd.Series:
        """Counts trips by hour of the day."""
        return self.df['HOUR'].value_counts().sort_index()

    def monthly_mileage(self) -> pd.Series:
        """Sums total miles driven per month."""
        return self.df.groupby('MONTH_NAME')['MILES*'].sum()
