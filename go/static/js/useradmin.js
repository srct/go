//Zosman- This file was created in an effort to make /useradmin more usable. As a responce to issue #119 ; branch 119-search-bar ;
//At the time this was created we had no searching feature of the users and it became somewhat hard to actually manage users
//This file has three js functions, one for each table in /useradmin , the functions allow a user to search through the table

function filterApplied() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("appliedInput"); 
    // the var that holdes input from text box
    filter = input.value.toUpperCase();
     //makes the input all uppercase so we dont have problems with case insensitivity
    table = document.getElementById("appliedTable"); 
    // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); 
    //the table rows
    for (i = 1; i < tr.length; i++) { 
        // loops through the table rows
        td = (tr[i].getElementsByTagName("td")[1] || tr[i].getElementsByTagName("td")[2]);
         //sets td to the element, gets changed evrey loop itteration
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
    input = document.getElementById("blockedInput"); 
    // the var that holdes input from text box
    filter = input.value.toUpperCase(); 
    //makes the input all uppercase so we dont have problems with case insensitivity
    table = document.getElementById("blockedTable"); 
    // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); 
    //the table rows
    for (i = 1; i < tr.length; i++) { 
        // loops through the table rows
        td = (tr[i].getElementsByTagName("td")[1] || tr[i].getElementsByTagName("td")[2]); 
        //sets td to the element, gets changed evrey loop itteration
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
    input = document.getElementById("currentInput");
     // the var that holdes input from text box
    filter = input.value.toUpperCase();
     //makes the input all uppercase so we dont have problems with case insensitivity
    table = document.getElementById("currentTable"); 
    // the table at the moment this is called
    tr = table.getElementsByTagName("tr"); 
    //the table rows
    for (i = 1; i < tr.length; i++) { 
        // loops through the table rows
        td = (tr[i].getElementsByTagName("td")[1] || tr[i].getElementsByTagName("td")[2]);
         //sets td to the element, gets changed evrey loop itteration
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
