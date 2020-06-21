from .service import PluginsService
from app.test.fixtures import app  # noqa
import dateutil.parser


class TestPluginService:

    def test_get_all_sort_by_plugin_id(self, app):
        with app.app_context():
            results = PluginsService.get_all("pluginID")
            for idx, result in enumerate(results):
                if idx > 0:
                    assert result.id <= results[idx - 1].id

    def test_get_all_sort_by_published(self, app):
        with app.app_context():
            results = PluginsService.get_all("published")
            for idx, result in enumerate(results):
                if idx > 0:
                    assert dateutil.parser.parse(result.published) <= dateutil.parser.parse(results[idx - 1].published)

    def test_get_all_sort_by_score(self, app):
        with app.app_context():
            results = PluginsService.get_all("score")
            for idx, result in enumerate(results):
                if idx > 0:
                    assert result.score <= results[idx - 1].score
