class TestIntegration:
    def test_generic(self):
        import pygalaxy
        del pygalaxy
        return
    
    def test_core(self):
        from pygalaxy import core
        del core
        return