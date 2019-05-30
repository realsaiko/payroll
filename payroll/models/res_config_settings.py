# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_account_accountant = fields.Boolean(string='Account Accountant')
    module_l10n_fr_payroll = fields.Boolean(string='French Payroll')
    module_l10n_be_payroll = fields.Boolean(string='Belgium Payroll')
    module_l10n_in_payroll = fields.Boolean(string='Indian Payroll')