from models.mongua import Mongua


class Blog(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('title', str, ''),
        ('content', str, ''),
        ('author', str, ''),
    ]


class BlogComment(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('content', str, ''),
        ('author', str, ''),
        ('blog_id', int, -1),
    ]
