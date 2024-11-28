from odoo import models, fields, api
from geopy.distance import geodesic

class RouteOptimization(models.Model):
    _name = 'route.optimization'
    _description = 'Route Optimization'

    sales_rep_id = fields.Many2one('res.users', string='Sales Representative', required=True)
    route_plan = fields.Html(string='Optimized Route', compute='_compute_route_plan')
    customer_ids = fields.Many2many('res.partner', string='Customers to Visit')

    @api.depends('customer_ids', 'sales_rep_id')
    def _compute_route_plan(self):
        for record in self:
            if record.customer_ids:
                # Dummy base location; replace with sales rep's actual location
                sales_rep_location = (33.888630, 35.495480)  # Beirut, Lebanon

                customers = [
                    (customer.name, customer.partner_latitude, customer.partner_longitude)
                    for customer in record.customer_ids
                    if customer.partner_latitude and customer.partner_longitude
                ]
                
                # Sort by distance from the sales rep's location
                sorted_customers = sorted(
                    customers,
                    key=lambda cust: geodesic(sales_rep_location, (cust[1], cust[2])).kilometers
                )

                # Generate an HTML plan
                plan = '<ol>'
                for customer in sorted_customers:
                    distance = geodesic(sales_rep_location, (customer[1], customer[2])).kilometers
                    plan += f'<li>{customer[0]} - {distance:.2f} km</li>'
                plan += '</ol>'
                record.route_plan = plan
            else:
                record.route_plan = "No customers assigned to this route."
