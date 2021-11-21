from flask_script import Manager
from flask_script.commands import Server
from app import initializateApp
from app.settings import setting

configuration = setting['develop']
app = initializateApp(configuration)

manager = Manager(app)
manager.add_command('runserver', Server(host='localhost', port=8100))

if __name__ == '__main__':
    manager.run()
