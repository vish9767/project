class AuthRouter:
    rout_app_labels = {'auth', 'contenttypes','sessions','admin','messages','staticfiles'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.rout_app_labels:
            return 'user_db'
        
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.rout_app_labels:
            return 'user_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.rout_app_labels or
            obj2._meta.app_label in self.rout_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.rout_app_labels:
            return db == 'user_db'     
        return None
