const addForm = document.querySelector("form.add");
const ul = document.querySelector("ul.todos");
const searchFormInput = document.querySelector("form.search input");


// Function to fetch todos from Django API
const fetchTodos = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/task/');
    if (!response.ok) {
      throw new Error('Failed to fetch todos');
    }
    const data = await response.json();
    console.log(data)
    // Clear existing todos before adding fetched ones
    ul.innerHTML = '';
    data.forEach(todo => {
      handleAddItem(todo.title, todo.id);
    });
  } catch (error) {
    console.error('Error fetching todos:', error.message);
  }
};



// Function to make a POST request to Django API to add a new todo
const addTodo = async (inputValue) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/task-create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title: inputValue }),
    });
    if (!response.ok) {
      throw new Error('Failed to add todo');
    }
    // After adding the todo successfully, fetch updated todo list
    fetchTodos();
  } catch (error) {
    console.error('Error adding todo:', error.message);
  }
};

//ADD NEW TODO
const handleAddItem = (inputValue, todoId) => {
  const html = `
  <li id="${todoId}" class="list-group-item"> 
  <div class="task-content">  <input class="form-check-input me-2" type="checkbox" id="checkboxNoLabel" value="" aria-label="...">
    <span class="task-span">${inputValue}</span>
  </div>
  <i class="far fa-trash-alt delete"></i> 
</li>
  `;
  ul.innerHTML += html;
};

addForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const inputValue = addForm.add.value;
  if (inputValue.length) {
    addTodo(inputValue);
    addForm.add.value = "";
  }
});

// Function to toggle strikethrough on task completion
const toggleStrikethrough = (checkbox, task) => {
  if (checkbox.checked) {
    task.innerHTML = `<s>${task.innerText}</s>`;
  } else {
    task.innerHTML = task.innerText.replace('<s>', '').replace('</s>', '');
  }
};

// Function to make a DELETE request to Django API to remove a todo
const deleteTodo = async (todoId) => {
  try {
    const response = await fetch(`/api/todos/${todoId}/`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to delete todo');
    }
    // If deletion is successful, fetch updated todo list
    fetchTodos();
  } catch (error) {
    console.error('Error deleting todo:', error.message);
  }
};

//REMOVE TODO
ul.addEventListener("click", (e) => {
  if (e.target.classList.contains("delete")) {
    const todoId = e.target.parentElement.id;
    deleteTodo(todoId);
  }
});

// Event listener for toggling strikethrough on task completion
ul.addEventListener("click", (e) => {
  if (e.target.classList.contains("form-check-input")) {
    const checkbox = e.target;
    const task = checkbox.parentElement.querySelector(".task-span");
    toggleStrikethrough(checkbox, task);
  }
});

//SEARCH INPUT: PREVENT DEFAULT ACTION - LITTLE BUG I FOUND IN THE COURSE PROJECT
searchFormInput.parentElement.addEventListener("submit", (e) =>
  e.preventDefault()
);

//SEARCH AND FILTER TODOS
const filterItems = (value) => {
  Array.from(ul.children).forEach((li) => {
    if (!li.textContent.toLowerCase().includes(value))
      li.classList.add("filtered");
    else li.classList.remove("filtered");
  });
};

searchFormInput.addEventListener("keyup", (e) => {
  const value = searchFormInput.value.toLowerCase().trim();
  filterItems(value);
});



// Fetch todos when the page loads
fetchTodos();


