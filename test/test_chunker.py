from domain.services.chunker import Chunker
from domain.entities.text_unit import TextUnit

def test_chunker_creates_chunks():
    units = [
        TextUnit(id=1, type="paragraph", text="Hello world"),
        TextUnit(id=2, type="paragraph", text="This is a test"),
        TextUnit(id=3, type="paragraph", text="Another paragraph")
    ]

    chunker = Chunker()
    chunks = chunker.chunk(units)

    assert len(chunks) == 1
    assert chunks[0].unit_ids == [1,2,3]

def test_chunker_splits_when_max_length_exceeded():
    units = [
        TextUnit(id=1, type="paragraph", text="A"*40),
        TextUnit(id=2, type="paragraph", text="B"*40),
        TextUnit(id=3, type="paragraph", text="C"*40)
    ]

    chunker = Chunker(max_length=50)
    chunks = chunker.chunk(units)

    assert len(chunks) == 3
    