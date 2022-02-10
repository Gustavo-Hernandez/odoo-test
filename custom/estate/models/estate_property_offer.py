from odoo import models, fields


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer"

    price = fields.Float(string="Offering")
    status = fields.Selection(string="Status", selection=[
                              ('accepted', 'Accepted'), ('refused', 'Refused')],
                              copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
