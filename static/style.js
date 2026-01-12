function addMovie() {
    const title = document.getElementById("title").value;
    if (title === "") {
        alert("Movie title is required");
        return;
    }
    const year = document.getElementById("year").value;
    if (year === "") {
        alert("Movie year is required");
        return;
    }
    const actor = document.getElementById("actor").value;
    if (actor === "") {
        alert("Movie actor is required");
        return;
    } 

    const listItem = document.createElement("li");
    listItem.innerHTML = "<input type='checkbox'> " + title + ", " + year + ", " + actor + "</input>";
    document.getElementById("movieList").appendChild(listItem);

    alert("Adding movie: " + title + " " + year + " " + actor);
    console.log("Movie was successfully added");

    clearForm();
}

function clearForm() {
    document.getElementById("title").value = "";
    document.getElementById("year").value = "";
    document.getElementById("actor").value = "";
}