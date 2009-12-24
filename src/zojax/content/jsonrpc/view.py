##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from rwproperty import getproperty, setproperty

from zope import interface, component
from zope.proxy import removeAllProxies
from zope.app.intid.interfaces import IIntIdAddedEvent, IIntIdRemovedEvent
from zope.app.container.interfaces import IObjectAddedEvent, IObjectRemovedEvent

from z3c.jsonrpc import publisher

class ContentView(publisher.MethodPublisher):
    """JSON view."""

    def get(self, attrs):
        res = {}
        for attr, params in attrs.items():
            value = getattr(self.context, attr)
            if callable(value):
                kv=[]
                kw = {}
                if params:
                    kv, kw = params
                res[attr] = value(*kv, **kw)
            else:
                res[attr] = value
        return res

    def set(self, attrs):
        for attr, value in attrs.items():
            setattr(self.context, attr, value)
