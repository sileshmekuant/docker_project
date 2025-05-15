import io
import xlsxwriter
from odoo import http
from odoo.http import request

class EstatePropertyExcelExport(http.Controller):

    @http.route('/estate_property/export/excel', type='http', auth="user")
    def export_excel(self, **kwargs):
        properties = request.env['estate.property'].search([])

        # Create Excel in-memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet("Properties")

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

        datetime_format = workbook.add_format({
            'border': 1,
            'num_format': 'yyyy-mm-dd hh:mm',
            'align': 'center',
            'valign': 'vcenter'
        })

        # Set column widths
        sheet.set_column(0, 10, 20)

        # Freeze header row
        sheet.freeze_panes(1, 0)

        # Write headers
        headers = [
            'Property Name', 'Country', 'Region', 'City', 'Sub City',
            'Listed Date', 'Available From', 'Sale Deadline', 
            'Price/sq.m', 'Area (sq.m)', 'Total Price',
            'Parking', 'Year Built', 'Sold', 'Grand Total'
        ]
        for col, header in enumerate(headers):
            sheet.write(0, col, header, header_format)

        # Write data
        for row_num, record in enumerate(properties, start=1):
            sheet.write(row_num, 0, record.name or '', cell_format)
            sheet.write(row_num, 1, record.country_id.name or '', cell_format)
            sheet.write(row_num, 2, record.region_id.name or '', cell_format)
            sheet.write(row_num, 3, record.city.name or '', cell_format)
            sheet.write(row_num, 4, record.sub_city_id.name or '', cell_format)

            sheet.write_datetime(row_num, 5, record.listed_date, date_format) if record.listed_date else sheet.write(row_num, 5, '', cell_format)
            sheet.write_datetime(row_num, 6, record.available_from, datetime_format) if record.available_from else sheet.write(row_num, 6, '', cell_format)
            sheet.write_datetime(row_num, 7, record.sale_deadline, datetime_format) if record.sale_deadline else sheet.write(row_num, 7, '', cell_format)

            sheet.write(row_num, 8, record.price_per_sq_m or 0.0, cell_format)
            sheet.write(row_num, 9, record.area or 0.0, cell_format)
            sheet.write(row_num, 10, record.price or 0.0, cell_format)

            sheet.write(row_num, 11, 'Yes' if record.parking_space else 'No', cell_format)
            sheet.write_datetime(row_num, 12, record.year_built, datetime_format) if record.year_built else sheet.write(row_num, 12, '', cell_format)
            sheet.write(row_num, 13, 'Yes' if record.sold else 'No', cell_format)
            sheet.write(row_num, 14, record.grand_total or 0.0, cell_format)

        workbook.close()
        output.seek(0)

        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename="estate_properties.xlsx"')
            ]
        )
