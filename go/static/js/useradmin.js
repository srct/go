function filterApplied() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("appliedInput"); // the var that holdes input from text box
    filter = input.value.toUpperCase(); //makes the input all uppercase so we can eliminate that from the things can break stuff
    table = document.getElementById("appliedTable"); // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); //the table rows
    for (i = 1; i < tr.length; i++) { // loops through the table rows
        td = tr[i].getElementsByTagName("td")[2]; //sets td to the element, gets changed evrey loop itteration
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
                // tr[1].style.display = "No results match your search! ¯\\_(ツ)_/¯"
            }
        }
    }
}

function filterBlocked() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("blockedInput"); // the var that holdes input from text box
    filter = input.value.toUpperCase(); //makes the input all uppercase so we can eliminate that from the things can break stuff
    table = document.getElementById("blockedTable"); // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); //the table rows
    for (i = 1; i < tr.length; i++) { // loops through the table rows
        td = tr[i].getElementsByTagName("td")[2]; //sets td to the element, gets changed evrey loop itteration
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
                // tr[1].style.display = "No results match your search! ¯\\_(ツ)_/¯"
            }
        }
    }
}

function filterCurrent() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("currentInput"); // the var that holdes input from text box
    filter = input.value.toUpperCase(); //makes the input all uppercase so we can eliminate that from the things can break stuff
    table = document.getElementById("currentTable"); // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); //the table rows
    for (i = 1; i < tr.length; i++) { // loops through the table rows
        td = tr[i].getElementsByTagName("td")[2]; //sets td to the element, gets changed evrey loop itteration
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
                // tr[1].style.display = "No results match your search! ¯\\_(ツ)_/¯"
            }
        }
    }
}
