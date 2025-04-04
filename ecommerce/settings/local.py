from .base import *

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL","postgresql://testdb_4qio_user:dyMZeIr3w5cpywknfyPE6yHLjK4pydN7@dpg-cvo33l49c44c73bhvg40-a.oregon-postgres.render.com/testdb_4qio"))
}
 