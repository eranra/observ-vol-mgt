#  Copyright 2024 IBM, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import common.configuration_api as api

logger = logging.getLogger(__name__)


def feature_extraction(subtype, config, input_data):
    if len(input_data) != 1:
        raise "feature_extraction configuration should have one input"
    signals_list = input_data[0]
    # switch based on the configuration feature_extraction type
    # verify config parameters conform to structure
    if subtype == api.ExtractSubType.PIPELINE_EXTRACT_TSFEL.value:
        tsfel_config = api.FeatureExtractionTsfel(**config)
        logger.debug("using tsfel feature_extraction")
        from feature_extraction.feature_extraction_tsfel import extract
        extracted_signals = extract(tsfel_config, signals_list)
    else:
        raise "unsupported feature_extraction configuration"
    return [extracted_signals]
