from uuid import uuid4
from pydantic import BaseModel
from .neo4j_connection import Neo4jConnection

class Node(BaseModel):

  @classmethod
  def create(cls, params):
    db = Neo4jConnection()
    with db.session() as session:
      return session.execute_write(cls._create, cls, params)

  @classmethod
  def find(cls, uuid):
    db = Neo4jConnection()
    with db.session() as session:
      return session.execute_read(cls._find, cls, uuid)

  @classmethod
  def exists(cls, key, value):
    db = Neo4jConnection()
    with db.session() as session:
      return session.execute_read(cls._exists, cls, key, value)

  def save(self):
    db = Neo4jConnection()
    with db.session() as session:
      return session.execute_write(self._save, self)

  @classmethod
  def wrap(cls, node):
    return cls(**cls.as_dict(node))

  @classmethod
  def as_dict(cls, node):
    dict = {}
    for items in node.items():
      dict[items[0]] = items[1]
    return dict

  @staticmethod
  def _exists(tx, cls, key, value):
    where_clause = f'{key}: "{value}"'
    query = "MATCH (a:%s {%s}) RETURN a" % (cls.__name__, where_clause)
    result = tx.run(query)
    for row in result:
      return cls.wrap(row['a'])
    return None
  
  @staticmethod
  def _save(tx, self):
    params = []
    for param in self.__fields__.keys():
      params.append(f"a.{param}='{getattr(self, param)}'")
    params_str = ", ".join(params)
    query = """
      MATCH (a:%s {uuid: '%s'})
      SET %s 
      RETURN a
    """ % (self.__class__.__name__, self.uuid, params_str)
    result = tx.run(query)
    for row in result:
      return self.__class__.wrap(row['a'])
    return None
  
  @staticmethod
  def _create(tx, cls, source_params):
    #print(f"SOURCE_PARAMS: {source_params}")
    params = []
    for param in source_params.keys():
      params.append(f"a.{param}='{source_params[param]}'")
    params_str = ", ".join(params)
    query = """
      CREATE (a:%s {uuid: $uuid1})
      SET %s 
      RETURN a
    """ % (cls.__name__, params_str)
    result = tx.run(query, uuid1=str(uuid4()))
    for row in result:
      dict = {}
      for items in row['a'].items():
        dict[items[0]] = items[1]
      return cls(**dict)
    return None

  @staticmethod
  def _find(tx, cls, uuid):
    query = """
      MATCH (a:%s { uuid: $uuid1 })
      RETURN a
    """ % (cls.__name__)
    result = tx.run(query, uuid1=uuid)
    for row in result:
      dict = {}
      for items in row['a'].items():
        dict[items[0]] = items[1]
      return cls(**dict)
    return None