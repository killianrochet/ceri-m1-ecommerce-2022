from typing import Union,Optional

from sqlmodel import Field,SQLModel,create_engine,select,Session

from fastapi import FastAPI

app = FastAPI()

#CREATE TABLE artists(ID int NOT NULL,name varchar(255),PRIMARY KEY(ID));
#CREATE TABLE albums(ID int NOT NULL,name varchar(255),artist_id int,PRIMARY KEY(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#CREATE TABLE chanson(ID int NOT NULL,name varchar(255),album_id int,artist_id int,PRIMARY KEY(ID),FOREIGN KEY(album_id) REFERENCES albums(ID),FOREIGN KEY(artist_id) REFERENCES artists(ID));
#



engine = create_engine("mysql://root:supersecret@127.0.0.1:3306/music")
class Artists(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
class Albums(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    artist_id: Optional[int] = Field(default=None,foreign_key="artists.id")
    
class Chanson(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    artist_id: Optional[int] = Field(default=None,foreign_key="artists.id")
    album_id: Optional[int] = Field(default=None,foreign_key="albums.id")
    
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/artiste/{artist_name}")
def read_name_art(artist_name: str):
    with Session(engine) as session:
        statement = select(Artists).where(Artists.name == artist_name)
        art = session.exec(statement).all()
        return(art)

@app.get("/catalogue/{artist_id}")
def read_catalogue_art(artist_id: int):
    with Session(engine) as session:
        statement = select(Albums).where(Albums.artist_id == artist_id)
        catalogue = session.exec(statement).all()
        return(catalogue)
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}