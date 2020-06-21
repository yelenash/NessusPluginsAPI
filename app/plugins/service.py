from typing import List
from .model import Plugin
from flask import current_app
from elasticsearch_dsl import Search

PLUGINS_INDEX = "nessus"


class PluginsService:
    @staticmethod
    def get_all(sort_by=None, start=0, limit=10) -> List[Plugin]:
        search = Search(using=current_app.elasticsearch, index=PLUGINS_INDEX)[start:limit]
        if sort_by:
            if sort_by == "score":
                search = search.sort({f"cvss.{sort_by}": {"order": "desc"}})
            else:
                search = search.sort({f"{sort_by}": {"order": "desc"}})
        response = search.execute()
        response = [PluginsService._parse_single_result(result) for result in response.hits]
        return response

    @staticmethod
    def get_by_id(plugin_id: int) -> Plugin:
        search = Search(using=current_app.elasticsearch, index=PLUGINS_INDEX) \
            .query("match", pluginID=plugin_id)
        response = search.execute()
        # TODO: somthing like firstOfDefault()
        for hit in response:
            return PluginsService._parse_single_result(hit)

    @staticmethod
    def get_by_cve(cve_id: int) -> List[Plugin]:
        search = Search(using=current_app.elasticsearch, index=PLUGINS_INDEX) \
            .query("term", cvelist__keyword=cve_id)
        response = search.execute()
        response = [PluginsService._parse_single_result(result) for result in response.hits]
        return response

    @staticmethod
    def _parse_single_result(result):
        return Plugin(result.pluginID, result.published, result.title, result.cvss.score, result.cvelist)
