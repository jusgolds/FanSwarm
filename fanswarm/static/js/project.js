$('.user-edit-form [name=leagues]').change(function() {
    console.log($(this).find('option:selected').text());
});
