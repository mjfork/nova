# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack LLC.
# Copyright 2012 Michael Still and Canonical Inc
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import Index, MetaData, Table


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    for table in ['block_device_mapping',
                  'consoles',
                  'volumes']:
        t = Table(table, meta, autoload=True)
        i = Index('%s_instance_uuid_idx' % table, t.c.instance_uuid)
        i.create(migrate_engine)


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    for table in ['block_device_mapping',
                  'consoles',
                  'volumes']:
        t = Table(table, meta, autoload=True)
        i = Index('%s_instance_uuid_idx' % table, t.c.instance_uuid)
        i.drop(migrate_engine)
