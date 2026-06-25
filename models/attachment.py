# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
import random

class Attachment(models.Model):
    _inherit = 'ir.attachment'
    
    directory_id = fields.Many2one('document.directory', string='Directory')
    document_tags = fields.Many2many('document.tags', string='Document Tags')
    color = fields.Integer(string='Color Index')
    
    # الحقل الجديد لاختيار أي عدد من المستخدمين لمشاركة المستند معهم
    shared_user_ids = fields.Many2many(
        'res.users', 
        'sh_document_res_users_rel', # اسم جدول الربط في قاعدة البيانات
        'attachment_id', 
        'user_id', 
        string='Shared With'
    )
    
    @api.model
    def create(self, values):
        number = random.randrange(1, 10)
        values['color'] = number
        return super(Attachment, self).create(values)
