# -*- coding:utf-8 -*-
from flask import Blueprint

from libs.external_api import ExternalApi

bp = Blueprint('service_api', __name__, url_prefix='/v1')
api = ExternalApi(bp)


from .app import completion, app, conversation, message, audio, file

from .dataset import document, segment, dataset
from .service_api.plugins.external_api_plugin import ExternalAPIPlugin
from .service_api.ui.external_api_plugin_config import ui_bp
bp.register_blueprint(ui_bp)
