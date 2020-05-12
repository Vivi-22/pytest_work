# -*- coding: utf-8 -*-
import json

import pytest
import yaml

from python.cacl import Calc


class YamlData:
    def get_data(self, data_path):
        data = yaml.safe_load(open(data_path))
        return data


class TestCalc:
    @pytest.fixture(autouse=True)
    def instance(self):
        self.calc = Calc()
        self.steps = YamlData().get_data('./step.yaml')

    data = YamlData().get_data('./data.yaml')

    @pytest.mark.parametrize('a,b,c', data['add']['valid'])
    def calc_add_valid(self, a, b, c):
        for step in self.steps:
            if step == 'add':
                result = self.calc.add(a, b)
                print(f"====result:{result}")
                assert c == result

    @pytest.mark.parametrize('a,b', data['add']['invalid'])
    def calc_add_invalid(self, a, b):
        for step in self.steps:
            if step == 'add':
                with pytest.raises(TypeError) as exc_info:
                    result = self.calc.add(a, b)
                    print(f"====result:{result}")
                assert exc_info.type == TypeError

    @pytest.mark.parametrize('a,b,c', data['sub']['valid'])
    def calc_sub_valid(self, a, b, c):
        result = self.calc.sub(a, b)
        print(f"====result:{result}")
        assert c == result

    @pytest.mark.parametrize('a,b', data['sub']['invalid'])
    def calc_sub_invalid(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            result = self.calc.sub(a, b)
            print(f"====result:{result}")
        assert exc_info.type == TypeError

    @pytest.mark.parametrize('a,b,c', data['mul']['valid'])
    def calc_mul_valid(self, a, b, c):
        result = self.calc.mul(a, b)
        print(f"====result:{result}")
        assert c == result

    @pytest.mark.parametrize('a,b', data['mul']['invalid'])
    def calc_mul_invalid(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            result = self.calc.mul(a, b)
            print(f"====result:{result}")
        assert exc_info.type == TypeError

    @pytest.mark.parametrize('a,b,c', data['div']['valid'])
    def calc_div_valid(self, a, b, c):
        for step in self.steps:
            if step == 'div':
                result = self.calc.div(a, b)
                print(f"====result:{result}")
                assert c == result

    @pytest.mark.parametrize('a,b', data['div']['invalid'])
    def calc_div_invalid_typeerror(self, a, b):
        for step in self.steps:
            if step == 'div':
                with pytest.raises(TypeError) as exc_info:
                    result = self.calc.div(a, b)
                    print(f"====result:{result}")
                assert exc_info.type == TypeError

    @pytest.mark.parametrize('a,b', [(1.3, 0)])
    def calc_div_invalid_zerodivisionerror(self, a, b):
        for step in self.steps:
            if step == 'div':
                with pytest.raises(ZeroDivisionError) as exc_info:
                    result = self.calc.div(a, b)
                    print(f"====result:{result}")
                assert exc_info.type == ZeroDivisionError


if __name__ == '__main__':
    pytest.main()
