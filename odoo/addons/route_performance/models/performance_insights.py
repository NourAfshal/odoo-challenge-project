from odoo import models, fields, api

class PerformanceInsights(models.Model):
    _name = 'performance.insights'
    _description = 'Sales Performance Insights'

    sales_rep_id = fields.Many2one('res.users', string='Sales Representative', required=True)
    completed_visits = fields.Integer(string='Completed Visits', compute='_compute_performance')
    restocks_initiated = fields.Integer(string='Restocks Initiated', compute='_compute_performance')
    products_sold = fields.Float(string='Products Sold', compute='_compute_performance')

    @api.depends('sales_rep_id')
    def _compute_performance(self):
        for record in self:
            # Dummy logic; replace with actual data fetching from related models
            visits = self.env['customer.visit'].search([('sales_rep_id', '=', record.sales_rep_id.id)])
            restocks = self.env['inventory.restock'].search([('sales_rep_id', '=', record.sales_rep_id.id)])
            sales = self.env['sale.order'].search([('user_id', '=', record.sales_rep_id.id)])
            
            record.completed_visits = len(visits)
            record.restocks_initiated = len(restocks)
            record.products_sold = sum(order.amount_total for order in sales)
