# controller.py
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar eventos
        self.view.add_button.config(command=self.add_task)
        self.view.delete_button.config(command=self.delete_task)

    def add_task(self):
        task = self.view.get_task_entry()
        if task:
            self.model.add_task(task)
            self.view.add_task_to_listbox(task)
            self.view.clear_task_entry()

    def delete_task(self):
        task_index = self.view.get_selected_task_index()
        if task_index is not None:
            task = self.model.get_tasks()[task_index]
            self.model.delete_task(task)
            self.view.delete_task_from_listbox(task_index)
