from server.bo.Grading import Grading
from server.db.GradingMapper import GradingMapper


class Administration(object):
    def __init__(self):
        pass
    
    def create_grading(self, creation_date, grade):
        

        allgrades = self.get_all_grades()

        glist=[]

        for g in allgrades:
            glist.append(g.get_grade())

        if grade in glist:
            print('grade exists')
            return None
        else:
            g = Grading()
            g.set_date(creation_date)
            g.set_grade(grade)
            g.set_id(1)

            with GradingMapper() as mapper:
                return mapper.insert(g)



    def save_grading(self, grading):
        """Saves a  grading objects."""

        with GradingMapper() as mapper:
            mapper.update(grading)

    def delete_grading(self, grading):
        """Delets a grading object by ID."""

        with GradingMapper() as mapper:

            participations = self.get_all_by_grading_id(grading.get_id())

            if not(participations is None):
                for p in participations:
                    self.delete_grading_id(p)

            mapper.delete(grading)


    def get_all_grades(self):
        """Reads out  all grading objects."""

        with GradingMapper() as mapper:
            return mapper.find_all()

    def get_by_grading_id(self, id):
        """Reads out a grading object by ID."""

        with GradingMapper() as mapper:
            return mapper.find_by_id(id)