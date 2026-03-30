import ast
from pathlib import Path


def _project_root() -> Path:
    cur = Path(__file__).resolve()
    for parent in [cur, *cur.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("Could not locate project root")


def _read(path: str) -> str:
    return (_project_root() / path).read_text(encoding="utf-8")


def test_lane_a_parser_registry_and_entrypoint():
    source = _read("rag/app/naive.py")
    tree = ast.parse(source)

    # Ensure DoXA entrypoint exists.
    assert any(
        isinstance(node, ast.FunctionDef) and node.name == "by_doxa"
        for node in tree.body
    )

    # Ensure PARSERS map routes doxa -> by_doxa.
    parser_dict = next(
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "PARSERS" for t in node.targets)
    )
    assert isinstance(parser_dict, ast.Dict)

    mapping = {
        key.value: val.id
        for key, val in zip(parser_dict.keys, parser_dict.values)
        if isinstance(key, ast.Constant)
        and isinstance(key.value, str)
        and isinstance(val, ast.Name)
    }
    assert mapping.get("doxa") == "by_doxa"


def test_lane_a_chunk_strategy_includes_doxa():
    source = _read("rag/app/naive.py")
    assert '["tcadp", "docling", "mineru", "paddleocr", "doxa"]' in source


def test_lane_b_parse_method_validation_includes_doxa():
    source = _read("rag/flow/parser/parser.py")
    assert '"doxa"' in source
    assert (
        'if pdf_parse_method.lower() not in ["deepdoc", "plain_text", "mineru", "docling", "tcadp parser", "paddleocr", "doxa"]'
        in source
    )


def test_lane_b_pdf_branch_has_doxa_parser_path():
    source = _read("rag/flow/parser/parser.py")
    assert 'elif parse_method.lower() == "doxa":' in source
    assert 'doxa_parser = DoxaParser(' in source
    assert 'parse_method=conf.get("doxa_parse_method", "default")' in source
