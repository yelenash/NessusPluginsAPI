from datetime import datetime


class Plugin:
    def __init__(self,
                 plugin_id: str,
                 published: datetime.date = datetime.today(),
                 title: str = None,
                 score: str = None,
                 cve_list: [str] = None
                 ):
        self.id = plugin_id
        self.published = published
        self.title = title
        self.score = score
        self.cve_list = cve_list
