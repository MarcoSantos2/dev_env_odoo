from odoo import models, Command
import logging
_logger = logging.getLogger(__name__)


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        _logger.warning("Overridden action_sold method called!")
        # Create an empty customer invoice (account.move) with two lines
        invoice_vals = {
            'partner_id': self.buyer_id.id,  # assuming buyer_id is set
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': '6% of selling price',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                }),
                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1,
                    'price_unit': 100.00,
                }),
            ],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        _logger.warning(f"Created invoice with ID: {invoice.id}")
        return super().action_sold()
