#!/bin/bash
# My Upload Hiptest results

echo "Uploading results to hiptest"

hiptest-publisher --config-file hiptest-publisher.config --push reports/TESTS-mercury_tours_web.functional_negative_tests.xml  --push-format junit
hiptest-publisher --config-file hiptest-publisher.config --push reports/TESTS-mercury_tours_web.functional_positive_tests.xml  --push-format junit
hiptest-publisher --config-file hiptest-publisher.config --push reports/TESTS-mercury_tours_web.navigation_tests.xml  --push-format junit


junit-viewer --results=reports/TESTS-mercury_tours_web.functional_positive_tests.xml --save=reports/pos_results.html
junit-viewer --results=reports/TESTS-mercury_tours_web.functional_negative_tests.xml --save=reports/negative_results.html
junit-viewer --results=reports/TESTS-mercury_tours_web.navigation_tests.xml --save=reports/nav_results.html


echo "Upload complete!"