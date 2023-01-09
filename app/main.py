from typing import Union,Optional

from sqlmodel import Field,SQLModel,create_engine,select,Session

from fastapi import FastAPI

from google.cloud.sql.connector import Connector,IPTypes
import os
iptypes = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(iptypes)
# initialize parameters
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]
INSTANCE_CONNECTION_NAME = os.environ["INSTANCE_CONNECTION_NAME"]
conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
app = FastAPI()

#CREATE TABLE artists(ID int NOT NULL,name varchar(255),PRIMARY KEY(ID));
#CREATE TABLE albums(ID int NOT NULL,name varchar(255),artist_id int,PRIMARY KEY(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#CREATE TABLE chanson(ID int NOT NULL,name varchar(255),album_id int,artist_id int,PRIMARY KEY(ID),FOREIGN KEY(album_id) REFERENCES albums(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#



#engine = create_engine("mysql://root:supersecret@127.0.0.1:3306/music")
engine = create_engine("mysql+pymysql://",creator=conn)
class Artists(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    


class Chansons(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    time: str
    artist: Optional[int] = Field(default=None,foreign_key="artists.id")
    album_id: Optional[int] = Field(default=None,foreign_key="albums.id")
    
class Albums(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    author: str
    price: int
    category: str
    artist_id: Optional[int] = Field(default=None,foreign_key="artists.id")
    image: str
    
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



@app.get("/catalogue/artiste/{artist_id}")
def read_catalogue_art(artist_id: int):
    with Session(engine) as session:
        statement = select(Albums).where(Albums.artist_id == artist_id)
        catalogue = session.exec(statement).all()
        return(catalogue)




@app.get("/api/album/{album_id}")
def get_list(album_id:int):
    with Session(engine) as session:
        statement = select(Albums).where(Albums.id == album_id)
        allalbums = session.exec(statement).all()
        output = []
        for album in allalbums:
            obj = Albums_output(album.id,album.name,album.image)
            statement_match = select(Chansons).where(Chansons.id == album.id)
            allchants = session.exec(statement_match).all()
            obj.songs = allchants
            output.append(obj)
        return(output)

@app.get("/api/album/song")
def read_songs():
    with Session(engine) as session:
        statement = select(Chansons)
        catalogue = session.exec(statement).all()
        return(catalogue)
@app.get("/catalogue/albums/{album_id}")
def read_catalogue_art(album_id: int):
    with Session(engine) as session:
        statement = select(Chansons).where(Chansons.album_id == album_id)
        catalogue = session.exec(statement).all()
        return(catalogue)


@app.get("/catalogue/artiste/{artist_id}")
def read_catalogue_art(artist_id: int):
    with Session(engine) as session:
        statement = select(Albums).where(Albums.artist_id == artist_id)
        catalogue = session.exec(statement).all()
        return(catalogue)




@app.get("/api/albums")
def get_list():
    with Session(engine) as session:
        statement = select(Albums)
        allalbums = session.exec(statement).all()
        output = []
        for album in allalbums:
            obj = Albums_output(album.id,album.name,album.image)
            statement_match = select(Chansons).where(Chansons.id == album.id)
            allchants = session.exec(statement_match).all()
            obj.songs = allchants
            output.append(obj)
        return(output)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}