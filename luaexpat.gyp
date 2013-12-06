{
  'targets': [
    {
      'target_name': 'lxp',
      'type': 'shared_library',
      'product_dir': "<(PRODUCT_DIR)",
      'sources': [
        'src/lxplib.c',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua',
        '<(DEPTH)/third_party/expat/expat.gyp:expat'
      ],
      'conditions': [
        ['OS == "win"', {
          'sources': [
            'src/lxp.def',
          ],
        }],
        ['OS == "linux"', {
          'product_prefix': '',
          'cflags!': ['-fvisibility=hidden'],
        }],
      ],
      'copies': [
        { 'destination': '<(PRODUCT_DIR)/lxp',
          'files': [
            'src/lxp/lom.lua'
        ]},
      ],  
    },
  ],
}
