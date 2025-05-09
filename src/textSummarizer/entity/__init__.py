from dataclasses import dataclass
from pathlib import Path  ##this is we are creating entity to get return type of a function

@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: Path
  source_URL:str                # This we have made a return type
  local_data_file:Path
  unzip_dir:Path