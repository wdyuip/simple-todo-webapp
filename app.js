document.addEventListener('DOMContentLoaded', () => {
    const addBtn = document.getElementById('add-btn');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    addBtn.addEventListener('click', () => {
        const task = todoInput.value.trim();
        if (task === '') return;

        const li = document.createElement('li');
        li.textContent = task;
        todoList.appendChild(li);

        todoInput.value = '';
    });
});