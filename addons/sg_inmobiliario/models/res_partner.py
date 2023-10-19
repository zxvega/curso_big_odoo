from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = "res.partner"

    birthday = fields.Date(string="Fecha de cumpleaños")
    inmuebles_count = fields.Integer(string="Cantidad de inmuebles",compute="_compute_inmuebles_count")

    def _compute_inmuebles_count(self):
        self.inmuebles_count =  self.env["sg.inmueble"].search_count([("owner_id","=",self.id)])

    def action_view_tree_inmuebles(self):
        return {
            "name":"Inmuebles",
            "type":"ir.actions.act_window",
            "res_model":"sg.inmueble",
            "view_mode":"tree",
            "domain":[("owner_id","=",self.id)]
        }