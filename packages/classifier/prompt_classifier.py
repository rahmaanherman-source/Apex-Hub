"""Pre-generation media classifier.

This is an independent safety gate. It is intentionally conservative and
should be treated as a signal detector, not the sole security control.
"""

PHOTOREALISTIC_SIGNALS = {
    "photorealistic", "photo-realistic", "hyperrealistic", "hyper-realistic",
    "8k", "4k", "ultra hd", "ultra-hd", "high resolution", "high-res",
    "cinematic", "dslr", "shot on", "photograph", "realistic photo",
    "lifelike", "true to life", "ultra detailed", "hyper detailed",
}

MEDIA_VERBS = {
    "generate", "create", "render", "produce", "draw", "paint",
    "illustrate", "visualize", "depict", "show me",
}

MEDIA_NOUNS = {
    "image", "picture", "photo", "photograph", "portrait",
    "video", "animation", "clip", "footage", "scene",
    "artwork", "illustration", "rendering",
}


def classify_prompt(prompt: str):
    normalized = prompt.lower()
    detected_photo = sorted(s for s in PHOTOREALISTIC_SIGNALS if s in normalized)
    has_media_verb = any(v in normalized for v in MEDIA_VERBS)
    has_media_noun = any(n in normalized for n in MEDIA_NOUNS)

    if detected_photo:
        return {
            "verdict": "BLOCKED",
            "reason": "PHOTOREALISTIC_SIGNAL",
            "detail": f"Detected: {detected_photo}",
        }

    if has_media_verb and has_media_noun:
        return {
            "verdict": "BLOCKED",
            "reason": "MEDIA_GENERATION_REQUEST",
            "detail": "Verb + media noun indicates a media-generation request.",
        }

    return {"verdict": "SAFE", "reason": None, "detail": None}


def pre_generation_gate(prompt: str):
    classification = classify_prompt(prompt)
    if classification["verdict"] == "BLOCKED":
        return {
            "action": "BLOCK",
            "reason": classification["reason"],
            "detail": classification["detail"],
        }
    return {"action": "ALLOW", "reason": None, "detail": None}
