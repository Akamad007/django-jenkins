INSTALLED_APPS = ('django_hudson',)
DATABASE_ENGINE = 'sqlite3'

if __name__ == "__main__":
    import sys, test_runner as settings
    from django.core.management import execute_manager

    if len(sys.argv) == 1:
            sys.argv.append('test')
    execute_manager(settings)
