


from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class MRPWizard(models.TransientModel):
    _name = 'mrp.wizard'

    quantity = fields.Float(string='Quantity')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    bom_id = fields.Many2one('mrp.bom', string='BOM')

    def action_create_mo(self):
        line_val = []
        for line in self.bom_id.bom_line_ids:
            line_val.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'location_id': self.bom_id.picking_type_id.default_location_src_id.id,
                'location_dest_id': 105,
                'product_uom_qty': line.product_qty * self.quantity,
                'product_uom': line.product_uom_id.id,
            }))
        record = self.env['mrp.production'].create({
            'date_planned_start': datetime.today(),
            'company_id': self.env.company.id,
            'user_id': self.env.user.id,
            'location_src_id': self.bom_id.picking_type_id.default_location_src_id.id,
            'location_dest_id': self.bom_id.picking_type_id.default_location_dest_id.id,
            'product_uom_id': self.uom_id.id,
            'bom_id': self.bom_id.id,
            'product_id': self.bom_id.product_tmpl_id.product_variant_id.id,
            'product_qty': self.quantity,
            'move_raw_ids': line_val,
            'state': 'to_close',
        })
        record.action_confirm()