import abc
from typing import Set
from src.adapters import orm
from src.domian import model


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def add(self, User: model.User):
        self._add(User)
        self.seen.add(User)

    def get(self, sku) -> model.Product:
        product = self._get(sku)
        if product:
            self.seen.add(product)
        return product

    def get_user(self, User) -> model.User:
        user = self._get_user(User)
        if product:
            self.seen.add(product)
        return product

    @abc.abstractmethod
    def _add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, sku) -> model.Product:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_user(self, User) -> model.User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, product):
        self.session.add(product)

    def _get(self, sku):
        return self.session.query(model.Product).filter_by(sku=sku).first()

    def _get_user(self, User) -> model.User:
        return (
            self.session.query(model.User)
            .join(model.get_user())
        )