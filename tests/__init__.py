"""Adds main code folder to path for simplified imports."""

import logging
import sys
from pathlib import Path

# For testing in the pipeline
current_working_dir = Path.cwd()
logging.debug(f"<TESTS> Extending working directory: {current_working_dir}")
sys.path.extend([str(current_working_dir / "src/"), str(Path(__file__).parent.absolute())])