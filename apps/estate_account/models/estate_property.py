# -*- coding: utf-8 -*-
from odoo import models, Command, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class EstateProperty(models.Model):
    """Estate property extension for invoice generation on sale."""
    _inherit = 'estate.property'

    def action_sold(self):
        """Create an invoice when a property is sold and mark it as sold.

        Creates an invoice with two lines:
        - 6% of the selling price
        - A fixed administrative fee of 100.00
        """
        self.ensure_one()
        _logger.info(
            "Creating invoice for property %s (ID: %s)",
            self.name, self.id
        )

        if not self.buyer_id:
            raise UserError(_(
                "Cannot create invoice: no buyer set on the property."
            ))

        # Create an invoice with two lines
        invoice_vals = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': _('6%% of selling price'),
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                }),
                Command.create({
                    'name': _('Administrative fees'),
                    'quantity': 1,
                    'price_unit': 100.00,
                }),
            ],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        _logger.info("Created invoice with ID: %s", invoice.id)

        return super().action_sold()
