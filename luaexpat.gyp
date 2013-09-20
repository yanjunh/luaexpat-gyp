{
  'targets': [
    {
      'target_name': 'lxp',
      'type': 'shared_library',
      'sources': [
        'src/lxplib.c',
        'src/lxp.def',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua',
        '<(DEPTH)/third_party/expat/expat.gyp:expat'
      ],
      'copies': [
        { 'destination': '<(PRODUCT_DIR)/lua/lxp',
          'files': [
            'src/lxp/lom.lua'
        ]},
      ],  
    },
  ],
}
