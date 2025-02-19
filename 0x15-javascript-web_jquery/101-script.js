$(document).ready(function () {
  // Add new item
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove last item
  $('#remove_item').click(function () {
    const list = $('.my_list li');
    if (list.length > 0) {
      list.last().remove();
    }
  });

  // Clear all items
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
