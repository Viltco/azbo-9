


from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class MRPWizard(models.TransientModel):
    _name = 'mrp.wizard'

    quantity = fields.Float(string='Quantity')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    mo_id = fields.Many2one('mrp.bom', string='MO')

    def action_create_mo(self):
        line_val = []
        for line in self.mo_id.bom_line_ids:
            line_val.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'location_id': 2,
                'location_dest_id': 1,
                'product_uom_qty': line.product_qty,
                'product_uom': line.product_uom_id.id,
            }))
        record = self.env['mrp.production'].create({
            'date_planned_start': datetime.today(),
            'company_id': self.env.company.id,
            'user_id': self.env.user.id,
            'location_dest_id': 1,
            'product_uom_id': self.uom_id.id,
            'product_id': self.mo_id.product_tmpl_id.product_variant_id.id,
            'move_raw_ids': line_val,
        })