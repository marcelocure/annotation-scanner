import pytest
from annscan import scanner

parametrize = pytest.mark.parametrize


class Test(object):
    def test_scan_annotations(self):
        file_path1 = 'tests/resources/testfileoneline.java'
        file_path2 = 'tests/resources/testfiletwolines.java'
        file_list = [file_path1, file_path2]
        occurrencies = scanner.scan_annotation(file_list)
        assert occurrencies == 1
