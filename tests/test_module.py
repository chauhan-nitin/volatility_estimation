"""Module to test basic functionality"""
import pytest
import pandas as pd
from src.Engine import get_data

def get_input():
    # Act
    result = get_data()
    # Assert
    # Check if ValidationError is raised
    assert isinstance(result, pd.DataFrame), "The result is not a Pandas DataFrame"