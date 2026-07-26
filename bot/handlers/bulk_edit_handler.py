async def handle_bulk_action(client, task, queue_manager, action):
    await client.answer_callback_query(task.callback_query.id, f"Bulk action {action} not fully implemented.", show_alert=True)
