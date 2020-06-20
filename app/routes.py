from .plugins.controller import api as plugins_api


def register_routes(api, app, root="nessus"):
    api.add_namespace(plugins_api, path=f"/{root}/plugins")
