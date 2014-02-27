import os


def scan_path(path):
    output_file = 'files.txt'
    output = open(output_file, 'wb')
    __read_dir(path, output)
    output.close()
    return get_file_content(output_file)


def get_file_content(file_path):
    with open(__remove_break_line(file_path)) as f:
        return f.readlines()


def __remove_break_line(file_path):
    return file_path.replace('\n', '')


def __read_dir(path, output):
    dirlist = os.listdir(path)

    for current in dirlist:
        file_path = '{0}/{1}'.format(path, current)
        if os.path.isdir(file_path):
            __read_dir(file_path, output)
        else:
            __save_java_files(output, file_path)


def __save_java_files(output, file_path):
    if __is_java_file(file_path):
        __write_output(output, file_path)


def __is_java_file(file_path):
    return file_path.endswith('.java')


def __write_output(f, current):
    f.write('{0}{1}'.format(current, '\n'))
