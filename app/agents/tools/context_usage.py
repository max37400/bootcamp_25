from agents import RunContextWrapper, function_tool


@function_tool
async def get_10_last_context_messages(ctx: RunContextWrapper[None]) -> str:
    """Get context of the dialogue. You must use this tool before EVERY response."""
    history = ctx.context.get("messages", [])
    last_10_messages = history[-10:]

    return str(last_10_messages)