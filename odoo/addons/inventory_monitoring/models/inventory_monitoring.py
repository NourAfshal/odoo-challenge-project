from odoo import models, fields, api

class CustomerInventory(models.Model):
    _name = 'customer.inventory'
    _description = 'Customer Inventory Monitoring'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Inventory Record', required=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=True)
    current_stock = fields.Float(string='Current Stock', required=True, tracking=True)
    restock_threshold = fields.Float(string='Restock Threshold', required=True, tracking=True)
    sales_rep_id = fields.Many2one('res.users', string='Sales Representative', default=lambda self: self.env.user, required=True)
    last_update_date = fields.Datetime(string='Last Updated', default=fields.Datetime.now, readonly=True)

    stock_alert = fields.Boolean(string='Stock Alert', compute='_compute_stock_alert', store=True)
    total_sales = fields.Float(string='Total Sales', compute='_compute_sales_metrics', store=True)
    turnover_rate = fields.Float(string='Inventory Turnover Rate', compute='_compute_sales_metrics', store=True)

    @api.depends('current_stock', 'restock_threshold')
    def _compute_stock_alert(self):
        for record in self:
            record.stock_alert = record.current_stock < record.restock_threshold

    @api.depends('product_id', 'customer_id')
    def _compute_sales_metrics(self):
        for record in self:
            # Dummy computations, replace with real sales data integration.
            record.total_sales = 100.0  # Placeholder: Fetch total sales for the product at this customer.
            record.turnover_rate = record.total_sales / max(record.current_stock, 1)

    @api.model
    def create(self, vals):
        record = super(CustomerInventory, self).create(vals)
        if record.stock_alert:
            record._send_stock_alert()
        return record

    def write(self, vals):
        result = super(CustomerInventory, self).write(vals)
        if 'current_stock' in vals:
            for record in self:
                if record.stock_alert:
                    record._send_stock_alert()
        return result

    def _send_stock_alert(self):
        for record in self:
            message = f"Stock Alert: The stock of {record.product_id.name} at {record.customer_id.name} is below the threshold."
            record.message_post(body=message, subtype_xmlid="mail.mt_comment")
            # Notify managers and sales reps
            managers = self.env.ref('base.group_system').users
            recipients = managers | record.sales_rep_id
            for user in recipients:
                self.env['mail.activity'].create({
                    'res_model_id': self.env['ir.model']._get('customer.inventory').id,
                    'res_id': record.id,
                    'user_id': user.id,
                    'summary': 'Stock Alert',
                    'note': message,
                    'activity_type_id': self.env.ref('mail.mail_activity_data_warning').id,
                })
