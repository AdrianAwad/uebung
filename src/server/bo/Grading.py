from server.bo import BusinessObject as bo

class Grading(bo.BusinessObject):
    """The implementation of a exemplary grading class.
    """
    def __init__(self):
        super().__init__()
        self._grade = 0.0

    def get_grade(self):
        """Reads out the grading"""
        return self._grade

    def set_grade(self, grade):
        """Sets the grading"""
        self._grade = grade


    @staticmethod
    def from_dict(dicti=dict()):

        """"Converts a Python dict() into a Grading()."""
        grading = Grading()
        grading.set_grade(dicti["grade"])
        return grading


