class Repository:
    def __init__(self):
        self._entities = {}

    def get_by_id(self, id_entity):
        """
        This method return the entity which has the same id with id_entity, None otherwise
        :param id_entity: int
        :return: object
        """
        return self._entities.get(id_entity, None)

    def add_entity(self, entity):
        """
        This method add in dictionary of entities a new entity, if id is still available
        :param entity: object
        :return:
        """
        if self.get_by_id(entity.id) is not None:
            raise ValueError("Duplicate error")
        self._entities[entity.id] = entity

    def get_all(self):
        """
        This method return a list with all values from dictionary of entities
        :return:
        """
        return list(self._entities.values())

    def GET_ALL(self):
        return self._entities

    def delete_entity(self, id_entity):
        """
        This method delete an entity from dictionary, if id will be found
        :param id_entity:
        :return:
        """
        if self.get_by_id(id_entity) is None:
            raise ValueError("This entity was not found")
        self._entities.pop(id_entity)

    def modify_entity(self, entity):
        """
        this method modify an entity, without id, from dictionary, if id will be found
        :param entity:
        :return:
        """
        if self.get_by_id(entity.id) is None:
            raise ValueError("This entity eas not found")
        self._entities[entity.id] = entity
