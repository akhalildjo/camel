# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import pytest

import examples.code.generate_meta_data
import examples.code.task_generation
import examples.evaluation.single_agent
import examples.misalignment.single_agent
import examples.single_agent
from camel.typing import ModelType

parametrize = pytest.mark.parametrize('model', [
    ModelType.STUB,
    pytest.param(None, marks=pytest.mark.model_backend),
])


@parametrize
def test_single_agent(model):
    examples.single_agent.main(model=model)


@parametrize
def test_misalignment_single_agent(model):
    examples.misalignment.single_agent.main(model=model)


@pytest.mark.parametrize('model', [
    ModelType.STUB,
])
def test_evaluation_single_agent(model):
    examples.evaluation.single_agent.main(model=model)


@parametrize
def test_code_generate_metadata(model):
    examples.code.generate_meta_data.main(model=model)


@pytest.mark.parametrize(
    'model',
    [
        ModelType.STUB,
        # The following marking hangs the application. Disabled it for now.
        # pytest.param(None,
        #              marks=[pytest.mark.model_backend, pytest.mark.slow]),
    ])
def test_code_task_generation(model):
    examples.code.task_generation.main(model=model)
