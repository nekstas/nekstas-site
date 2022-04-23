# -*- coding: utf-8 -*-
import os

from backend.core import config


class CountItem:
    def __init__(self, ext, name, comment_prefix=''):
        self.ext = ext
        self.name = name
        self.comment_prefix = comment_prefix

        self.files_count = 0
        self.all_count = 0
        self.useful_count = 0

    def useful_filter(self, line):
        return (
            line.strip() and
            not line.strip().startswith(self.comment_prefix)
        )

    def check(self, file):
        return os.path.splitext(file)[1] == self.ext

    def count(self, lines):
        self.files_count += 1
        self.all_count += len(lines)
        self.useful_count += len([*filter(self.useful_filter, lines)])

    def print(self, i):
        print(f'{i}. {self.name} '
              f'- {self.files_count} файлов '
              f'- {self.all_count} всего строк '
              f'- {self.useful_count} полезных строк')


class CountLines:
    def __init__(self, *count_items, ignored_folders=()):
        self.count_items = count_items
        self.ignored_folders = ignored_folders

    def check_path(self, path):
        path = path.replace('\\', '/') + '/'
        return not any(
            ('/' + folder + '/') in path
            for folder in self.ignored_folders
        )

    def count(self, root_path):
        for path, _, files in os.walk(root_path):
            if not self.check_path(path):
                continue

            for file in files:
                path_to_file = os.path.join(path, file)

                for count_item in self.count_items:
                    if count_item.check(file):
                        with open(path_to_file, 'r', encoding='UTF-8') \
                                as code_file:
                            count_item.count(code_file.readlines())

    def print(self, project_name):
        print('Статистика', project_name, end='\n\n')
        for i, count_item in enumerate(self.count_items, 1):
            count_item.print(i)


def main():
    count_lines = CountLines(
        CountItem('.py', 'Python файлы', '#'),
        CountItem('.html', 'Python файлы', ''),
        CountItem('.css', 'Python файлы', ''),
        CountItem('.js', 'Python файлы', '//'),
        ignored_folders=('.git', '.idea', 'venv')
    )
    count_lines.count(config.PROJECT_ROOT)
    count_lines.print(config.PROJECT_NAME)


if __name__ == '__main__':
    main()
