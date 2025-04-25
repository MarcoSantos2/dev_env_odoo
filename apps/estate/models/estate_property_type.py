from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'name'

    name = fields.Char(required=True)
    description = fields.Text()
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    sequence = fields.Integer(default=1)

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Name must be unique'),
    ]
