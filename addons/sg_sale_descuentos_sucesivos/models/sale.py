from odoo import models,fields,api
import logging
from odoo.exceptions import UserError, ValidationError
from odoo.addons.sg_sale_descuentos_sucesivos.utils.utils import descuento_sucesivos

_logger = logging.getLogger(__name__)


class SaleOrdeLine(models.Model):
    _inherit = "sale.order.line"

    descuento_1 = fields.Float("%Dsct 1")
    descuento_2 = fields.Float("%Dsct 2")
    descuento_3 = fields.Float("%Dsct 3")

    def validacion_descuentos(self):
        return (self.descuento_1 > 100 or self.descuento_1 < 0) or \
                (self.descuento_2 > 100 or self.descuento_2 < 0) or \
                (self.descuento_3 > 100 or self.descuento_3 < 0)

    @api.constrains('descuento_1','descuento_2','descuento_3')
    def _check_descuentos(self):
        for record in self:
            if record.validacion_descuentos():
                raise UserError("Los descuentos deben ser menores o iguales a 100 y mayores a cero")
    """
    def descuento_unico(self):
        return 100-((100-self.descuento_1)*(100-self.descuento_2)*(100-self.descuento_3)/100**2)
    """       

    @api.onchange("descuento_1","descuento_2","descuento_3")
    def onchange_discount(self):
        """
        self.discount = self.descuento_unico()
        """
        # self puede albergar 1 o más registros [line1,line2,line3]
        for record in self:
            discount = 0 # Valor por defecto inicial, en caso que no tome algun valor tomará 0
            discount = descuento_sucesivos([record.descuento_1,record.descuento_2,record.descuento_3]) # calculo del descuento, se realiza la operación para obtener el valor buscado
            record.discount = discount # se establece el valor calculado
        