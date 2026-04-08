import importlib


def test_settings_exists():
    config = importlib.import_module("config")
    assert hasattr(config, "SETTINGS")
    assert config.SETTINGS.sample_rate > 0
