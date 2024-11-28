from odoo import models, fields, api

class SalesDashboard(models.Model):
    _name = 'sales.dashboard'
    _description = 'Sales Dashboard'

    sales_rep_id = fields.Many2one('res.users', string='Sales Representative')
    route_coverage = fields.Html(string='Route Coverage Overview', compute='_compute_route_coverage')
    visit_summary = fields.Html(string='Visit Summary', compute='_compute_visit_summary')
    inventory_status = fields.Html(string='Inventory Status', compute='_compute_inventory_status')

    @api.depends('sales_rep_id')
    def _compute_route_coverage(self):
        for record in self:
            # Generate route coverage overview (dummy example)
            record.route_coverage = """
                <ul>
                    <li>Route A: Completed</li>
                    <li>Route B: Pending</li>
                </ul>
            """

    @api.depends('sales_rep_id')
    def _compute_visit_summary(self):
        for record in self:
            # Generate visit summary (dummy example)
            record.visit_summary = """
                <table>
                    <tr><th>Customer</th><th>Outcome</th><th>Feedback</th></tr>
                    <tr><td>Customer A</td><td>Success</td><td>Positive</td></tr>
                    <tr><td>Customer B</td><td>Failed</td><td>Neutral</td></tr>
                </table>
            """

    @api.depends('sales_rep_id')
    def _compute_inventory_status(self):
        for record in self:
            # Generate inventory status (dummy example)
            record.inventory_status = """
                <table>
                    <tr><th>Product</th><th>Location</th><th>Stock</th><th>Status</th></tr>
                    <tr><td>Product A</td><td>Customer A</td><td>5</td><td>Low</td></tr>
                    <tr><td>Product B</td><td>Customer B</td><td>15</td><td>Good</td></tr>
                </table>
            """
