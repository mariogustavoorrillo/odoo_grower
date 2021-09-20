from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/rescue_it', type='http',auth='none')
    def rescue_it_main(self):
        html_result = "<h2>Rescue IT</h2>"
        uid = request.env.context['uid']
        user = request.env['res.users'].sudo().browse(uid)
        return request.render('odoo_grower.show_rescue_welcome',{'usuario': user.name, 'inv': {}})



    @http.route('/rescue_it/<int:invoice>', type='http',auth='none')
    def rescue_it(self, invoice=None, **kw):
        html_result = "<h2>Rescue IT</h2>"
        import pdb;pdb.set_trace()
        uid = request.env.context['uid']
        user = request.env['res.users'].sudo().browse(uid)
        if invoice:
            inv = request.env['account.move'].sudo().browse(invoice)
        return request.render('odoo_grower.show_rescue_welcome',{'usuario': user.name, 'invoice': inv})
        """
        books = request.env['library.book'].sudo().search([])
        html_result = '<html><body><ul>'
        for book in books:Making a path accessible from the network
            html_result += "<li> %s </li>" % book.name
            html_result += '</ul></body></html>'
        return html_result
        """
