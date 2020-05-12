# -*- coding: utf-8 -*-
import pytest
import yaml

from python.cacl import Calc


class TestCalc:
    @pytest.fixture(autouse=True)
    def instance(self):
        self.calc = Calc()

    @pytest.mark.valid
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./add_data_valid.yaml')))
    def test_add_valid(self, a, b, c):
        result = self.calc.add(a, b)
        print(f"====result:{result}")
        assert c == result

    @pytest.mark.invalid
    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./add_data_invalid.yaml')))
    def test_add_invalid(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            result = self.calc.add(a, b)
            print(f"====result:{result}")
        assert exc_info.type == TypeError

    @pytest.mark.valid
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./div_data_valid.yaml')))
    def test_div_valid(self, a, b, c):
        result = self.calc.div(a, b)
        print(f"====result:{result}")
        assert c == result

    @pytest.mark.invalid
    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./div_data_invalid.yaml')))
    def test_div_invalid_typeerror(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            result = self.calc.div(a, b)
            print(f"====result:{result}")
        assert exc_info.type == TypeError

    @pytest.mark.invalid
    @pytest.mark.parametrize('a,b', [(1.3, 0)])
    def test_div_invalid_zerodivisionerror(self, a, b):
        with pytest.raises(ZeroDivisionError) as exc_info:
            result = self.calc.div(a, b)
            print(f"====result:{result}")
        assert exc_info.type == ZeroDivisionError


if __name__ == '__main__':
    pytest.main()