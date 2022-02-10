from calendar import month
from email.policy import default
from odoo import models, fields
from datetime import date
from dateutil.relativedelta import relativedelta


class Property(models.Model):
    _name = "estate.property"
    _description = "Property to advertise"

    name = fields.Char("Property name", size=30, required=True)
    description = fields.Char("Property description", size=30)
    post_code = fields.Char("Postal code", size=5)
    date_availability = fields.Date(copy=False, default=date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer("Garden area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[("north", "North"), ("east", "East"), ("south", "South"), ("west", "West")])
    active = fields.Boolean(default=True)
    state = fields.Selection(string="State", copy=False, required=True,
                             selection=[("new", "New"), ("accepted", "Offer Accepted"), ("sold", "Sold"),
                                        ("canceled", "Canceled"), ("received", "Offer Received")],
                             default="new")
