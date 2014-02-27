import io_file


def scan_annotation(file_list):
	occurrencies = 0
	for file_path in file_list:
		content = io_file.get_file_content(file_path)
		if (__check(content)):
			occurrencies = occurrencies + 1
	return occurrencies

def __check(content):
	return any('@Refactoring' in line for line in content)