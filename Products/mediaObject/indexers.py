from plone.indexer.decorator import indexer
from .object import IObject
from decimal import Decimal

SHOP_AVAILABLE = True
try:
    from bda.plone.cart import get_item_data_provider
    from bda.plone.shop.dx import IStockBehavior
    from bda.plone.shop.dx import ITradingBehavior
    from bda.plone.shop.dx import IBuyableBehavior
except ImportError:
    SHOP_AVAILABLE = False


@indexer(IStockBehavior)
def product_stock(object, **kw):
    if SHOP_AVAILABLE:
        try:
            if hasattr(object, 'item_available'):
                return object.item_available
            else:
                return ""
        except:
            return ""
    else:
        return ""

@indexer(IBuyableBehavior)
def product_price(object, **kw):
    if SHOP_AVAILABLE:
        try:
            item_data = get_item_data_provider(object)
            net_price = Decimal(item_data.net)
            vat = item_data.vat
            if vat % 2 != 0:
                item_vat = Decimal(vat).quantize(Decimal('1.0'))
            else:
                item_vat = Decimal(vat)
            
            gross_price = net_price + net_price / Decimal(100) * item_vat
            gross_final = gross_price.quantize(Decimal('1.0'))
            return str(gross_final)
        except:
            return ""
    else:
        return ""
        

@indexer(ITradingBehavior)
def product_articleNumber(object, **kw):
    if SHOP_AVAILABLE:
        try:
            if hasattr(object, 'item_number'):
                return object.item_number
            else:
                return ""
        except:
            return ""
    else:
        return ""


@indexer(IObject)
def object_type(object, **kw):
    try:
        terms = []
        if hasattr(object, 'object_type'):
            if object.object_type:
                terms.append(object.object_type) 
        
        if hasattr(object, 'object_category'):
            if object.object_category:
                terms.append(object.object_category) 
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def object_material(object, **kw):
    try:
        terms = []
        if hasattr(object, 'object_material'):
            for material in object.object_material:
                if material['material']:
                    terms.append(material['material'])
        
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def object_technique(object, **kw):
    try:
        terms = []
        if hasattr(object, 'technique'):
            if object.technique:
                terms.append(object.technique) 
        
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def object_number(object, **kw):
    try:
        terms = []
        if hasattr(object, 'object_number'):
            if object.object_number:
                terms.append(object.object_number) 
        
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def object_collection(object, **kw):
    try:
        terms = []
        if hasattr(object, 'administration_name'):
            if object.administration_name:
                terms.append(object.administration_name) 
        
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def objectnumber(object, **kw):
    try:
        terms = []
        if hasattr(object, 'object_number'):
            if object.object_number:
                terms.append(object.object_number) 
        
        return terms
    except:
        return ""

@indexer(IObject)
def object_priref(object, **kw):
    try:
        if hasattr(object, 'priref'):
            if object.priref != None:
                return str(object.priref)
            else:
                return ""
        return ""
    except:
        return ""

@indexer(IObject)
def object_creator(object, **kw):
    try:
        terms = []
        if hasattr(object, 'creator'):
            for creator in object.creator:
                if creator['creator']:
                    terms.append(creator['creator']) 

        if hasattr(object, 'object_author'):
            for author in object.object_author:
                if author['creator']:
                    terms.append(author['creator']) 
        
        return " ".join(terms)
    except:
        return ""

