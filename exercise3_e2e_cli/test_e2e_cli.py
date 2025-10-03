import subprocess
import sys
import pathlib

HERE = pathlib.Path(__file__).parent

def run(cmd: str) -> str:
    """Run calc.py as a real process, return stdout text."""
    p = subprocess.run([sys.executable, str(HERE/"calculator.py")],
                       input=cmd.encode(),
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       check=False)
    return p.stdout.decode().strip()

def test_add_e2e():
    assert run("add 5 10\n") == "15"

def test_div_e2e():
    assert run("div 9 3\n") == "3"

def test_div_by_zero_e2e():
    assert run("div 1 0\n") == "ERROR"

def test_clamp_e2e():
    assert run("clamp 11 0 10\n") == "10"

def test_bad_input_e2e():
    assert run("multiply 2 3\n") == "ERROR"
    assert run("add two 3\n") == "ERROR"

# add some of the tests made in excercise 1
# def test_sub_e2e():
#     assert run("sub 10 4\n") == "6"
# def test_mul_e2e():
#     assert run("mul 3 5\n") == "15"
# def test_clamp_negative_e2e():
#     assert run("clamp -5 0 10\n") == "0"
# def test_clamp_within_bounds_e2e():
#     assert run("clamp 5 0 10\n") == "5"
# def test_extra_whitespace_e2e():
#     assert run("  add   7    8   \n") == "15"
# def test_multiple_commands_e2e():
#     assert run("add 1 2\nmul 3 4\nsub 5 6\n") == "3\n12\n-1"