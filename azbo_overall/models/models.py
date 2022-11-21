# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from re import findall as regex_findall
from re import split as regex_split
from dateutil import relativedelta
from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare, float_is_zero, float_repr, float_round
from odoo.tools.misc import format_date, OrderedSet
from odoo.exceptions import AccessError, UserError


class BOMInh(models.Model):
    _inherit = 'mrp.bom'

    is_sample_order = fields.Boolean('Sample Order')

    sale_count = fields.Integer(compute='get_sale_count')

    def button_create_sample(self):
        pass

    def button_create_sale(self):
        line_val = []
        for line in self.bom_line_ids:
            line_val.append((0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_qty,
                'product_uom': line.product_uom_id.id,
            }))
        record = self.env['sale.order'].create({
            'date_order': datetime.today(),
            'company_id': self.company_id.id,
            'bom_id': self.id,
            'partner_id': self.company_id.partner_id.id,
            'order_line': line_val,
        })

    def get_sale_count(self):
        for rec in self:
            count = self.env['sale.order'].search_count([('bom_id', '=', self.id)])
            rec.sale_count = count

    def action_sale_order_view(self):
        return {
            'name': _('Sale Order'),
            'domain': [('bom_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }


class SaleInh(models.Model):
    _inherit = 'sale.order'

    bom_id = fields.Many2one('mrp.bom', 'BOM Ref')

