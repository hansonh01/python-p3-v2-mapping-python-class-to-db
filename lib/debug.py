#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
payroll.save()  

hr = Department.create("Human Resources", "Building C, East Wing")
hr.save()

ipdb.set_trace()
