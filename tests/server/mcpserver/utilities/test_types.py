import pytest
from inline_snapshot import snapshot

from mcp.server.mcpserver.utilities.types import Audio


def test_audio_accepts_empty_bytes_as_valid_data():
    """Pins the fix for modelcontextprotocol/python-sdk#3656: a truthiness check on
    `data` treated `b""` as missing, though it's a valid (empty) payload."""
    audio = Audio(data=b"")

    assert audio.to_audio_content().data == ""


def test_audio_rejects_neither_path_nor_data():
    with pytest.raises(ValueError) as exc_info:
        Audio()

    assert str(exc_info.value) == snapshot("Either path or data must be provided")


def test_audio_rejects_both_path_and_data():
    with pytest.raises(ValueError) as exc_info:
        Audio(path="sound.wav", data=b"abc")

    assert str(exc_info.value) == snapshot("Only one of path or data can be provided")
