# -*- coding: utf-8 -*-

# Copyright 2013-2020 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os

common_globals = {}
execfile_('common.py', common_globals)

MODEL_VERSIONS = {
    u'CP960': u'73.83.0.30',
    u'T29G': u'46.83.0.120',
    u'T41P': u'36.83.0.35',
    u'T42G': u'29.83.0.120',
    u'T46G': u'28.83.0.120',
    u'T48G': u'35.83.0.120',
    u'T56A': u'58.83.0.15',
    u'T58': u'58.83.0.15',
    u'W60B': u'77.83.0.85',
    u'W80B': u'103.83.0.80',
}

COMMON_FILES = [
    ('y000000000028.cfg', u'T46-28.83.0.120.rom', 'model.tpl'),
    ('y000000000029.cfg', u'T42-29.83.0.120.rom', 'model.tpl'),
    ('y000000000035.cfg', u'T48-35.83.0.120.rom', 'model.tpl'),
    ('y000000000036.cfg', u'T41-36.83.0.35.rom', 'model.tpl'),
    ('y000000000046.cfg', u'T29-46.83.0.120.rom', 'model.tpl'),
    ('y000000000058.cfg', u'T58V(T56A)-58.83.0.15.rom', 'model.tpl'),
    ('y000000000076.cfg', u'T40G-76.83.0.35.rom', 'model.tpl'),
    ('y000000000073.cfg', u'CP960-73.83.0.30.rom', 'model.tpl'),
]

COMMON_FILES_DECT = [
    {
        'filename': u'y000000000077.cfg',
        'fw_filename': u'W60B-77.83.0.85.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.83.0.90.rom',
            'w56h': u'W56H-61.83.0.90.rom',
            'cp930w': u'CP930W-87.83.0.60.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    },
    {
        'filename': u'y000000000103.cfg',
        'fw_filename': u'W80B-103.93.0.80.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.83.0.90.rom',
            'w56h': u'W56H-61.83.0.90.rom',
            'w59r': u'W59R-115.83.0.10.rom',
            'cp930w': u'CP930W-87.83.0.60.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    }
]


class YealinkPlugin(common_globals['BaseYealinkPlugin']):
    IS_PLUGIN = True

    pg_associator = common_globals['BaseYealinkPgAssociator'](MODEL_VERSIONS)

    # Yealink plugin specific stuff

    _COMMON_FILES = COMMON_FILES

    def configure_common(self, raw_config):
        super(YealinkPlugin, self).configure_common(raw_config)
        for dect_info in COMMON_FILES_DECT:
            tpl = self._tpl_helper.get_template('common/%s' % dect_info[u'tpl_filename'])
            dst = os.path.join(self._tftpboot_dir, dect_info[u'filename'])
            raw_config[u'XX_handsets_fw'] = dect_info[u'handsets_fw']
            raw_config[u'XX_fw_filename'] = dect_info[u'fw_filename']

            self._tpl_helper.dump(tpl, raw_config, dst, self._ENCODING)
