import functools, operator

class Task():
    def __init__(self, triplet: tuple):
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
    def __init__(self, task_instance_list: list):
        self.project_estimate = round(self.total_project_estimate(task_instance_list), 2)
        self.project_error = round(self.calculate_standard_error(task_instance_list), 2)
    
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


def collect_project_data():
    """This function collects the (a, m, b) data for all project's tasks from user input"""
    task_list = []
    task_length = int(input("Enter total number of available project tasks: "))
    for i in range(task_length):
        task_list.append([])
        task_list[i].append(int(input(f"Enter the best-case estimate 'A' for the Task #{i+1}: ")))
        task_list[i].append(int(input(f"Enter the most-likely estimate 'M' for the Task #{i+1}: ")))
        task_list[i].append(int(input(f"Enter the worst-case estimate 'B' for the Task #{i+1}: ")))
    return task_list

def create_task_instances(task_list: list):
    """This function generates and returns the list of Task class instances"""
    task_instance_list = []
    for i in range(len(task_list)):
        task_instance_list.append(Task(task_list[i]))
    return task_instance_list

def main():
    collected_project_data = collect_project_data()
    task_class_objects = create_task_instances(collected_project_data)
    project = Project(task_class_objects)
    project.confidence_interval_info(project.confidence_interval_95())


if (__name__=='__main__'):
    main()
    