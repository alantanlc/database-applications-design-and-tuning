import argparse
from sqlalchemy.orm import sessionmaker
import time
from db_connect import get_conn
from sqlalchemy import Column, Integer, Float
import random
from sqlalchemy.ext.declarative import declarative_base

# Declarative Mapping for account table
Base = declarative_base()
class Account(Base):
	__tablename__ = 'account'

	id = Column(Integer, primary_key=True)
	branch = Column(Integer)
	balance = Column(Float)

## Argument parser to take the parameters from the command line
## Example on how to run: python run_exchanges.py 10 READ_COMMITTED
parser = argparse.ArgumentParser()
parser.add_argument('E', type = int, help = 'number of exchanges')
parser.add_argument('I', help = 'isolation level')
args = parser.parse_args()

## Execute an exchange query and return the results
def exchange(sess):
	## 1. Read the balance from a first account A1 (picked at random) into a variable
	a1 = sess.query(Account).filter_by(id = random.randint(1, account_length-1)).first()
	v1 = a1.balance

	## 2. Read the balance from a second account A2 (picked at random) into a variable V2
	a2 = sess.query(Account).filter_by(id = random.randint(1, account_length-1)).first()
	v2 = a2.balance

	## 3. Write the value V1 as the new balance of the account A2
	a2.balance = v1

	## 4. Write the value V2 as the new balance of the account A1
	a1.balance = v2

	sess.commit()

	return

## Create E swap operations
def E_swaps(sess, E):
	start = time.time()

	for i in xrange(0, E):
		while True:
			try:
				exchange(sess)
			except Exception as e:
				print e
				continue
			break
		time.sleep(0.0001)

	stop = time.time()
	return stop-start

## Create the engine and run the exchanges
engine = get_conn()
Session = sessionmaker(bind=engine.execution_options(isolation_level=args.I, autocommit=True))
sess = Session()
account_length = sess.query(Account).count()
time = E_swaps(sess, args.E)
print time