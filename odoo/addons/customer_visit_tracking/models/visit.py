from odoo import models, fields, api
from datetime import datetime

class CustomerVisit(models.Model):
    _name = 'customer.visit'
    _description = 'Customer Visit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Visit Title', required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    sales_rep_id = fields.Many2one('res.users', string='Sales Representative', default=lambda self: self.env.user, required=True)
    scheduled_date = fields.Datetime(string='Scheduled Date', required=True)
    check_in_time = fields.Datetime(string='Check-In Time', readonly=True)
    visit_status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled', tracking=True)
    visit_objectives = fields.Text(string='Objectives')
    visit_report = fields.Text(string='Visit Report')
    feedback = fields.Text(string='Customer Feedback')
    inventory_levels = fields.Text(string='Inventory Levels')
    sales_discussions = fields.Text(string='Sales Discussions')

    @api.model
    def create(self, vals):
        record = super(CustomerVisit, self).create(vals)
        record.message_post(body="New customer visit scheduled.")
        return record

    def action_check_in(self):
        for visit in self:
            visit.check_in_time = datetime.now()
            visit.visit_status = 'in_progress'
            visit.message_post(body="Check-in recorded.")

    def action_complete_visit(self):
        for visit in self:
            visit.visit_status = 'completed'
            visit.message_post(body="Visit marked as completed.")
