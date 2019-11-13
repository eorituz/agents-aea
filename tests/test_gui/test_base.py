# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This test module contains the tests for the `aea gui` sub-commands."""
import io
import os
import shutil
import json

import tempfile

import aea.cli_gui


def create_app():
    app = aea.cli_gui.run_test()
    app.debug = True
    app.testing = True
    return app


class DummyPID:
    """Mimics the behaviour of a process id"""
    def __init__(self, return_code, stdout_str, stderr_str):
        self.return_code = return_code
        self.stdout = io.BytesIO(stdout_str.encode(encoding='UTF-8'))
        self.stderr = io.BytesIO(stderr_str.encode(encoding='UTF-8'))

    def poll(self):
        return self.return_code



class TempCWD:

    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def destroy(self):
        os.chdir(self.cwd)
        try:
            shutil.rmtree(self.temp_dir)
        except (OSError, IOError):
            pass