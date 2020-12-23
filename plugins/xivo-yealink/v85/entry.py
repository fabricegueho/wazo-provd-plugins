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
    u'T27G': u'69.85.0.5',
    u'T30': u'124.85.0.40',
    u'T30P': u'124.85.0.40',
    u'T31': u'124.85.0.40',
    u'T31P': u'124.85.0.40',
    u'T31G': u'124.85.0.40',
    u'T33P': u'124.85.0.40',
    u'T33G': u'124.85.0.40',
    u'T41S': u'66.85.0.5',
    u'T42S': u'66.85.0.5',
    u'T46S': u'66.85.0.5',
    u'T48S': u'66.85.0.5',
    u'T53': u'96.85.0.5',
    u'T53W': u'96.85.0.5',
    u'T54W': u'96.85.0.5',
    u'T57W': u'96.85.0.5',
    u'T58': u'58.85.0.5',
    u'W60B': u'77.85.0.20',
    u'CP960': u'73.85.0.5',
    u'CP920': u'78.85.0.5',

}

COMMON_FILES = [
    ('y000000000069.cfg', u'T27G-69.85.0.5.rom', 'model.tpl'),
    ('y000000000065.cfg', u'T46S(T48S,T42S,T41S)-66.85.0.5.rom', 'model.tpl'),
    ('y000000000066.cfg', u'T46S(T48S,T42S,T41S)-66.85.0.5.rom', 'model.tpl'),
    ('y000000000067.cfg', u'T46S(T48S,T42S,T41S)-66.85.0.5.rom', 'model.tpl'),
    ('y000000000068.cfg', u'T46S(T48S,T42S,T41S)-66.85.0.5.rom', 'model.tpl'),
    ('y000000000073.cfg', u'CP960-73.85.0.5.rom', 'model.tpl'),
    ('y000000000078.cfg', u'CP920-78.85.0.5.rom', 'model.tpl'),
    ('y000000000123.cfg', u'T31(T30,T30P,T31G,T31P,T33P,T33G)-124.85.0.40.rom', 'model.tpl'),
    ('y000000000124.cfg', u'T31(T30,T30P,T31G,T31P,T33P,T33G)-124.85.0.40.rom', 'model.tpl'),
    ('y000000000127.cfg', u'T31(T30,T30P,T31G,T31P,T33P,T33G)-124.85.0.40.rom', 'model.tpl'),
]

COMMON_FILES_DECT = [
    {
        'filename': u'y000000000058.cfg',
        'fw_filename': u'T58-58.85.0.5.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.85.0.20.rom',
            'w56h': u'W56H-61.85.0.20.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    },    
    {
        'filename': u'y000000000077.cfg',
        'fw_filename': u'W60B-77.85.0.20.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.85.0.20.rom',
            'w56h': u'W56H-61.85.0.20.rom',
            'w59r': u'W59R-115.85.0.20.rom',		
            'cp930w': u'CP930W-87.85.0.20.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    },
    {
        'filename': u'y000000000095.cfg',
        'fw_filename': u'T54W(T57W,T53W,T53)-96.85.0.5.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.85.0.20.rom',
            'w56h': u'W56H-61.85.0.20.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    },
    {
        'filename': u'y000000000096.cfg',
        'fw_filename': u'T54W(T57W,T53W,T53)-96.85.0.5.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.85.0.20.rom',
            'w56h': u'W56H-61.85.0.20.rom',
        },
        'tpl_filename': u'dect_model.tpl',
    },
    {
        'filename': u'y000000000097.cfg',
        'fw_filename': u'T54W(T57W,T53W,T53)-96.85.0.5.rom',
        'handsets_fw': {
            'w53h': u'W53H-88.85.0.20.rom',
            'w56h': u'W56H-61.85.0.20.rom',
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
