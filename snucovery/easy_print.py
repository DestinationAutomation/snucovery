import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


#Print out addresses from excel sheets for easy copy and paste into Nessus

def printer(workbook_name):
#Print out addresses from excel workbooks
#Passed workbook_name from __init__.py
#Note: Returns nothing since it only prints

    try:
        pd.set_option('max_colwidth',80)
        ec2 = pd.read_excel(workbook_name , sheet_name = 'Instances')
        ec2ip = ec2['PrivateDnsName'].to_string(index=False)

        print("\n************EC2 Addresses************\n%s\n\n" % (ec2ip))

    except:
        print("\nERROR: no EC2 instances available")
        
    try:
        pd.set_option('max_colwidth',80)
        rds = pd.read_excel(workbook_name, sheet_name = 'Db Instances')
        rdsip = rds['Address'].to_string(index=False)

        print("************RDS Addresses************\n%s\n\n" % (rdsip))

    except:
        print("\nERROR: no RDS instances available")