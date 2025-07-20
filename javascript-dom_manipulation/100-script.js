document.addEventListener('DOMContentLoaded', function () {
  const list = document.querySelector('.my_list');
  const addBtn = document.querySelector('#add_item');
  const removeBtn = document.querySelector('#remove_item');
  const clearBtn = document.querySelector('#clear_list');

  addBtn.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
  });

  removeBtn.addEventListener('click', function () {
    const lastItem = list.lastElementChild;
    if (lastItem) {
      list.removeChild(lastItem);
    }
  });

  clearBtn.addEventListener('click', function () {
    list.textContent = '';
  });
});

