from flask_script import Manager, Server
from app import create_app
from app.models import Comment, Pitch, User, Vote

app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, User=User,Pitch=Pitch, Comment=Comment, Vote=Vote)

@manager.command
def test():
    """Run the unit tests"""
    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=="__main__":
    manager.run()