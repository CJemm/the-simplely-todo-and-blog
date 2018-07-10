# coding: utf-8
from models.mongua import Mongua


class Todo(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('title', str, ''),
        ('completed', bool, False),
    ]

    def update(self, id, form):
        t = self.find(id)
        valid_names = [
            'title',
            'completed'
        ]
        for key in form:
            if key in valid_names:
                setattr(t, key, form[key])
        t.save()
        return t

    def complete(self, id, completed=True):
        t = self.find(id)
        t.completed = completed
        t.save()
        return t