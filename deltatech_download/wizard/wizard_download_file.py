# ©  2008-2018 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import _, api, fields, models


class WizardDownloadFile(models.TransientModel):
    _name = "wizard.download.file"

    file_name = fields.Char(string="File Name")
    data_file = fields.Binary(string="File")

    @api.multi
    def do_download_file(self):
        return {
            "type": "ir.actions.act_url",
            "url": "/web/content?model=%s&download=True&field=data_file&id=%s&filename=%s"
            % (self._name, self.id, self.file_name),
            "target": "new",
        }
