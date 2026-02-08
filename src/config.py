from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "BrentOilPrices.csv"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

IMAGES_PATH = BASE_DIR / "images"

# Create required folders
for path in [DATA_DIR, PROCESSED_DATA_DIR, IMAGES_PATH]:
    path.mkdir(parents=True, exist_ok=True)

# Validate raw data existence
if not RAW_DATA_PATH.exists():
    raise FileNotFoundError(
        f"Raw data file not found at {RAW_DATA_PATH}. "
        "Please ensure BrentOilPrices.csv exists."
    )
