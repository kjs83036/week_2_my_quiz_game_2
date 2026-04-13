class Quiz:

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def __getitem__(self, key):
        return getattr(self, key)
 
    def __setitem__(self, key, value):
        setattr(self, key, value)