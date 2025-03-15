/*ZOE HIGHTOWER*/
$(document).ready(function() {
    function highlightText(text, query) {
        if (!query) return text;
        let regex = new RegExp(`(${query})`, "gi");
        return text.replace(regex, "<span class='highlight'>$1</span>"); 
    }

    $.each(results, function(i, current_band) {
        let name_div = $("<div>", { id: "band-name" });
        let name = $("<h2>").html(highlightText(current_band.name, query)); 
        name_div.append(name);

        let image = $("<img>", { src: current_band.image, class: "band-image", alt: current_band.name});

        let members = $("<p>").html("<strong>Band Members:</strong> " + highlightText(current_band.members.join(", "), query)); 
        let genres = $("<p>").html("<strong>Genres:</strong> " + highlightText(current_band.subgenres.join(", "), query)); 

        let bandElement = $("<a>", { class: "band col-md-3", href: "/view/" + current_band.id });
        bandElement.append(name_div);
        bandElement.append(image);
        bandElement.append(members);
        bandElement.append(genres);

        $(".results").append(bandElement);
    });
});
