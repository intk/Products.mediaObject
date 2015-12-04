from plone.indexer.decorator import indexer
from .object import IObject

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
def material(object, **kw):
    try:
        terms = []
        if hasattr(object, 'material'):
            if object.material:
                terms.append(object.material) 
        
        return " ".join(terms)
    except:
        return ""

@indexer(IObject)
def technique(object, **kw):
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
def object_priref(object, **kw):
    try:
        if hasattr(object, 'priref'):
            return object.priref
        return ""
    except:
        return ""

@indexer(IObject)
def maker(object, **kw):
    try:
        terms = []
        if hasattr(object, 'artist'):
            if object.artist:
                terms.append(object.artist) 

        if hasattr(object, 'author'):
            if object.author:
                terms.append(object.author) 
        
        return " ".join(terms)
    except:
        return ""

