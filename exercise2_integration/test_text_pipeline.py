from text_pipeline import analyze
import pytest

def test_pipeline_positive():
    out = analyze("I love good food")
    assert out["words"] == ["I","love","good","food"]
    assert out["score"] == 2
    assert out["label"] == "pos"

def test_pipeline_negative_mixes():
    out = analyze("I love fries but hate the sauce")
    # 1 positive (love), 1 negative (hate) -> net 0
    assert out["score"] == 0
    assert out["label"] == "neu"

def test_pipeline_all_negative():
    out = analyze("awful bad terrible")
    assert out["label"] == "neg"

# TODO: Write a test case tht include captial letters and punctuation
def test_pipeline_case_and_punctuation():
    out = analyze("AWESOME!!! This food is GREAT.")
    assert out["words"] == ["AWESOME", "This", "food", "is", "GREAT"]
    assert out["score"] == 2
    assert out["label"] == "pos"

# TODO: Write a test case that includes repeated words
def test_pipeline_repeated_words():
    out = analyze("bad bad bad but also good good")
    assert out["words"] == ["bad", "bad", "bad", "but", "also", "good", "good"]
    assert out["score"] == -1
    assert out["label"] == "neg"

# TODO: add the assertion checks
def test_pipeline_unicode_emoji():
    out = analyze("I LOVE THIS 😊👍 but the UI is bad 😡")
    assert out["words"] == ["I", "LOVE", "THIS", "but", "the", "UI", "is", "bad"]
    assert out["score"] == 0
    assert out["label"] == "neu"

# TODO: fix analyze to reject non-string inputs
def test_pipeline_rejects_non_string():
    with pytest.raises(TypeError):
        analyze(123)
