import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_subtract():
    assert calculator.calculate(10, 5, "subtract") == 5

def test_multiply():
    assert calculator.calculate(10, 5, "multiply") == 50

def test_divide():
    assert calculator.calculate(10, 5, "divide") == 2

def test_negative_add():
    assert calculator.calculate(5, -5, "add") == 0

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

