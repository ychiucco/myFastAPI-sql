# Import all the models, so that Base has them before being
# imported by Alembic
from .base_class import Base  # noqa
from .school import School  # noqa
from .people import Student  # noqa
from .people import Teacher  # noqa
