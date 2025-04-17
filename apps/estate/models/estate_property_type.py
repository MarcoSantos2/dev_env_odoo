from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'

    name = fields.Char(required=True)
    description = fields.Text()
    