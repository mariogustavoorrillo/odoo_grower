from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date,datetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def cron_rescue_it(self):
        import pdb;pdb.set_trace()
        leads = self.env['crm.lead'].search([('type','=','lead')])
        for lead in leads:
            lead.active = False



class AccountMove(models.Model):
    _inherit = 'account.move'

    def update_narration(self):
        parameter = self.env['ir.config_parameter'].search([('key','=','DEMO-FRANCO')])
        for rec in self:
            rec.narration = parameter.value


class Plantas(models.Model):
    _name = 'grower.planta'

    @api.depends('pedido_ids')
    def _compute_total_sales(self):
        for rec in self:
            res = 0
            for pedido in rec.pedido_ids:
                res = res + pedido.amount_total
            rec.total_sales = res

    @api.model
    def create(self,vals):
        next_code = self.env['ir.sequence'].next_by_code('PLANTA')
        vals['code'] = next_code
        return super(Plantas, self).create(vals)

    name = fields.Char("Plant Name")
    price = fields.Float('Precio')
    code = fields.Char('Codigo')
    total_sales = fields.Float('Monto Ventas',compute=_compute_total_sales,store=True)
    pedido_ids = fields.One2many(comodel_name='grower.pedido',inverse_name='planta_id',string='Pedidos')

class Pedidos(models.Model):
    _name = 'grower.pedido'

    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = rec.planta_id.price * rec.qty

    @api.constrains('qty')
    def check_qty(self):
        if self.qty < 1:
            raise ValidationError('La cantidad debe ser un numero positivo')

    @api.model
    def create(self, vals):
        res = super(Pedidos, self).create(vals)
        partner_id = self.env['res.partner'].search([('ref','=','NWA')])
        if not partner_id:
            raise ValidationError('No esta el proveedor')
        vals_po = {
                'partner_id': partner_id.id,
                'partner_ref': 'Pedido desde Eagan',
                'date_order': str(date.today()),
                }
        po_id = self.env['purchase.order'].create(vals_po)
        return res
        

    planta_id = fields.Many2one('grower.planta','Planta')
    partner_id = fields.Many2one('res.partner',string='Cliente')
    qty = fields.Integer('Cantidad')
    amount_total = fields.Float('Monto total',compute=_compute_amount_total)
