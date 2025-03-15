/*ZOE HIGHTOWER*/
$(document).ready(function () {
    const selectedBands = new Set();
    const selected_genres = new Set();

    var band_count=0;
    var genre_count=0;

    $(".band-btn").on("click", function () {
        const band = $(this).data("value");

        if (selectedBands.has(band)) {
            selectedBands.delete(band);
            $(this).removeClass("btn-primary").addClass("btn-outline-primary");
            band_count--;
        } else {
            selectedBands.add(band);
            $(this).removeClass("btn-outline-primary").addClass("btn-primary");
            band_count++;
        }
    });

    $(".genre-btn").on("click", function () {
        const gen = $(this).data("value");

        if (selected_genres.has(gen)) {
            selected_genres.delete(gen);
            $(this).removeClass("btn-primary").addClass("btn-outline-primary");
            genre_count--;
        } else {
            selected_genres.add(gen);
            $(this).removeClass("btn-outline-primary").addClass("btn-primary");
            genre_count++;
        }
    });

    $("#submit").click(function () {
        if (!check_feilds(genre_count, band_count)) return;

    
        var current_edit = [{
            "id": null,
            "name": $("#input-name").val(),
            "description": $("#input-description").val(),
            "popular albums": [
                {
                    "album": $("#1input-album-name").val(),
                    "cover": $("#1input-album-cover-url").val(),
                    "songs": $("#1input-songs").val().split("\n").map(song => song.trim()).filter(song => song !== ""),
                },
                {
                    "album": $("#2input-album-name").val(),
                    "cover": $("#2input-album-cover-url").val(),
                    "songs": $("#2input-songs").val().split("\n").map(song => song.trim()).filter(song => song !== ""),
                }
            ],
            "monthly listeners": $("#input-listeners").val(),
            "image": $("#input-image").val(),
            "similar artists": Array.from(selectedBands),
            "subgenres": Array.from(selected_genres),
            "members": $("#input-band-members").val().split("\n").map(member => member.trim()).filter(member => member !== "")
        }];
        
        edit_entry(current_edit);
    });
});

function edit_entry(edit){
    $.ajax({
        type: "POST",
        url: "/edit/edit_entry",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(edit),
        success: function (response) {
            var success_alert="<div>New item successfully created.</div>";

            var new_link = $("<a></a>");
            new_link.attr("href", "/view/" + response.id);
            new_link.text("Click Here to See New Page");

            $("#success").append(success_alert);
            $("#success").append(new_link);


            $("#input-name").val("");
            $("#input-listeners").val("");
            $("#input-image").val("");
            $("#input-description").val("");
            $("#input-band-members").val("");
            $("#1input-album-cover-url").val("");
            $("#1input-album-name").val("");
            $("#1input-songs").val("");
            $("#2input-album-cover-url").val("");
            $("#2input-album-name").val("");
            $("#2input-songs").val("");

            $("#input-name").focus();


        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function check_feilds(genre_count,band_count){
    let valid = true;
    let firstErrorField = null;
    $(".error_message").remove();


    if (($("#input-name").val()).trim().length == 0) {
        $("#input-name").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#input-name";
        valid = false;
    }
    if (($("#input-listeners").val()).trim().length == 0) {
        $("#input-listeners").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#input-listeners";
        valid = false;
    }
    else if (isNaN(Number($("#input-listeners").val().replace(/,/g, "")))) {
        $("#input-listeners").after("<span class='error_message'>Must be a number</span>");
        if (!firstErrorField) firstErrorField = "#input-listeners";
        valid = false;
    }    
    if (($("#input-image").val()).trim().length == 0) {
        $("#input-image").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#input-image";
        valid = false;
    }
    if (($("#input-description").val()).trim().length == 0) {
        $("#input-description").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#input-description";
        valid = false;
    }
    if (($("#input-band-members").val()).trim().length == 0) {
        $("#input-band-members").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#input-band-members";
        valid = false;
    }
    if(genre_count==0){
        $(".genre-label").before("<span class='error_message'>Required *Hint: all bands on this website are Alternative Rock* </span>");
        if (!firstErrorField) firstErrorField = ".genre-label";
        valid= false;
    }
    if(band_count==0){
        $(".band-label").before("<span class='error_message'>Required *Help users find your artists!*</span>");
        if (!firstErrorField) firstErrorField = ".band-label";
        valid= false;
    }
    if (($("#1input-album-cover-url").val()).trim().length == 0) {
        $("#1input-album-cover-url").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#1input-album-cover-url";
        valid = false;
    }
    if (($("#1input-album-name").val()).trim().length == 0) {
        $("#1input-album-name").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#1input-album-name";
        valid = false;
    }
    if (($("#1input-songs").val()).trim().length == 0) {
        $("#1input-songs").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#1input-songs";
        valid = false;
    }

    if (($("#2input-album-cover-url").val()).trim().length == 0) {
        $("#2input-album-cover-url").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#2input-album-cover-url";
        valid = false;
    }
    if (($("#2input-album-name").val()).trim().length == 0) {
        $("#2input-album-name").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#2input-album-name";
        valid = false;
    }
    if (($("#2input-songs").val()).trim().length == 0) {
        $("#2input-songs").after("<span class='error_message'>Required</span>");
        if (!firstErrorField) firstErrorField = "#2input-songs";
        valid = false;
    }
    
    if (firstErrorField) {
        $('html, body').animate({
            scrollTop: $(firstErrorField).offset().top - 100
        }, 500);
        $(firstErrorField).focus(); 
    }
    
   return valid;
}

