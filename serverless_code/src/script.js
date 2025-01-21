document.getElementById('addBtn').addEventListener('click', addTodo)

function addTodo() {
    const todoInput = document.getElementById('todoInput').value;

    if(todoInput) {
        fetch('{API_GATEWAAY_INSERT_URL}', {
            method: 'POST',
            body: JSON.stringify({ todo: todoInput }),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            addListItem(data.body);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };
};

function addListItem(data) {
    const list = document.getElementById('todoList');
    list.innerHTML = '';

    body = JSON.parse(data)
    body.forEach((item) => {
        const listItem = document.createElement('li');
        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.classList.add("deleteBtn");

        listItem.textContent = item.todo;
        listItem.appendChild(deleteBtn);
        list.appendChild(listItem);

        deleteBtn.addEventListener("click", () => {
            console.log(listItem)
            deleteTodo(item)
            listItem.remove();
        });
    });
}


function deleteTodo(item) {
    console.log(item)
    console.log(item.todo)
    console.log(typeof item.todo)
    // console.log(typeof item)
    // todo = JSON.parse(item)
    // console.log(typeof todo)
    fetch('{API_GATEWAAY_DELETE_URL}', {
        method: 'POST',
        body: JSON.stringify({ todo: item.todo }),
        headers: { 'Content-Type': 'application/json' }
    })
}