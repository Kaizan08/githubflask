import os
from flask_migrate import Migrate, MigrateCommand
from github import Github

from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'githubflask.sqlite'),
    )

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        g = Github(os.getenv('GHUB_USER'), os.getenv('GHUB_PWD'))
        results = g.search_repositories(query='language:Python',
                                        sort='stars',
                                        order='desc')
        for x in results:
            print(x.name + ' ' + str(x.stargazers_count))
        return results


    from . import db
    db.init_app(app)

    return app