import configparser
import datetime
import os

import psycopg2
from pony.orm import Database, PrimaryKey, Optional, Set, Required

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'settings/config.cfg'))
con = psycopg2.connect(**config['database'])

db = Database()
db.bind(**config['database'], provider='postgres')


class ReviewsReview(db.Entity):
    _table_ = 'reviews_review'
    id = PrimaryKey(int, auto=True)
    review = Optional(str, nullable=False, default='')
    is_confirm = Optional(int, default=0)
    order = Required('OrdersOrder', reverse='review', column='order_id', nullable=True)
    user = Required('LoginMyuser', reverse='review', column='user_id', nullable=True)


class OrdersOrder(db.Entity):
    _table_ = 'orders_order'
    id = PrimaryKey(int, auto=True)
    num_order = Optional(str, unique=True, default='')
    order_price = Optional(float)
    payment_state = Optional(bool)
    contract = Optional(str, unique=True, default='')
    manager = Required('LoginMyuser', unique=False, column='manager_id', reverse='order_manager')
    user = Required('LoginMyuser', unique=False, column='user_id', reverse='order_user')
    terms_of_readiness = Optional(int)
    installation_time = Optional(int)
    is_cancel = Optional(bool)
    is_notified = Optional(bool)
    delivery_price = Optional(float)
    extra_charge = Optional(float)
    installation_price = Optional(float)
    note = Optional(str, default='')
    prepayment = Optional(float)
    review = Set(ReviewsReview, nullable=True, reverse='order')


class LoginMyuser(db.Entity):
    _table_ = 'login_myuser'
    id = PrimaryKey(int, auto=True)
    password = Optional(str, default='')
    last_login = Optional(datetime.datetime, nullable=True)
    is_superuser = Optional(bool)
    phone = Optional(str, unique=True, default='')
    email = Optional(str, unique=True, default='')
    first_name = Optional(str, default='')
    last_name = Optional(str, default='')
    patronymic = Optional(str, default='')
    address = Optional(str, default='')
    avatar = Optional(str, default='')
    is_active = Optional(bool)
    is_staff = Optional(bool)
    date_joined = Optional(datetime.datetime, nullable=True)
    preferred_social_network = Optional(int)
    additional_information = Optional(str, default='', nullable=True)
    review = Set(ReviewsReview, nullable=True, reverse='user')
    order_manager = Set(OrdersOrder, nullable=True, reverse='manager')
    order_user = Set(OrdersOrder, nullable=True, reverse='user')
    reg_from_mes = Set('LoginRegisterfrommessangers', nullable=True, reverse='user')


class LoginRegisterfrommessangers(db.Entity):
    _table_ = 'login_registerfrommessangers'
    id = PrimaryKey(int, auto=True)
    messenger = Optional(int)
    id_messenger = Optional(str, unique=True)
    user = Optional(LoginMyuser, nullable=True, column='user_id', reverse='reg_from_mes')
    phone = Optional(str, unique=True)


db.generate_mapping(create_tables=True)
