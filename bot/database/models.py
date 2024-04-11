from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)

    def __str__(self):
        return f"{self.id}:{self.telegram_id}"
