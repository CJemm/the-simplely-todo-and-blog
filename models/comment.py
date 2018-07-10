# coding: utf-8
from models.mongua import Mongua


class Comment(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('author', str, ''),
        ('content', str, ''),
    ]