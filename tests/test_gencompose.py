from pathlib import Path

from click.testing import CliRunner
from gencompose import main


def test_special_characters():
    runner = CliRunner()
    file = Path(__file__).parent / 'test_special_chars.yaml'
    result = runner.invoke(main, args=[str(file)])
    print(result.output)
    assert result.exit_code == 0
    assert '"\\\\^"' in result.output
    assert '"2"' in result.output
