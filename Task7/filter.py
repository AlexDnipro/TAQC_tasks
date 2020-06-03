import sys
from abc import ABC, abstractmethod
from enum import Enum
from contextlib import contextmanager
import re


class Filter(ABC):
    @abstractmethod
    def name(self):
        """Provides a name of the rule (like FP005)."""
        pass
    
    @abstractmethod
    def matches(self, line: str):
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass


class FP001(Filter):
    def name(self):
        return 'FP001'
    def matches(self, line: str):
        """"Checks if line ends with '.' """
        return line.endswith('.')

class FP002(Filter):
    def name(self):
        return 'FP002'
    def matches(self, line: str):
        """"Checks if line has less than 100 characters """
        return len(line.strip()) > 0 and len(line.rstrip()) < 100

class FP003(Filter):
    def name(self):
        return 'FP003'
    def matches(self, line: str):
        """"Checks if line contains at least 5 'a' letters """
        return line.count('a') >= 5

class FN201(Filter):
    def name(self):
        return 'FN201'
    def matches(self, line: str):
        """"Checks if line has more then 3 'z' letters """
        return line.count('z') > 3

class FN202(Filter):
    def name(self):
        return 'FN202'
    def matches(self, line: str):
        """"Checks if line is empty"""
        return len(line.rstrip()) == 0

class FN203(Filter):
    def name(self):
        return 'FN203'
    def matches(self, line: str):
        """Checks if line consists only from non-letter characters"""
        return len(line.strip()) > 0 and not re.search("[A-Za-z]", line.rstrip())

class Rules(Enum):
    FP001 = FP001()
    FP002 = FP002()
    FP003 = FP003()
    FN201 = FN201()
    FN202 = FN202()
    FN203 = FN203()
    
    @classmethod
    def rules_generator(cls):
        for item in cls:
            yield item.value

class Option(ABC):
    @abstractmethod
    def filter_file(self, file_lines: tuple):
        """Parent method, which is processing file content and returns tuple, containing information
        which is further used in 'filter' and 'annotate' classes inherited from Option class."""
        file_rules = {}
        count = 0
        for line in file_lines:
            count += 1
            str = ' '.join([rule.name() for rule in Rules.rules_generator() if rule.matches(line)])
            file_rules[f'{count}'] = str
        return file_rules
    
    @staticmethod
    def get_option(option: str):
        """
        Method receives argument from command line: 'filter' or 'annotate' and creates the instance
        of corresponding Class which will contains method with requested logic.
        """
        if option == 'filter':
            return FilterOption()
        if option == 'annotate':
            return AnnotateOption()
        raise Exception('Wrong arguments!')
        
class FilterOption(Option):
    def filter_file(self, file_lines: tuple):
        """
        Method calls for parent method which is processing text file content and contains additional
        logic specific for 'filter' scenario: the program should display lines in console based on given
        rules.
        """
        file_rules = super().filter_file(file_lines)
        for key in file_rules.keys():
            if 'FP' in file_rules[key]:
                print(f'{key}:{file_lines[int(key) - 1]}')

class AnnotateOption(Option):
    def filter_file(self, file_lines: tuple):
        """
        Method calls for parent method which is processing text file content and contains additional logic 
        specific for 'annotate' scenario: the program has to display the information about which rules are
        applicable for each line.
        """
        file_rules = super().filter_file(file_lines)
        for key in file_rules.keys():
            print(f'{key}: {file_rules[key]}')


if __name__ == '__main__':
    option = Option.get_option(sys.argv[1])
    file_path = sys.argv[2]
    content = open(file_path, 'r')
    file_lines = content.readlines()
    content.close()
    option.filter_file(file_lines)
                