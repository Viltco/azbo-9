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


class CRMLeadInh(models.Model):
    _inherit = 'crm.lead'

    def action_order_cost_sheet(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bill of Material',
            'view_id': self.env.ref('mrp.mrp_bom_form_view', False).id,
            'target': 'current',
            'res_model': 'mrp.bom',
            'view_mode': 'form',
        }