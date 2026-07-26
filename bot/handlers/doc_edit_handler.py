async def handle_doc_action(client, task, queue_manager, action):
    await client.answer_callback_query(task.callback_query.id, f"Document action {action} not fully implemented.", show_alert=True)
