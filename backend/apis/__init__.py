from flask import Blueprint
from flask_restplus import Api

from .create_database import api as create_database
from .analyze import api as analyze
from .downloadLineagesInfo import api as downloadLineagesInfo
from .private import api as private
from .ufl import api as ufl

enable_doc = True

api_blueprint = Blueprint('api', __name__)

if enable_doc:
    api = Api(title='UFL API', version='1.0', description='TODO', )
else:
    api = Api(title='UFL API', version='1.0', description='TODO', doc=False)


api.init_app(api_blueprint, add_specs=enable_doc)

api.add_namespace(create_database)
api.add_namespace(ufl)
api.add_namespace(private)
api.add_namespace(analyze)
api.add_namespace(downloadLineagesInfo)
