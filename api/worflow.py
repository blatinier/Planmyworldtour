from flask import Blueprint

from models.workflow import Workflow


wf_bp = Blueprint('workflow', __name__, url_prefix='/workflow/')


@wf_bp.route("/")
def workflow():
    return Workflow.objects()
