import io
import xlsxwriter
from odoo import http
from odoo.http import request
from datetime import datetime

class AssetAssignmentExcelExport(http.Controller):

    @http.route('/asset_assignment/export/excel', type='http', auth="user")
    def export_excel(self, **kwargs):
        assignments = request.env['asset.assignment'].search([])
        
        # Create Excel in-memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet("Assignments")

        # Formats
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#D9E1F2',
            'border': 2,
            'align': 'center',
            'valign': 'vcenter'
        })

        cell_format = workbook.add_format({
            'border': 1,
            'align': 'left',
            'valign': 'vcenter'
        })

        date_format = workbook.add_format({
            'border': 1,
            'num_format': 'yyyy-mm-dd',
            'align': 'center',
            'valign': 'vcenter'
        })

        # Set column widths
        sheet.set_column(0, 1, 25)  # Asset, Employee
        sheet.set_column(2, 4, 15)  # Dates
        sheet.set_column(5, 5, 20)  # Status

        # Freeze header row
        sheet.freeze_panes(1, 0)

        # Write headers
        headers = ['Asset', 'Employee', 'Assignment Date', 'Return Deadline', 'Return Date', 'Status']
        for col, header in enumerate(headers):
            sheet.write(0, col, header, header_format)

        # Write data
        for row_num, record in enumerate(assignments, start=1):
            sheet.write(row_num, 0, record.asset_id.name or '', cell_format)
            sheet.write(row_num, 1, record.employee_id.name or '', cell_format)

            # Date formatting with fallback
            assignment_date = record.assignment_date or ''
            return_deadline = record.return_deadline or ''
            return_date = record.return_date or ''

            sheet.write_datetime(row_num, 2, assignment_date, date_format) if assignment_date else sheet.write(row_num, 2, '', cell_format)
            sheet.write_datetime(row_num, 3, return_deadline, date_format) if return_deadline else sheet.write(row_num, 3, '', cell_format)
            sheet.write_datetime(row_num, 4, return_date, date_format) if return_date else sheet.write(row_num, 4, '', cell_format)

            sheet.write(row_num, 5, record.state or '', cell_format)

        workbook.close()
        output.seek(0)

        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename="asset_assignments.xlsx"')
            ]
        )
