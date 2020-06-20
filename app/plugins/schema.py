from marshmallow import fields, Schema


class PluginSchema(Schema):
    id = fields.String(attribute="id")
    published = fields.String(attribute="published")
    title = fields.String(attribute="title")
    score = fields.String(attribute="score")
    cveList = fields.String(attribute="cve_list")
