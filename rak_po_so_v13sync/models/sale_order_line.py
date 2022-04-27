# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _purchase_service_create(self, quantity=False):
        res = super(SaleOrderLine, self)._purchase_service_create(quantity=False)
        PurchaseOrderLine = self.env['purchase.order.line'].search([
            ('sale_line_id', '=', self.id)], limit=1)

        if PurchaseOrderLine:
            so = self.env['sale.order'].browse(PurchaseOrderLine.sale_order_id.id)
            PurchaseOrderLine.write({'account_analytic_id': so.analytic_account_id.id})
        return res
