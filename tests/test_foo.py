from tw_mirror.core import out_sync


def test_foo():
    assert out_sync([]) == "foo"
