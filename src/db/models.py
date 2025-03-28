from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean,
    ForeignKey, Date, Text, CheckConstraint
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    event_name = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    point_type = Column(String)
    scoring_method = Column(String)
    source_id = Column(Integer, unique=True, nullable=False)

class Pair(Base):
    __tablename__ = 'pairs'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    pair_position = Column(String, CheckConstraint("pair_position IN ('NS', 'EW')"))

class PairResult(Base):
    __tablename__ = 'pair_results'
    id = Column(Integer, primary_key=True)
    pair_id = Column(Integer, ForeignKey('pairs.id'))
    rank = Column(Integer)
    score = Column(Float)
    percentage = Column(Float)
    masterpoints = Column(Float, default=0)

class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    board_number = Column(Integer)
    dealer = Column(String(1))
    vulnerability = Column(String)

class BoardResult(Base):
    __tablename__ = 'board_results'
    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    pair_id = Column(Integer, ForeignKey('pairs.id'))
    opponent_pair_id = Column(Integer, ForeignKey('pairs.id'))
    contract = Column(String)
    declarer = Column(String(1))
    lead = Column(String)
    tricks = Column(Integer)
    score = Column(Integer)
    matchpoints = Column(Float)
    rank_percentage = Column(Float)
    bidding_comment = Column(Text)
    hand_comment = Column(Text)

class HandRecord(Base):
    __tablename__ = 'hand_records'
    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    north_hand = Column(String)
    east_hand = Column(String)
    south_hand = Column(String)
    west_hand = Column(String)
    hcp_north = Column(Integer)
    hcp_east = Column(Integer)
    hcp_south = Column(Integer)
    hcp_west = Column(Integer)

class Traveller(Base):
    __tablename__ = 'travellers'
    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    ns_player1_id = Column(Integer, ForeignKey('players.id'))
    ns_player2_id = Column(Integer, ForeignKey('players.id'))
    ew_player1_id = Column(Integer, ForeignKey('players.id'))
    ew_player2_id = Column(Integer, ForeignKey('players.id'))
    contract = Column(String)
    declarer = Column(String(1))
    lead = Column(String)
    tricks = Column(Integer)
    ns_score = Column(Integer)
    ew_score = Column(Integer)
    ns_matchpoints = Column(Integer)
    ew_matchpoints = Column(Integer)

class Auction(Base):
    __tablename__ = 'auctions'
    id = Column(Integer, primary_key=True)
    board_result_id = Column(Integer, ForeignKey('board_results.id'))
    comment = Column(Text)

class AuctionCall(Base):
    __tablename__ = 'auction_calls'
    id = Column(Integer, primary_key=True)
    auction_id = Column(Integer, ForeignKey('auctions.id'))
    position = Column(String(1))
    call = Column(String)
    alert = Column(Boolean, default=False)
    explanation = Column(Text)
    call_order = Column(Integer)
