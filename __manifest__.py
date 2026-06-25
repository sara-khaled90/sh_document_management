# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Document Management",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Document Management",
    "summary": "View  Document Module, Filter Document,Document Management,Manage Doc Group By Document, Get Document Details, Document Manage, Manage Directory Document Odoo",
    "description": """This module helps to manage documents easily in odoo. You can create the directory and manage directory wise documents. Users can filter the documents by visible directory & my directory. You can easily group by the documents by directory, custom date & created by. You can easily add custom filters/groups of documents. From the menu bar, the user can see directory tags & document tags. Using a search bar you can search documents details easily. You can download the document from the files in the directory. You can see related documents from the sub-directory.
 Document Management Odoo
 View  Document Module, Filter Document, Group By Document, Get Document Details, Document Manage, Manage Directory Document Odoo
 View  Document Module, Filter Document, Group By Document App, Get Document Details, Document Manage, Manage Directory Document Odoo
Document Management Odoo
 Ver módulo de documento, Filtrar documento, Agrupar por documento, Obtener detalles del documento, Administrar documento, Administrar documento de directorio Odoo
Ver módulo de documento, Filtrar documento, Agrupar por aplicación de documento, Obtener detalles del documento, Administrar documento, Administrar directorio Documento Odoo""",
    "version": "13.0.6",
    "depends": ["base", "mail"],
    "application": True,
    "data": [
        'security/sh_document_security.xml',
            'security/ir.model.access.csv',
            'views/document_view.xml',
            'views/docuement_tags_view.xml',
            'views/directory_tags_view.xml',
            'views/directory_view.xml',
            'views/attachment_view.xml',
            'data/data.xml'
    ],
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/I2RflSl1GyE",
    "auto_install": False,
    "installable": True,
    "price": 24.83,
    "currency": "EUR"
}
