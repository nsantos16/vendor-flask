import logging

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from .models import VendingMachine

logger = logging.getLogger('default-logger')


def get_vending_machine(db: Session):
    try:
        return db.query(VendingMachine).one()
    except NoResultFound:
        logger.error("There is not a vending machine initialized in the DB, checkout the database or run the "
                     "seeding script otherwise")
        raise NoResultFound
    except MultipleResultsFound:
        logger.error("Currently the system only supports a unique vending machine, checkout the database to verify "
                     "there is a unique instance")
        raise MultipleResultsFound
