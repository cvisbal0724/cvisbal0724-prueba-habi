from flask import Blueprint
from models.property import PropertyModel as model
from flask import jsonify
from utilities.structure import Structure
from flask import request

routeProperty = Blueprint('property', __name__)

@routeProperty.route('/')
def get_properties():
    try:
        year = request.args.get('year', None)
        city = request.args.get('city', None)
        status = request.args.get('status', None)
        response = model.get_properties(year, city, status);
        result = Structure.success('', response)
        return jsonify(result)
    except Exception as e:
        return Structure.error(e.message)
       
        