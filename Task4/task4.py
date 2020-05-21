"""This module realizes the three-point estimation technique used in project management"""
import functools, operator

class Task():
    """
    This class has 5 properties that are: Task a,m,b, E and SD.
    E and SD properties are initialized with the help of Task methods 'estimate' and
    'standard_deviation' correspondingly.
    """
    def __init__(self, triplet: list):
        self.a_best = triplet[0]
        self.m_most_likely = triplet[1]
        self.b_worst = triplet[2]
        self.task_estimate = round(self.estimate(), 2)
        self.task_deviation = round(self.standard_deviation(), 2)
        
    def estimate(self):
        """This method calculates the estimate E for the given task."""
        return (self.a_best + 4 * self.m_most_likely + self.b_worst) / 6
    
    def standard_deviation(self):
        """This method calculates the standard deviation SD for the given task."""
        return (self.b_worst - self.a_best) / 6

class Project():
    """
    This class has 2 properties that are: estimate and standard error for entire project.
    They are initialized with the help of Project methods 'total_project_estimate'
    and 'calculate_standard_error' correspondingly.
    Static method 'collect_project_data' collects project data consisting of several tasks from
    user console input and returns the list of data where each element is representing a separate task
    and in its own turn is a list of 3 elements: (a,m,b).
    Static method 'create_task_instances' creates a list of n instances of class Task depending of number
    of tasks: n. We use this list of instances in other methods to initialize Project properties and calculate
    other project metrics.
    """
    def __init__(self, task_instance_list: list):
        self.project_estimate = round(self.total_project_estimate(task_instance_list), 2)
        self.project_error = round(self.calculate_standard_error(task_instance_list), 2)
    
    @staticmethod
    def collect_project_data(num: int):
        """This function collects the (a, m, b) data for all project's tasks from user input"""
        task_list = []
        for i in range(num):
            task_list.append([])
            task_list[i].append(float(input(f"Enter the best-case estimate 'A' for the Task #{i+1}: ")))
            task_list[i].append(float(input(f"Enter the most-likely estimate 'M' for the Task #{i+1}: ")))
            task_list[i].append(float(input(f"Enter the worst-case estimate 'B' for the Task #{i+1}: ")))
        return task_list
    
    @staticmethod
    def create_task_instances(task_list: list):
        """This function generates and returns the list of Task class instances"""
        task_instance_list = []
        for i in range(len(task_list)):
            task_instance_list.append(Task(task_list[i]))
        return task_instance_list
    
    def total_project_estimate(self, task_instance_list: list):
        """This method calculates the total estimate E for the entire project."""
        return functools.reduce(operator.add,[task_instance_list[i].task_estimate for i in range(len(task_instance_list))])
    
    def calculate_standard_error(self, task_instance_list: list):
        """This method calculates the standard error SE for the entire project."""
        return pow(functools.reduce(operator.add,[pow(task_instance_list[i].task_deviation, 2) for i in range(len(task_instance_list))]), 0.5)
    
    def confidence_interval_95(self):
        """This method calculates the 95% confidence interval for the project and returns the tuple with 2 min/max values"""
        return (round(self.project_estimate - 2 * self.project_error), round(self.project_estimate + 2 * self.project_error))

    def confidence_interval_info(self, interval:tuple):
        """This method outputs the project's confidence interval to console"""
        print(f"Project's 95% confidence interval: {interval[0]} ... {interval[1]} points")
    

def main():
    flag = True
    while flag:
        task_length = int(input("Enter total number of available project tasks: "))
        if task_length == 0:
            print("Number of tasks cannot be 0, please try again")
        elif task_length < 0:
            print("Number of tasks cannot be negative, please try again")
        else:
            flag = False

    collected_project_data = Project.collect_project_data(task_length)
    task_class_objects = Project.create_task_instances(collected_project_data)
    project = Project(task_class_objects)
    project.confidence_interval_info(project.confidence_interval_95())
    task5 = Task((1,2,3))
    print(task5.task_estimate)


if (__name__=='__main__'):
    main()
    