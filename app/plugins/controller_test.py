import datetime
from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import PluginsService
from .schema import PluginSchema
from .model import Plugin

published_date1 = datetime.datetime.today()
published_date2 = datetime.datetime.today() - datetime.timedelta(4)


def make_plugin(
        plugin_id: str = "123",
        published: datetime.datetime = published_date1,
        title: str = "Test",
        score: str = 5,
        cve_list: [str] = None
) -> Plugin:
    return Plugin(plugin_id=plugin_id, published=published, title=title, score=score, cve_list=cve_list)


class TestPluginResource:
    @patch.object(
        PluginsService,
        "get_all",
        lambda a, b, c: [
            make_plugin("123", published_date1, "asdf", "5", ["cve1", "cve2"]),
            make_plugin("456", published_date2, "asdf", "5", ["cve1", "cve2"]),
        ],
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(
                "nessus/plugins", follow_redirects=True
            ).get_json()
            expected = (
                PluginSchema(many=True)
                    .dump(
                    [
                        make_plugin("123", published_date1, "asdf", "5", ["cve1", "cve2"]),
                        make_plugin("456", published_date2, "asdf", "5",
                                    ["cve1", "cve2"]),
                    ]
                )

            )
            for r in results:
                assert r in expected


class TestPluginIdResource:
    @patch.object(PluginsService, "get_by_id", lambda plugin_id: make_plugin(plugin_id=plugin_id))
    def test_get_by_id(self, client: FlaskClient):
        with client:
            result = client.get("/nessus/plugins/888").get_json()
            expected = Plugin(plugin_id="888")
            assert result["id"] == expected.id
