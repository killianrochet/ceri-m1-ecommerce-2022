from typing import Union,Optional

from sqlmodel import Field,SQLModel,create_engine,select,Session

from fastapi import FastAPI
import datetime
from sqlalchemy import create_engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
from google.cloud.sql.connector import Connector,IPTypes
import os

class Item(BaseModel):
    customer_name: str
    customer_address: str
    customer_phone_number: str
    album_id: int
    
#if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
#    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './../../ceri-m1-ecommerce.json'
from dotenv import load_dotenv
load_dotenv()

#iptypes = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
#connector = Connector()
# initialize parameters
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]
INSTANCE_CONNECTION_NAME = os.environ["INSTANCE_CONNECTION_NAME"]

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine("mysql://"+DB_USER+":"+DB_PASS+"@127.0.0.1:3309/"+DB_NAME)
session = Session(bind=engine)
app = FastAPI()

#CREATE TABLE artists(ID int NOT NULL,name varchar(255),PRIMARY KEY(ID));
#CREATE TABLE albums(ID int NOT NULL,name varchar(255),,artist_id int,PRIMARY KEY(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#CREATE TABLE chanson(ID int NOT NULL,name varchar(255),album_id int,artist_id int,PRIMARY KEY(ID),FOREIGN KEY(album_id) REFERENCES albums(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#



#engine = create_engine("mysql://root:supersecret@127.0.0.1:3308/music")
#engine = create_engine("mysql+pymysql://",creator=conn)


class Artists(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    


class Album(Base):
    __tablename__ = "albums2"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Integer)
    category = Column(String,index=True)
    image = Column(String,index=True)
    stock = Column(Integer)

class Song(Base):
    __tablename__ = "songs2"
    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("albums2.id"))
    name = Column(String, index=True)
    duration = Column(Integer)
    album = relationship("Album", back_populates="songs")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_phone_number = Column(String)
    album_id = Column(Integer,ForeignKey("albums.id"))
    date = Column(String)

Album.songs = relationship("Song", order_by=Song.id, back_populates="album")

class Albums_output:
    def __init__(self,id,name,image):
        self.id = id
        self.name = name
        self.image = image
        self.songs = []
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/artiste/{artist_name}")
def read_name_art(artist_name: str):
    with Session(engine) as session:
        statement = select(Artists).where(Artists.name == artist_name)
        art = session.exec(statement).all()
        return(art)

@app.get("/catalogue/albums/{album_id}")
def read_catalogue_art(album_id: int):
    with Session(engine) as session:
        statement = select(Chansons).where(Chansons.album_id == album_id)
        catalogue = session.exec(statement).all()
        return(catalogue)

@app.post("/order/create")
async def create_order(item:Item):
    album = session.query(Album).filter(Album.id == item.album_id).first()
    if album.stock > 0:
        order = Order(
            customer_name=item.customer_name,
            customer_address=item.customer_address,
            customer_phone_number=item.customer_phone_number,
            album_id=item.album_id,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        session.add(order)
        album.stock -= 1
        session.commit()
        return {"message": "Order created successfully"}
    else:
        return {"message": "Stock not available"}

@app.get("/order/list")
def list_orders():
    orders = session.query(Order).all()
    return [
        {
            "customer_name": order.customer_name,
            "customer_address": order.customer_address,
            "customer_phone_number": order.customer_phone_number,
            "album_id": order.album_id,
            "date": order.date,
        }
        for order in orders
    ]


@app.get("/catalogue/artiste/{artist_id}")
def read_catalogue_art(artist_id: int):
    with Session(engine) as session:
        statement = select(Albums).where(Albums.artist_id == artist_id)
        catalogue = session.exec(statement).all()
        return(catalogue)


@app.get("/api/backdoor")
def lol():
    return(INSTANCE_CONNECTION_NAME)

@app.get("/api/test")
def test():
    return("test")

@app.get("/api/albums")
def get_albums():
    albums = session.query(Album).all()
    return [
        {
            "id": album.id,
            "name": album.name,
            "author": album.author,
            "price": album.price,
            "category": album.category,
            "image": album.image,
            "stock": album.stock,
            "songs": [
                {
                    "id": song.id,
                    "song_title": song.name,
                    "duration":song.duration
                }
                for song in album.songs
            ]
        }
        for album in albums
    ]
    


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}