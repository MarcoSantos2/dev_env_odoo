# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    """Real Estate Property model for managing properties and listings."""
    _name = 'estate.property'
    _description = 'Real Estate Property'
    _order = 'id desc'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=lambda self: fields.Date.today() + relativedelta(months=3),
        copy=False
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', required=True, copy=False)
    property_type_id = fields.Many2one(
        'estate.property.type',
        string='Property Type'
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    seller_id = fields.Many2one(
        'res.users',
        string='Salesman',
        default=lambda self: self.env.user
    )
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many(
        'estate.property.offer',
        'property_id',
        string='Offers'
    )
    total_area = fields.Float(compute='_compute_total_area', store=True)
    best_offer = fields.Float(compute='_compute_best_price', store=True)

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'Expected price must be positive'),
        ('check_selling_price', 'CHECK(selling_price > 0)',
         'Selling price must be positive'),
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        """Compute the total area by adding living area and garden area."""
        for property_rec in self:
            property_rec.total_area = (
                property_rec.living_area + property_rec.garden_area
            )

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        """Compute the best offer price among all offers for a property."""
        for property_rec in self:
            if property_rec.offer_ids:
                property_rec.best_offer = max(
                    offer.price for offer in property_rec.offer_ids
                )
            else:
                property_rec.best_offer = 0

    @api.onchange('garden')
    def _onchange_garden(self):
        """Set default garden area and orientation when garden is enabled."""
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = None

    def action_sold(self):
        """Mark the property as sold if not canceled."""
        for prop in self:
            if prop.state == 'canceled':
                raise UserError(_("Canceled properties cannot be sold."))
            prop.state = 'sold'
        return True

    def action_cancel(self):
        """Mark the property as canceled if not sold."""
        for prop in self:
            if prop.state == 'sold':
                raise UserError(_("Sold properties cannot be canceled."))
            prop.state = 'canceled'
        return True

    @api.constrains('selling_price', 'expected_price')
    def _check_price_difference(self):
        """
        Validate that the selling price is at least 90% of the expected price.
        """
        for prop in self:
            if not float_is_zero(prop.selling_price, precision_digits=2):
                min_price = prop.expected_price * 0.9
                if float_compare(
                    prop.selling_price, min_price, precision_digits=2
                ) < 0:
                    raise ValidationError(_(
                        "Selling price cannot be lower than 90% of the "
                        "expected price! Minimum allowed: %(min_price).2f"
                    ) % {'min_price': min_price})

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_canceled(self):
        """Only allow deletion of properties in 'new' or 'canceled' states."""
        for prop in self:
            if prop.state not in ['new', 'canceled']:
                raise UserError(
                    _("Only new or canceled properties can be deleted.")
                )
