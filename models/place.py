#!/usr/bin/python3
import models

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_type == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id", ondelete="CASCADE", onupdate="CASCADE"),
            primary_key=True,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id", ondelete="CASCADE", onupdate="CASCADE"),
            primary_key=True,
        ),
    )


class Place(BaseModel):
    """Represent a place.
    attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max number of guests
        price_by_night (int): price by night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of amenity ids
    """

    if models.storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=True)
        number_bathrooms = Column(Integer, default=0, nullable=True)
        max_guest = Column(Integer, default=0, nullable=True)
        price_by_night = Column(Integer, default=0, nullable=True)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            backref="place_amenities",
            viewonly=False,
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":

        @property
        def review(self):
            """getter for review"""
            from models.review import Review

            review_list = []
            all_rev = models.storage.all(Review)
            for review in all_rev.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter for amenities"""
            from models.amenity import Amenity

            amenity_list = []
            all_amen = models.storage.all(Amenity)
            for amenity in all_amen.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
