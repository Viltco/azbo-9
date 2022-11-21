from odoo import models, fields, api


class ConfigSettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    is_po_approval = fields.Boolean('QTY PO Approval')

    min_qty = fields.Float(string='Minimum Quantity',
                           config_parameter='azbo_overall.min_qty')

    max_qty = fields.Float(string='Maximum Quantity',
                           config_parameter='azbo_overall.max_qty')


