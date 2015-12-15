#!/usr/bin/env python
# -*- coding: utf-8 -*-


from zope import schema
from zope.interface import Interface
from five import grok
from Products.mediaObject import MessageFactory as _

class IListField(Interface):
    pass

class ListField(schema.List):
    grok.implements(IListField)
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

class IArtist(Interface):
	creator = schema.TextLine(title=_(u'Artist'), required=False)
	role = schema.TextLine(title=_(u'Role'), required=False)
	qualifier = schema.TextLine(title=_(u'Qualifier'), required=False)
	date_of_birth = schema.TextLine(title=_(u'Date of birth'), required=False)
	date_of_death = schema.TextLine(title=_(u'Date of death'), required=False)

class IProductionPeriod(Interface):
	place = schema.TextLine(title=_(u'Place'), required=False)
	period = schema.TextLine(title=_(u'Period'), required=False)
	reason = schema.TextLine(title=_(u'Reason'), required=False)
	notes = schema.TextLine(title=_(u'Notes'), required=False)

class IDating(Interface):
	start = schema.TextLine(title=_(u'Start'), required=False)
	end = schema.TextLine(title=_(u'End'), required=False)
	start_precision = schema.TextLine(title=_(u'Precision'), required=False)
	end_precision = schema.TextLine(title=_(u'Precision'), required=False)

class IDimensions(Interface):
	type = schema.TextLine(title=_(u'Type'), required=False)
	value = schema.TextLine(title=_(u'Value'), required=False)
	unit = schema.TextLine(title=_(u'Unit'), required=False)
	part = schema.TextLine(title=_(u'Part'), required=False)
	notes = schema.TextLine(title=_(u'Notes'), required=False)

class IDescription(Interface):
	description = schema.TextLine(title=_(u'Description'), required=False)

class IMaterial(Interface):
	material = schema.TextLine(title=_(u'Material'), required=False)


class IInscription(Interface):
	type = schema.TextLine(title=_(u'Type'), required=False)
	content = schema.TextLine(title=_(u'Content'), required=False)

class IReproductionReference(Interface):
	reference = schema.TextLine(title=_(u'Reproduction reference'), required=False)
