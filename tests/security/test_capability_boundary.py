from packages.classifier.prompt_classifier import pre_generation_gate


def test_image_generation_blocked():
    result = pre_generation_gate("Generate a photorealistic image of a sunset")
    assert result["action"] == "BLOCK"
    assert result["reason"] == "PHOTOREALISTIC_SIGNAL"


def test_video_generation_blocked():
    result = pre_generation_gate("Create a video of a cat playing piano")
    assert result["action"] == "BLOCK"
    assert result["reason"] == "MEDIA_GENERATION_REQUEST"


def test_media_editing_signal_blocked():
    result = pre_generation_gate("Render a cinematic portrait")
    assert result["action"] == "BLOCK"


def test_normal_code_request_not_blocked_by_classifier():
    result = pre_generation_gate("Write a Python function to sort a list")
    assert result["action"] == "ALLOW"
