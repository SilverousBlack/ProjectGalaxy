import typing

from .meta import FloatRanged

class Galaxy:
    pass

class Galaxy:
    """# Galaxy
    
    Relevant values for galaxies
    """
    
    # required attributes
    object_id: int
    """## `object_id`
    
    Galaxy identification number
    
    * type: `int`
    """
    right_ascension: typing.Annotated[float, FloatRanged(0, 360)]
    """## `right_ascension`
    
    Galaxy right ascension in degrees
    * type: `float`
    * minimum: 0
    * maximum: 360
    """
    declination: typing.Annotated[float, FloatRanged(0, 360)]
    """## `declination`
    
    Galaxy decliantion in degrees
    * type: `float`
    * minimum: 0
    * maximum: 360
    """
    redshift: float
    """## `redshift`
    
    Galaxy redshift (`z`)
    * type: `float`
    """
    
    # optional attributes
    name: str
    
    def __generate_default_name(self):
        return hex(self.object_id).upper()
    
    def __init__(self, *, other: Galaxy = None, **params) -> None:
        attributes = [
            "object_id",
            
        ]
        if other is not None:
            self.object_id = other.object_id
        else:
            try:
                for attr in attributes:
                    setattr(self, attr, params[attr])
            except IndexError as e:
                raise AttributeError(f"Missing attribute: {attr}")
        
        self.name = params["name"] if "name" in params.keys() else self.__generate_default_name()
    
    def __repr__(self):
        return "Galaxy #{} [{}]: RA@{:.6f} DEC@{:.6f} Z@{:.6f}".format(self.object_id, self.name, self.right_ascension, self.declination, self.redshift)
    
    @property
    def obj_id(self) -> int:
        return self.object_id
    