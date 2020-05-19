"""
This module asks for file path and outputs some statistics for z symbol and "and" word
"""
def read_file(file_name: str):
   reader = open(file_name,'r')
   file_content = reader.readlines()
   reader.close()
   return file_content

def statistics(file_content: tuple):
    statistics = {}
    count_z = 0
    count_lines_with_and = 0
    statistics['total lines'] = len(file_content)
    statistics['empty lines'] = file_content.count('\n')
    
    for _ in file_content:
        if (_.find('z')) != -1:
            count_z = count_z + 1
        if (_.find('and')) != -1:
            count_lines_with_and = count_lines_with_and + 1
    
    statistics['lines with "z"'] = count_z
    statistics['"z" count'] = len(re.findall("z", "".join(file_content)))
    statistics['lines with "and"'] = count_lines_with_and
    return statistics
def print_file_info(statistics: dict):
    for k, v in statistics.items():
        print(f'{k}: {v}')

def main():
    while True:
       tuply = read_file(str(input('Please enter file path:')))
       print_file_info(statistics(tuply))
       if (input("would you like to analyze another file (Yes/No)?:")) == 'Yes':
           continue
       else:
           break
       

if (__name__=='__main__'):
    import re
    main()
