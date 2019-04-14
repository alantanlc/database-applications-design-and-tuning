##### 
## This section imports the necessary classes and methods from the SQLAlchemy library
####
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

######## IMPORTANT! Change this to your metric number for grading
student_no = 'A0174404L' 
#########################

#####
## This section creates an engine for the PostgreSQL
## and creates a database session s.
#####
username = 'postgres'
password = 'postgres'
dbname = 'cs4221'
engine = create_engine('postgres://%s:%s@localhost:5432/%s' % (username, password, dbname))

Session = sessionmaker(bind=engine)
s = Session()

#####
## Query 
#####
query1 = """SELECT lo.lo_orderkey, p.p_name, s.s_name, lo.lo_orderdate, lo.lo_extendedprice 
			FROM fact_lineorder lo, dim_customer c, dim_part p, dim_supplier s 
			WHERE lo.lo_custkey = c.c_custkey
			AND lo.lo_partkey = p.p_partkey 
			AND lo.lo_suppkey = s.s_suppkey 
			AND c.c_name = 'Customer#000000001';"""

s.execute(query1)

query2 = """SELECT c.c_region, c.c_nation, c.c_mktsegment, sum(lo.lo_extendedprice)
			FROM fact_lineorder lo, dim_customer c, dim_part p
			WHERE lo.lo_custkey = c.c_custkey 
			AND lo.lo_partkey = p.p_partkey
			AND p.p_brand = 'Brand#13'
			GROUP BY c.c_region, c.c_nation, c.c_mktsegment;"""

s.execute(query2)

query3 = """SELECT extract(year from o.o_orderdate) as year, extract(month from o.o_orderdate) as month, count(l.l_orderkey) as num_of_line_orders, sum(l_extendedprice) as sum_ext_price, sum(l_extendedprice * (1 - l_discount)) as sum_disc_ext_price, sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_disc_ext_price_plus_tax, avg(l_quantity) as avg_qty, avg(l_extendedprice) as avg_ext_price, avg(l_discount) as avg_disc
			FROM lineitem l, orders o
			WHERE l.l_orderkey = o.o_orderkey
			GROUP BY extract(year from o.o_orderdate), extract(month from o.o_orderdate)
			ORDER BY extract(year from o.o_orderdate), extract(month from o.o_orderdate);"""

s.execute(query3)


query4 = """SELECT o.o_orderpriority, count(*) as order_count
			FROM orders o
			WHERE exists
				(
					SELECT *
					FROM lineitem l
					WHERE l.l_orderkey = o.o_orderkey
					AND l.l_commitdate < l.l_receiptdate
				)
			GROUP BY o.o_orderpriority
			ORDER BY o.o_orderpriority;"""

s.execute(query4)


s.commit()





