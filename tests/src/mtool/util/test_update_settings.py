from unittest.mock import patch
import pytest

@patch('builtins.input', lambda *args: 'q')
def test_quit_update_settings(setup, setup_telemetry, telemetry_db):
    from src.mtool.util import update_settings

    assert update_settings.update_settings(telemetry_db) == 0


def test_value_error(setup, setup_telemetry, telemetry_db):
    from src.mtool.util import update_settings

    assert update_settings.get_ordinal("not_ord", update_settings.get_values(telemetry_db), telemetry_db) == "not_ordinal"

@patch('builtins.input', lambda *args: 'nn')
def test_edit_settings(setup, setup_telemetry, telemetry_db):
    from src.mtool.util import update_settings

    update_settings.edit_settings(1, update_settings.get_values(telemetry_db), telemetry_db)
    