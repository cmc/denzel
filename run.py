import os
from api import app, router

if __name__ == '__main__':
    from api.routes import Compare
    router.add_resource(Compare, "/compare")
    app.debug = True
    app.run(host='0.0.0.0', port=8080, use_reloader=True)
