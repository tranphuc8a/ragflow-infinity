from common.parser_config_utils import normalize_layout_recognizer


def test_normalize_layout_recognizer_doxa_alias():
    recognizer, model = normalize_layout_recognizer("my-doxa-model@doxa")
    assert recognizer == "DoXA"
    assert model == "my-doxa-model"


def test_normalize_layout_recognizer_mineru_alias():
    recognizer, model = normalize_layout_recognizer("mineru-1.0@mineru")
    assert recognizer == "MinerU"
    assert model == "mineru-1.0"


def test_normalize_layout_recognizer_passthrough_non_string():
    recognizer, model = normalize_layout_recognizer(None)
    assert recognizer is None
    assert model is None
