// hide by default
$("div_id_expires_custom").hide();

// if the expires_custom checkbox is checked..
if ($("#id_expires_5").is(":checked")) {
    // display the field
    $("#div_id_expires_custom").slideDown();
} else {
    // keep it up
    $("#div_id_expires_custom").slideUp();
}

// if the expires_custom checkbox is clicked..
$("#div_id_expires").click(function () {
    // if the expires_custom checkbox is checked..
    if ($("#id_expires_5").is(":checked")) {
        // display the field
        $("#div_id_expires_custom").slideDown();
    } else {
        // keep it hidden
        $("#div_id_expires_custom").slideUp();
    }
})

function httpErrorPopover() {
  var url = document.getElementById("id_target").value
  $.ajax(url,
      {
         statusCode: {
         404: function() {
           console.log("url not found")
           $(this).popover({
             content: "popover text here",
             trigger: 'manual'
           });
           $(this).popover('show');
         }
      }
   });
}
