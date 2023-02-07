function addInputFields() {
  let container = document.getElementById('container');

  let itemInput = document.createElement('input');
  itemInput.type = 'text';
  itemInput.name = 'item';
  itemInput.id = 'item';

  let priceInput = document.createElement('input');
  priceInput.type = 'text';
  priceInput.name = 'price';
  priceInput.id = 'price';

  container.appendChild(itemInput);
  container.appendChild(priceInput);
}
