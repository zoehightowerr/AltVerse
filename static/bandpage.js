/*ZOE HIGHTOWER*/
$(document).ready(function() {
    $('#name').text(band.name);
    if((band.name).length > 12){
        $('#name').addClass("smaller_name");
    }

    $('#listeners').append(band["monthly listeners"]);

    $('#image').html('<img src="' + band.image + '"alt="' + band.name + '">');

    $('#description').append(band.description);

    $.each(band["popular albums"], function(i, album) {
        let current_album = $("<div class='album col-md-4 col-sm-12'></div>");
    
        let album_name = $("<div class='album_name'>" + album["album"] + "</div>");
    
        let album_cover = $("<img class='cover' src='" + album["cover"] + "' alt='" + album["album"] + " cover' />");
    
        current_album.append(album_name);
        current_album.append(album_cover);
    
        let song_list = $("<div class='song_list'></div>");
        song_list.text(album["songs"].join(", ")); //join w/ commas for style
    
        current_album.append(song_list);
    
        $("#album_container").append(current_album);
    });
    
    
    
    $.each(band["similar artists"], function(i, artistName){

        const artist = data.find(function(band) {
            return band.name === artistName;
        });
    
        if (artist) {
            var artistId = artist.id;
    
            var artistButton = $("<button></button>");
            artistButton.attr("data-artist-id", artistId); 
            artistButton.text(artistName);
            artistButton.addClass("artist-button btn btn-primary");
            artistButton.on("click", function() {
                window.location.href = "/view/" + artistId; 
            });
    
            $("#similar_bands").append(artistButton);
        }
    });
    
    
    
    $.each(band["subgenres"], function(i, genre) {
        var genreLink = $("<a></a>");
        genreLink.attr("href", "/genres/" + genre.toLowerCase());
        genreLink.text(genre);
        genreLink.addClass("genre-link");
    
        var genreWrapper = $("<div></div>").append(genreLink);
        $("#genres").append(genreWrapper);
    });
    
    $.each(band["members"], function(i, member) {
        var memberlink = $("<a></a>");
        memberlink.attr("href", "/members/" + member.toLowerCase());
        memberlink.text(member);
        memberlink.addClass("member-link");
    
        var memberWrapper = $("<div></div>").append(memberlink);
        $("#members").append(memberWrapper);
    });
    
});
