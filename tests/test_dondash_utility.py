import imp
import os
import sys

module_name = 'dondash'

here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)

dondash = imp.load_module(module_name, fp, pathname, description)


class TestDondashVaidator:
    def test_validator_pass(self):
        should_pass = ['9bfd0190354a01329e143c764e10cb60',
                       '4a1a6990ab3d013249a53c764e1094a6',
                       'bbf43f60355a013236633c764e1094a6',
                       'd7986c20ab3801327d0c3c764e109fc9']
        for candidate in should_pass:
            assert dondash.Validator.is_an_id(candidate)

    def test_validator_fail(self):
        should_fail = ['FAILMEPLEASE',
                       '4a1a6990ab3d013249a53c764e1094a',
                       '',
                       1234567890]
        for candidate in should_fail:
            assert not dondash.Validator.is_an_id(candidate)
