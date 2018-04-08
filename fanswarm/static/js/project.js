const userEditForm = $('.user-edit-form [name=leagues]')

function updateSelected(el) {
  const selected = $(el).find('option:selected').text();
  const option = '.user-edit-form [name=favorite_teams] > option';
  $(option + '[data-league=' + selected + ']').show();
  $(option + ':not([data-league=' + selected + '])').hide();
}

updateSelected(userEditForm);

userEditForm.change(function() {
    updateSelected(this);
});
