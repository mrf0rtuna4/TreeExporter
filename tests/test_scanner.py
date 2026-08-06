from tree_exporter.scanner import scan_repository


def test_scan_returns_list() -> None:
    result = scan_repository(".")

    assert isinstance(result, list)
