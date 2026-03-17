from application.chunker import Chunker
from domain.models import ParagraphUnit

def test_chunker_creates_chunks():
    units = [
        ParagraphUnit(id=1, type="paragraph", text="Hello world"),
        ParagraphUnit(id=2, type="paragraph", text="This is a test"),
        ParagraphUnit(id=3, type="paragraph", text="Another paragraph")
    ]

    chunker = Chunker()
    chunks = chunker.chunk(units)

    assert len(chunks) == 1
    assert chunks[0].paragraph_ids == [1,2,3]

def test_chunker_splits_when_max_length_exceeded():
    units = [
        ParagraphUnit(id=1, type="paragraph", text="A"*40),
        ParagraphUnit(id=2, type="paragraph", text="B"*40),
        ParagraphUnit(id=3, type="paragraph", text="C"*40)
    ]

    chunker = Chunker(max_length=50)
    chunks = chunker.chunk(units)

    assert len(chunks) == 3
    