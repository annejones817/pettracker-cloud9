import os
from flask_script import Manager

from pettracker import app 

manager = Manager(app)

@manager.command
def run(): 
    port=int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
    
if __name__ == "__main__": 
    manager.run()
        
            