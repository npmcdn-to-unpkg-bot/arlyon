class FlipRouter(object):

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'flipper':
            return 'flipper'
        elif model._meta.app_label == 'program':
            return 'program'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'flipper':
            return 'flipper'
        elif model._meta.app_label == 'program':
            return 'program'
        return None
