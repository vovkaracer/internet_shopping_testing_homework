def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')