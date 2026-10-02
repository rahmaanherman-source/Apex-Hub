"""APEX routing policy.

Every tool dispatch must pass this deterministic boundary before execution.
"""

FORBIDDEN_TOOL_CLASSES = {
    "image_generation",
    "video_generation",
    "audio_generation",
    "image_editing",
    "video_editing",
    "media_upscaling",
    "media_enhancement",
}


class Decision:
    def __init__(self, action: str, reason: str | None = None, tool=None, message: str | None = None):
        self.action = action
        self.reason = reason
        self.tool = tool
        self.message = message

    @property
    def blocked(self) -> bool:
        return self.action == "BLOCK"


def route_request(request, capability_contract, resolver, audit):
    """Resolve a request and enforce the capability boundary.

    The caller supplies resolver and audit implementations so this policy stays
    deterministic and independently testable.
    """
    target_tool = resolver(request)

    if target_tool.class_name in FORBIDDEN_TOOL_CLASSES:
        audit("ROUTING_BLOCKED", {
            "reason": "FORBIDDEN_TOOL_CLASS",
            "tool": target_tool.id,
            "class": target_tool.class_name,
            "request_id": request.id,
        })
        return Decision(
            action="BLOCK",
            reason="FORBIDDEN_TOOL_CLASS",
            message="This system does not authorize image, video, audio, or media-generation tools.",
        )

    if target_tool.name not in capability_contract.allowed:
        audit("ROUTING_BLOCKED", {
            "reason": "TOOL_NOT_IN_CONTRACT",
            "tool": target_tool.id,
            "request_id": request.id,
        })
        return Decision(
            action="BLOCK",
            reason="TOOL_NOT_IN_CONTRACT",
            message="Requested capability is not authorized by the capability contract.",
        )

    return Decision(action="ALLOW", tool=target_tool)
