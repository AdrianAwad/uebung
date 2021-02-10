import mysql.connector
from server.bo.Grading import Grading
from server.db.Mapper import Mapper


class GradingMapper (Mapper):
    """This is a mapper-class, which represents grading objects into
    a relational database. For this reason you can find some methods,
    which help to find, insert, modify, and delete objects. The mapping is 
    bidirectional, which means objects can be transformed into database structures
    and the other way around"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Reads out all gradings.
        :return A collection of grading objects that repesent all gradings.
        """

        result = []
        cursor = self._connection.cursor()

        cursor.execute("SELECT id, creation_date, grade FROM Grading ORDER BY grade")
        tuples = cursor.fetchall()

        for (id, creation_date, grade) in tuples:
            grading = Grading()
            grading.set_id(id)
            grading.set_date(creation_date)
            grading.set_grade(grade)
            result.append(grading)

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Reads out one grading by id.
        :param id Unique id of the grading
        :return A grading object, which has the required id.
        """

        result = None
        cursor = self._connection.cursor()

        command = "SELECT id, creation_date, grade FROM Grading WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creation_date, grade) in tuples:
            grading = Grading()
            grading.set_id(id)
            grading.set_date(creation_date)
            grading.set_grade(grade)
            result = grading

        self._connection.commit()
        cursor.close()
        return result


    def insert(self, grading):
        """Adds a grading object into the database.
        The primary key of the object gets checked and if neccessary adjusted.
        :param grading object which will be saved
        :return grading object with the changed id
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM Grading")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                grading.set_id(maxid[0] + 1)
            else:
                grading.set_id(1)
            
        command = "INSERT INTO Grading (id, creation_date, grade) VALUES (%s,%s,%s)"
        data = (grading.get_id(), grading.get_date(), grading.get_grade())
        cursor.execute(command, data)
        self._connection.commit()
        cursor.close()
        

        return grading

    def update(self, grading):
        """Updates a grading object in the database.
        :param grading object which will be updated
        """

        cursor = self._connection.cursor()

        command = "UPDATE Grading " + "SET grade=%s WHERE id=%s"
        data = (grading.get_grade(), grading.get_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, grading):
        """Deletes a grading object from the database.
        :param grading object which will be deleted
        """

        cursor = self._connection.cursor()
        command = "DELETE FROM Grading WHERE id={}".format(grading.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



