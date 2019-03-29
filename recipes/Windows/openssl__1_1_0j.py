'''
Copyright (C) 2019 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os

from recipes.builder import Builder

class Recipe(Builder):
    '''
    Recipe to build libssl.
    '''
    name = "openssl"
    version = "1.1.0j"
    url = "https://www.openssl.org/source/openssl-1.1.0j.tar.gz"
    install_paths = {
        "x86" : {
            "include" : [os.path.join("include", "openssl")],
            "lib" : [
                os.path.join("libssl-1_1.dll"),
                os.path.join("libssl.lib"),
                os.path.join("libcrypto-1_1.dll"),
                os.path.join("libcrypto.lib"),
            ],
        },
        "x64" : {
            "include" : [os.path.join("include", "openssl")],
            "lib" : [
                os.path.join("libssl-1_1-x64.dll"),
                os.path.join("libssl.lib"),
                os.path.join("libcrypto-1_1-x64.dll"),
                os.path.join("libcrypto.lib"),
            ],
        },
    }
    dependencies = ["zlib"]
    toolchain = ["nasm", "perl", "vs2017"]
    build_script = {
        'x86' : '''
            CALL set PATH={libs};%PATH%
            CALL vcvarsall.bat x86
            CALL perl Configure VC-WIN32 zlib --with-zlib-include="{includes}" --with-zlib-lib="{libs}\\zlib.lib"
            CALL nmake
        ''',
        'x64' : '''
            CALL set PATH={libs};%PATH%
            CALL vcvarsall.bat amd64
            CALL perl Configure VC-WIN64A zlib --with-zlib-include="{includes}" --with-zlib-lib="{libs}\\zlib.lib"
            CALL nmake
        ''',
    }