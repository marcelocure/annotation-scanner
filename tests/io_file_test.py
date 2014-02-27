import pytest
from annscan import io_file

parametrize = pytest.mark.parametrize


class Test(object):
    @parametrize('file_to_read', ['tests/resources/testfileoneline.java'])
    def test_get_file_content_one_line(self, file_to_read):
        content = io_file.get_file_content(file_to_read)
        assert len(content) == 1
        assert content[0] == 'test file . java @Refactoring'

    @parametrize('file_to_read', ['tests/resources/testfiletwolines.java'])
    def test_get_file_content_two_lines(self, file_to_read):
        content = io_file.get_file_content(file_to_read)
        assert len(content) == 2
        assert content[0] == 'test file . java\n'
        assert content[1] == 'second line'

    @parametrize('path', ['tests/resources'])
    def test_scan_path(self, path):
        content = io_file.scan_path(path)
        assert len(content) == 2
        assert content[0] == 'tests/resources/testfileoneline.java\n'
        assert content[1] == 'tests/resources/testfiletwolines.java\n'
