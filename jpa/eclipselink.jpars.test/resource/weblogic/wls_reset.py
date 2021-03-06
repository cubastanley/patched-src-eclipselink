#
# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v. 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0,
# or the Eclipse Distribution License v. 1.0 which is available at
# http://www.eclipse.org/org/documents/edl-v10.php.
#
# SPDX-License-Identifier: EPL-2.0 OR BSD-3-Clause
#

############################################################################
# Generic script applicable on any Operating Environments (Unix, Windows)
# ScriptName    : wls_reset.py
# Properties    : weblogic.properties
# Author        : Kevin Yuan
############################################################################

#===========================================================================
# Connect to wls server
#===========================================================================

connect('@WL_USR@','@WL_PWD@','t3://@WL_HOST@:@WL_PORT@')

#===========================================================================
# Remove Data Sources using wlst on-line commonds
#===========================================================================

edit()
startEdit()
delete('@DS_NAME@','JDBCSystemResource')
delete('@NON_JTA_DS_NAME@','JDBCSystemResource')
save()
activate()
exit()
