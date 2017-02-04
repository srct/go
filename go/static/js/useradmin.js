function filterApplied() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("appliedInput"); // the var that holdes input from text box
  filter = input.value.toUpperCase(); //makes the input all uppercase for some fucking reason
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
