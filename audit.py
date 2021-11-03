#! /usr/bin/python3
#
# Copyright (C) 2021 VMware, Inc. All rights reserved.
#

import argparse
from pyVmomi import vmodl, vim
from pyVim.connect import SmartConnect, Disconnect

parser = argparse.ArgumentParser("Display locally stored audit records.")

parser.add_argument("--host", dest="host", required=True,
                    help="The IP address of the ESXi host")

parser.add_argument("--password", dest="password", required=True,
                    help="Password to log in with");

parser.add_argument("--user", dest="user", required=True,
                    help="User name to log in with")

args = parser.parse_args()

si = SmartConnect(host=args.host,
                  user=args.user,
                  pwd=args.password,
                  disableSslCertValidation=True)

token = None

while True:
   x = si.content.diagnosticManager.FetchAuditRecords(token)

   if len(x.records) == 0:
      break
   else:
      print(x.records)

   token = x.nextToken

