from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = 'price desc'

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string='Partner')
    property_id = fields.Many2one('estate.property', string='Property')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type', related='property_id.property_type_id', store=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', store=True)

    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'Price must be positive'),
    ]

    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Date.today() + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            offer.validity = (offer.date_deadline - fields.Date.today()).days

    def action_accept(self):
        self.ensure_one()
        if self.property_id.state == 'sold':
            raise UserError("Cannot accept an offer for a sold property.")
        if self.property_id.state == 'canceled':
            raise UserError("Cannot accept an offer for a canceled property.")
        
        self.status = 'accepted'
        
        self.property_id.write({
            'state': 'offer_accepted',
            'selling_price': self.price,
            'buyer_id': self.partner_id.id
        })
        
        # Refuse all other offers
        other_offers = self.property_id.offer_ids.filtered(lambda o: o.id != self.id)
        other_offers.write({'status': 'refused'})
        
        return True

    def action_refuse(self):
        self.ensure_one()
        self.status = 'refused'
        return True

    @api.model
    def create(self, vals):
        property_id = self.env['estate.property'].browse(vals['property_id'])
        
        # Check if the offer amount is higher than existing offers
        if property_id.offer_ids:
            max_offer = max(offer.price for offer in property_id.offer_ids)
            if vals['price'] <= max_offer:
                raise UserError(f"The offer must be higher than {max_offer}")
        
        # Set property state to 'offer_received'
        property_id.write({'state': 'offer_received'})
        
        return super().create(vals)
  
