# -*- coding: utf-8 -*-
"""Integration test for combined_example MOE example."""
import testify as T

from moe.optimal_learning.python.constant import TEST_OPTIMIZATION_MULTISTARTS, TEST_OPTIMIZATION_NUM_RANDOM_SAMPLES, TEST_GRADIENT_DESCENT_PARAMETERS

from moe_examples.tests.moe_example_test_case import MoeExampleTestCase
from moe_examples.combined_example import run_example


class CombinedExampleTest(MoeExampleTestCase):

    """Test the combined_example MOE example."""

    def test_example_runs(self):
        """Simple integration test for example."""
        run_example(
                num_to_sample=1,
                verbose=False,
                testapp=self.testapp,
                optimization_info={
                    'num_multistarts': TEST_OPTIMIZATION_MULTISTARTS,
                    'num_random_samples': TEST_OPTIMIZATION_NUM_RANDOM_SAMPLES,
                    'optimization_parameters': TEST_GRADIENT_DESCENT_PARAMETERS._asdict(),
                    })


if __name__ == "__main__":
    T.run()
