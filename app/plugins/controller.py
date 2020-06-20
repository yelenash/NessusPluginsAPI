from flask import request
from flask_accepts import responds
from flask_restx import Namespace, Resource
from typing import List

from .schema import PluginSchema
from .service import PluginsService
from .model import Plugin

api = Namespace("Plugins", description="Nessus plugins")  # noqa


@api.route("/")
@api.doc(params={"cve": {"description": "cve id on which plugins affect"},
                 "orderBy": {"description": "pluginID/published/score (descending)"},
                 "start": {"description": "start page", "default": 0},
                 "limit": {"description": "page size", "default": 10}
                 })
class PluginResource(Resource):
    @responds(schema=PluginSchema(many=True))
    def get(self) -> List[Plugin]:
        cve_id = request.args.get('cve')
        order_by = request.args.get('orderBy')
        start = int(request.args.get('start') or "0")
        limit = int(request.args.get('limit') or "10")
        if cve_id:
            return PluginsService.get_by_cve(cve_id)
        return PluginsService.get_all(order_by, start, limit)


@api.route("/<int:pluginID>")
@api.doc(params={"pluginID": "Nessus plugin id"})
class PluginIdResource(Resource):
    @responds(schema=PluginSchema)
    def get(self, pluginID: int) -> Plugin:
        return PluginsService.get_by_id(pluginID)
