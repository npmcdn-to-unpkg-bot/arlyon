class FlipRouter(object):

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'flipper':
            return 'flipper'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'flipper':
            return 'flipper'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if model._meta.app_label == 'flipper':
            return 'flipper'
        return None

        # if obj1._meta.app_label == 'auth' or \
        #    obj2._meta.app_label == 'auth':
        #    return True
        # return None
