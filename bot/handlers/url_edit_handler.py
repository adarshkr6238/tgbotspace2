async def handle_url_action(client, task, queue_manager, action):
    await client.answer_callback_query(task.callback_query.id, f"URL action {action} not fully implemented.", show_alert=True)
