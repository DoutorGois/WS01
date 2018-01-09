#!/opt/conda/bin/python

import time
import sqlite3

import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  create_engine, Sequence
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
session = scoped_session(sessionmaker())
engine = None

class Dataset(Base):
    __tablename__ = "dataset"
    
    id = Column(Integer, Sequence('dset_id_seq'), primary_key=True)
    alias = Column(String(20)) 
    desc = Column(String(400)) 
    
    def __repr__(self):
        return "<DSet({})>".format(self.alias)


class Animal(Base):
    __tablename__ = "animal"
    
    id = Column(Integer, Sequence('animal_id_seq'), primary_key=True)
    alias = Column(String(20)) 
    name = Column(String(10))
    desc = Column(String(120)) 
    
    def __repr__(self):
        return "<Task({}:{})>".format(self.alias,self.desc)

    
class Region(Base):
    __tablename__ = "region"
    
    id = Column(Integer, Sequence('region_id_seq'), primary_key=True)
    alias = Column(String(20)) 
    name = Column(String(10))
    
    def __repr__(self):
        return "<Region({})>".format(self.alias)

    
class Task(Base):
    __tablename__ = "task"
    
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    alias = Column(String(20)) 
    name = Column(String(10))
    desc = Column(String(120)) 
    
    def __repr__(self):
        return "<Task({}:{})>".format(self.alias,self.desc)


def init_db(dbname='data'):
    global engine
    engine = create_engine("sqlite:///" + dbname + ".db", echo=False)
    session.remove()
    session.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)