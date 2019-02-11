from typing import List
from src.object_behavior import ObjectBehavior
from src.result import Result, ResultLine

def run_spec(spec_class: ObjectBehavior) -> List[ResultLine]:
    result_lines = []
    spec = spec_class()
    tests = [func for func in dir(spec) if func.startswith('it_') and callable(getattr(spec, func))]
    for test in tests:
        spec._let()
        exception = None

        try:
            getattr(spec, test)()
        except Exception as e:
            exception = str(e)

        result_lines.append(ResultLine(spec_class, test, exception))
        spec._let_go()

    return result_lines

def run_specs(specs: List[ObjectBehavior]):
    result_lines = [] # type: List[ResultLine]
    for spec in specs:
        result_lines = result_lines + run_spec(spec)

    result = Result(result_lines)
    print(result.export())
