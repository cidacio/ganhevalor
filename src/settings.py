# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tmpl_middleware import TemplateMiddleware
from tekton.gae.middleware.email_errors import EmailMiddleware
from tekton.gae.middleware.json_middleware import JsonMiddleare
from tekton.gae.middleware.parameter import RequestParamsMiddleware
from tekton.gae.middleware.router_middleware import RouterMiddleware, ExecutionMiddleware
from tekton.gae.middleware.webapp2_dependencies import Webapp2Dependencies
from web.seguranca.middleware import SegurancaMiddleware

SENDER_EMAIL = 'cidacio@gmail.com'
WEB_BASE_PACKAGE = "web"
MIDDLEWARES = [SegurancaMiddleware,
               TemplateMiddleware,
               JsonMiddleare,
               EmailMiddleware,
               Webapp2Dependencies,
               RequestParamsMiddleware,
               RouterMiddleware,
               ExecutionMiddleware]

