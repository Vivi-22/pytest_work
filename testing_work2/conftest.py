import pytest


def pytest_collection_modifyitems(session, config, items: list):
    # 自动添加标签(add, sub, mul, div四种)
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
