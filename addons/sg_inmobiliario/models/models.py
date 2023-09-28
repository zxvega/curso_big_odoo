from odoo import models,fields

class TipoInmueble(models.Model):
    _name = "sg.tipo.inmueble"
    _description = "Tipo de Inmueble"

    name = fields.Char("Nombre")


class Inmuebles(models.Model):
    _name = "sg.inmueble"
    _description = "Inmuebles"
    
    name = fields.Char("Nombre")
    tag_ids = fields.Many2many("sg.tag",string="Etiquetas")
    value = fields.Float(string="Valor de propiedad")
    currency_id = fields.Many2one("res.currency",string="Moneda")
    street = fields.Text(string="Dirección")
    partner_ids = fields.Many2many("res.partner",string="Interesados")
    operation = fields.Selection(selection=[('venta','Venta'),('compra','Compra'),('alquiler','Alquiler')],default="venta")
    image = fields.Binary("Imagen")
    type = fields.Many2one("sg.tipo.inmueble",string="Tipo de Inmueble")

    user_id = fields.Many2one("res.users",string="Responsable",default=lambda self:self.env.user.id)
    company_id = fields.Many2one("res.company",string="Compañía",default=lambda self:self.env.company.id)
    owner_id = fields.Many2one("res.partner",string="Propietario")
    date = fields.Date("Fecha de alta")
    codigo_catastral = fields.Char("Código catastral")


class Tags(models.Model):
    _name = "sg.tag"
    _description = "Etiquetas de Inmueble"

    name = fields.Char("Nombre")