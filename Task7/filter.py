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
    def generator(cls):
        """"Generator which yields rules out of Rules class"""
        for item in cls:
            yield item.value

class Option(ABC):
    @abstractmethod
    def filter_file(self, lines: list):
        """This method will contain 'filter' or 'annotate' logic in inherited classes"""
        pass
    
    def _search_rules(self, lines: list):
        """
        Method receives list with file strings and returns dictionary, containing information:
        which rules are applicable for each line
        """
        relevant_rules = {}
        count = 0
        for line in lines:
            count += 1
            str = ' '.join([rule.name() for rule in Rules.generator() if rule.matches(line)])
            relevant_rules[f'{count}'] = str
        return relevant_rules

    @staticmethod
    def get_option(option: str):
        """
        Method receives argument from command line: 'filter' or 'annotate' and creates the instance
        of corresponding Class which further contains method with relevant logic.
        """
        if option == 'filter':
            return FilterOption()
        if option == 'annotate':
            return AnnotateOption()
        raise Exception('Wrong arguments!')
        
class FilterOption(Option):
    def filter_file(self, lines: list):
        """
        Method is realizing 'filter' scenario: display file lines in console based on given rules.
        Call for _search_rules method, with the list of file strings passed as argument, will generate 
        the dictionary of applicable rules and assign it to relevant_rules variable
        """
        relevant_rules = self._search_rules(lines)
        for key in relevant_rules.keys():
            if relevant_rules[key].count('FP') >= relevant_rules[key].count('FN'):
                print(f'{key}:{lines[int(key) - 1]}')

class AnnotateOption(Option):
    def filter_file(self, lines: list):
        """
        Method is realizing 'annotate' scenario: the program has to display the information about 
        which rules are applicable for each line.
        Call for _search_rules method, with the list of file strings passed as argument, will generate 
        the dictionary of applicable rules and assign it to relevant_rules variable
        """
        relevant_rules = self._search_rules(lines)
        for key in relevant_rules.keys():
            print(f'{key}: {relevant_rules[key]}')


if __name__ == '__main__':
    option = Option.get_option(sys.argv[1])
    file_path = sys.argv[2]
    content = open(file_path, 'r')
    lines = content.readlines()
    content.close()
    option.filter_file(lines)
                