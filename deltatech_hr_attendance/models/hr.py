# coding=utf-8



from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import ValidationError

class Department(models.Model):
    _inherit = "hr.department"

    type = fields.Selection([('div', 'Division'),('dep','Department'),('for','Formation')])


class Holidays(models.Model):
    _inherit = "hr.holidays"


    @api.model
    def default_get(self, fields_list):
        default = super(Holidays, self).default_get(fields_list)

        if 'default_date' in self.env.context:
            default['date_from'] = self.env.context['default_date']
            default['date_to'] = self.env.context['default_date']

        return default


    @api.constrains('date_from', 'date_to')
    def _check_date(self):
        for holiday in self:
            domain = [
                ('date_from', '<=', holiday.date_to),
                ('date_to', '>=', holiday.date_from),
                ('employee_id', '=', holiday.employee_id.id),
                ('id', '!=', holiday.id),
                ('holiday_status_id', '=', holiday.holiday_status_id.id),
                ('state', 'not in', ['cancel', 'refuse']),
            ]
            nholidays = self.search_count(domain)
            if nholidays:
                raise ValidationError(_('You can not have 2 leaves that overlaps on same day!'))