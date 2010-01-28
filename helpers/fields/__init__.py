class BinaryField(Field):
    description = _("Binary content field")

    def db_type(self, connection):
        return 'longblob'

    def to_python(self, value):
        if isinstance(value, basestring) or value is None:
            return value
        return smart_unicode(value)

    def get_prep_value(self, value):
        return self.to_python(value)
