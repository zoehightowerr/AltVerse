/*ZOE HIGHTOWER*/
document.addEventListener("DOMContentLoaded", function() {
    var searchField = document.getElementById("search_field");

    var searchForm = document.querySelector("form");
    searchForm.addEventListener("submit", function(event) {
        var query = searchField.value.trim(); 

        if (!query) { 
            event.preventDefault();  
            searchField.value = "";
            searchField.focus();
        }
    });
});
