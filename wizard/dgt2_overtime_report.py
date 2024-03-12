from odoo import models, fields
from xlwt import Workbook, easyxf
import base64


class OvertimeReportWizard(models.TransientModel):
    _name = 'overtime.report.wizard'
    _description = 'DGT-2 Overtime Report Wizard'

    company_id = fields.Many2one('res.company',
                                 'Compañía',
                                 default=lambda self: self.env.company.id,
                                 required=True, readonly=True)

    payslip_run_ids = fields.Many2many('hr.payslip.run',
                                       string="Lotes incluidos", domain="[('company_id', '=?', company_id)]")

    def generate_report(self):
        slip_ids = self.env['hr.payslip'].search(
            [('payslip_run_id', 'in', self.payslip_run_ids.ids), ('company_id', '=?', self.company_id.id)])
        print(slip_ids)
