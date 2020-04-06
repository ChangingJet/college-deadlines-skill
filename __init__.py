from mycroft import MycroftSkill, intent_file_handler


class CollegeDeadlines(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('deadlines.college.intent')
    def handle_deadlines_college(self, message):
        self.speak_dialog('deadlines.college')


def create_skill():
    return CollegeDeadlines()

