
class User:
    def __init__(self):
        """
        Constructor calls for static method get_user_name to initialize user's full name
        and creates user_specific_file names for time reports and answers with
        the help of create_timer_file_name and create_answers_file_name methods.
        """
        self.user_name = self.get_user_name()
        self.timer_file_name = self.create_timer_file_name(self.user_name)
        self.answers_file_name = self.create_answers_file_name(self.user_name)
        self.quiz_answers = {}
    
    @staticmethod
    def get_user_name():
        """
        Function receives user name and surname from console and performs
        some basic validation. It returns the dict where user name and surname are stored under
        'user_name' and 'user_last_name' keys.
        """
        flag_first_name = True
        flag_last_name = True
        while flag_first_name:
            user_first_name = input("Please enter your first name: ")
            if user_first_name:
                flag_first_name = False
            else: print("User's first name can't be empty..")
        while flag_last_name:
            user_last_name = input("Please enter your last name: ")
            if user_last_name:
                flag_last_name = False
            else: print("User's last name can't be empty..")
        user_name = {'user_name': user_first_name, 'user_last_name': user_last_name}
        return user_name

    def create_timer_file_name(self, user_name: dict):
        """Based on user's name the function creates specific file name for time report file"""
        timer_file_name = user_name['user_name'] + '_' + user_name['user_last_name'] + '_timer.txt'
        return timer_file_name

    def create_answers_file_name(self, user_name: dict):
        """Based on user's name the function creates specific file name for user's quiz answers"""
        answers_file_name = user_name['user_name'] + '_' + user_name['user_last_name'] + '_answers.txt'
        return answers_file_name