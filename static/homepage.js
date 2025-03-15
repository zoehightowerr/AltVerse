/*ZOE HIGHTOWER*/
$(document).ready(function() {
    $.each(favorites, function(i, id) {
        
        const band = data.find(band => band.id === id);

        if (band) {
            const favorite_item = $(`<a class="favorite-item col-md-3 col-sm-12" href="/view/${id}"></a>`);
            
            favorite_item.append(`<img src="${band.image}" alt="${band.name}" />`);
            favorite_item.append(`<h3>${band.name}</h3>`);
        
            $('#favorite-items').append(favorite_item);
        }        
    });
});
