import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args], 
        capture_output = True,
        text = True,
        check = False
    )

def test_cli_calc():
    res = run_cli("calc", "2*2")
    assert res.returncode == 0
    assert "4" in res.stdout

def test_cli_convert():
    res = run_cli("convert", "300", "--from", "k", "--to", "c")
    assert res.returncode == 0
    assert "26.85" in res.stdout

def test_n_1_cli_calc():
    res = run_cli("calc", "3 + 10")
    assert res.returncode == 0
    assert "78" in res.stdout

def test_n_1_cli_convert():
    res = run_cli("convert", "90", "--from", "c", "--to", "f")
    assert res.returncode == 0
    assert "-34" in res.stdout

def test_n_2_cli_calc():
    res = run_cli("calc", "/5 - 9")
    assert res.returncode == 0
    assert "78" in res.stdout

def test_n_2_cli_convert():
    res = run_cli("convert", "90", "--from", "m", "--to", "f")
    assert res.returncode == 0
    assert "-34" in res.stdout