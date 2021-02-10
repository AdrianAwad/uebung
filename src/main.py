from flask import Flask
from flask_restx import Api, Resource, fields, resource
from flask_cors import CORS

from server.Administration import Administration
from server.bo.Grading import Grading





app = Flask(__name__)

CORS(app, support_credentials = True, resources = {r'/test/*': {"origins": "*"}})

api = Api(app, version='1.0', title='Test',
            description='a test system for joy')

test = api.namespace('test', 'test description is useless')


bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique id of a business object'),
    'creation_date': fields.String(attribute='_creation_date', description='creation date of a business object')
})

grading = api.inherit('Grading', bo, {
    'grade': fields.Float (attribute='_grade', descritpion='Grade for evaluation'),
})




@test.route('/grading')
@test.response(500, 'server error')
class GradingListOperations(Resource):
    @test.marshal_list_with(grading)
    def get(self):
        """reading out all grading objects. If no grading objects are available, an empty sequence is returned."""           
        adm = Administration()
        grades = adm.get_all_grades()
        return grades

    @test.marshal_with(grading, code=200)
    @test.expect(grading)
    def post(self):
        """Create a new grading object. It is up to the election administration (business logic) to have a correct ID
        to forgive. The corrected object will eventually be returned. """
        adm = Administration()

        proposal = Grading.from_dict(api.payload)

        if proposal is not None:
            """We only use the attributes of grading of the proposal for generation
            of a grading object. The object created by the server is authoritative and
            is also returned to the client."""
            g = adm.create_grading(proposal.get_date(), proposal.get_grade())
            return g, 200
        else:
            #server error
            return '', 500

@test.route('/grading/<int:id>')
@test.response(500, 'server error')
class GradingOperations(Resource):
    @test.marshal_with(grading)
    def get(self, id):
        """reading out a specific grading object.
        The object to be read is determined by the '' id '' in the URI."""      
        adm = Administration()
        g = adm.get_by_grading_id(id)
        return g

    @test.marshal_with(grading)
    @test.expect(grading, validate=True)
    def put(self, id):
        """ Update of a specific gradingn object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        grading object."""
        adm = Administration()
        g = Grading.from_dict(api.payload)

        if g is not None:
            """This sets the id of the grading object to be overwritten""" 
            g.set_id(id)
            adm.save_grading(g)
            return '', 200
        else: 
            return '', 500

    def delete(self, id):
        """Deleting a specific grading object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        g = adm.get_by_grading_id(id)
        adm.delete_grading(g)
        return '', 200
    



if __name__ == '__main__':
    app.run()