from ATARI.CardHandler.CardEffects.effect import *
from typing import List, Dict, Type

"""
Used Dynamic class registration via reflection;
to ensure open closed principle is kept when adding new effect types. 
Benefitting also in time complexity 
when looking up effect classes by command string.
"""

EFFECT_CLASS_REGISTRY: Dict[str, Type[Effect]] = {
    "HEAL": HealEffect,
    "DRAW": DrawEffect
}    

def parse_effect(effect_data: List[str]) -> List[Effect]:
    if not effect_data:
        return []
    
    effect_classes = []
    for key in effect_data:
        if "_" in key:
            command, val_str = key.split("_", 1)
            value = int(val_str)  
    
        else: 
            command = key
            value = 1
        
        effect_class = EFFECT_CLASS_REGISTRY.get(command)

        if effect_class:
            effect_instance = effect_class(amount=value)
            effect_classes.append(effect_instance)
        else:
            raise ValueError(f"Unknown effect command: {command}")
    return effect_classes