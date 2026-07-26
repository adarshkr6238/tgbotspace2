async def handle_audio_action(client, task, queue_manager, action):
    await client.answer_callback_query(task.callback_query.id, f"Audio action {action} not fully implemented.", show_alert=True)
