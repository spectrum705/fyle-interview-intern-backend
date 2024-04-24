from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_faculty_resources = Blueprint('principal_faculty_resources', __name__)


@principal_faculty_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of faculty"""
    principal_faculty = Teacher.get_all_teachers()
    principal_faculty_dump = TeacherSchema().dump(principal_faculty, many=True)
    return APIResponse.respond(data=principal_faculty_dump)