import pytest


class TestConfiguration:
    def test_default(self):
        from pygalaxy.core import config
        del config
        return
    
    @pytest.fixture(scope="class")
    def path_fixture(self, request):
        return request.config.getoption("--path", default=None)
    
    def test_config_reload(self, path_fixture):
        if path_fixture is None:
            return
        else:
            from pygalaxy.core import config
            config.load(path_fixture)
            print(path_fixture, config.COMMON_CONFIG_PATH)
            assert config.COMMON_CONFIG_PATH == path_fixture
    